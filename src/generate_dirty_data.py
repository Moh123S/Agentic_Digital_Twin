import pandas as pd
import numpy as np
import os

os.makedirs('data', exist_ok=True)

def generate_messy_data(samples=2000):
    t = np.linspace(0, 100, samples)
    
    # Sensors with noise
    temp = 60 + 5 * np.sin(t) + np.random.normal(0, 2, samples)
    vibration = 2 + 0.5 * np.cos(t) + np.random.normal(0, 0.5, samples)
    flow = 50 + np.random.normal(0, 5, samples)
    
    df = pd.DataFrame({'timestamp': pd.date_range(start='2026-01-01', periods=samples, freq='min'),
                       'temp': temp, 'vibration': vibration, 'flow': flow})
    
    df['flow'] = df['flow'].astype(object)
    
    # --- YAHAN SE MESS SHURU HOTA HAI ---
    # 1. Missing values (Sensors going offline)
    df.loc[np.random.choice(df.index, 100), 'temp'] = np.nan
    
    # 2. Outliers (Sensor Malfunction)
    df.loc[np.random.choice(df.index, 20), 'vibration'] = 99.9
    
    # 3. String errors (Wrong data types)
    df.loc[5, 'flow'] = "ERROR_500" 
    
    df.to_csv('data/raw_sensor_data.csv', index=False)
    print("⚠️ Success: Dirty Data generated. Ab isse saaf karke dikhao!")

if __name__ == "__main__":
    generate_messy_data()