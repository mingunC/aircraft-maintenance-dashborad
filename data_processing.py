import pandas as pd
from sklearn.ensemble import IsolationForest

def load_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, parse_dates=['timestamp'])
    df.sort_values('timestamp', inplace=True)
    return df

def detect_anomalies(df: pd.DataFrame, feature_cols: list):
    model = IsolationForest(contamination=0.01, random_state=42)
    df['anomaly'] = model.fit_predict(df[feature_cols])
    # mark anomalies as True
    df['anomaly'] = df['anomaly'] == -1
    return df

def prepare_trends(df: pd.DataFrame, feature: str):
    # resample hourly
    trends = df.set_index('timestamp')[feature].resample('H').mean().fillna(method='ffill')
    return trends