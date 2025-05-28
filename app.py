from flask import Flask, render_template, request, redirect, url_for
import os
from data_processing import load_data, detect_anomalies, prepare_trends
from models import upload_to_s3, download_from_s3
import dash
from dash import dcc, html
import plotly.express as px
from config import AWS_S3_BUCKET

UPLOAD_FOLDER = "uploads/"
DATA_FILE = os.path.join(UPLOAD_FOLDER, "maintenance_logs.csv")

server = Flask(__name__)
server.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create Dash app
app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/')

@app.server.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        filepath = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(filepath)
        # upload to S3
        upload_to_s3(filepath, f"data/{f.filename}")
        return redirect(url_for('dashboard'))
    return render_template('index.html', bucket=AWS_S3_BUCKET)

@app.server.route('/dashboard/')
def dashboard():
    # download latest file from S3
    download_from_s3("data/maintenance_logs.csv", DATA_FILE)
    df = load_data(DATA_FILE)
    df = detect_anomalies(df, feature_cols=['sensor1', 'sensor2', 'sensor3'])
    trend = prepare_trends(df, 'sensor1')

    fig_trend = px.line(trend, title="Sensor1 Hourly Trend")
    fig_anom = px.scatter(df, x='timestamp', y='sensor1',
                          color=df['anomaly'].map({True: 'Anomaly', False: 'Normal'}),
                          title="Anomaly Detection on Sensor1")

    return app.index()  # placeholder; Dash layout below handles rendering

# Dash layout
app.layout = html.Div([
    html.H1("Aircraft Health Monitoring Dashboard"),
    dcc.Graph(figure=fig_trend),
    dcc.Graph(figure=fig_anom)
])

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=5000)