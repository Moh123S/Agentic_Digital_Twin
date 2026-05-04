import pandas as pd
import numpy as np

def clean_industrial_data(file_path):
    # 1. Load Data
    df = pd.read_csv(file_path)
    print("📊 Raw Data Loaded. Checking for mess...")

    # 2. Convert Flow to Numeric (Errors will become NaN)
    df['flow'] = pd.to_numeric(df['flow'], errors='coerce')

    # 3. Handle Missing Values (Linear Interpolation)
    df['temp'] = df['temp'].interpolate(method='linear')
    df['flow'] = df['flow'].fillna(df['flow'].median())

    # 4. Handle Outliers (Z-Score Method)
    # Agar vibration 3 standard deviation se upar hai, toh use limit kar do
    upper_limit = df['vibration'].mean() + 3 * df['vibration'].std()
    df.loc[df['vibration'] > upper_limit, 'vibration'] = upper_limit

    # 5. Feature Engineering (Industrial KPI)
    # Pump Efficiency ka ek naya column banao (Flow/Temp ratio)
    df['efficiency_index'] = df['flow'] / (df['temp'] + 1)

    df.to_csv('src/data/cleaned_sensor_data.csv', index=False)
    print("✅ Data Cleaned & Saved to 'data/cleaned_sensor_data.csv'")

if __name__ == "__main__":
    clean_industrial_data('data/raw_sensor_data.csv')