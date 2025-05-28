# Aircraft Health Monitoring Dashboard

This project is an MVP dashboard for monitoring aircraft maintenance logs and detecting anomalies.

## Features

- **File Upload:** Upload CSV maintenance logs via a web form.  
- **AWS S3 Storage:** Automatically uploads and downloads CSV files to/from an S3 bucket.  
- **Anomaly Detection:** Uses Isolation Forest to detect sensor anomalies.  
- **Trend Visualization:** Hourly trend charts for key sensor readings.  
- **Interactive Dashboard:** Built with Flask and Plotly Dash for a user-friendly interface.

## Tech Stack

- **Backend:** Python, Flask  
- **Dashboard:** Plotly Dash  
- **Data Processing:** pandas, scikit-learn  
- **Cloud:** AWS S3 via boto3  
- **Frontend:** HTML, CSS

## Setup & Run

1. **Clone repository**  
   ```bash
   git clone https://github.com/mingunC/aircraft-health-dashboard.git
   cd aircraft-health-dashboard