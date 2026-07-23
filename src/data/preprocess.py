import pandas as pd

def to_numeric(df):
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'],errors='coerce')
    return df

def fill_na(df):
    df['TotalCharges'] = df.fillna(df['TotalCharges'].mean())
    return df

def remove_space(df):
    target_cols = [
    col for col in df.select_dtypes(include=['object', 'string']).columns
    if df[col].astype(str).str.contains(' ').any()
    ]
    for col in target_cols:
        df[col] =  df[col].str.replace(' ', '')
    return df

def encode_columns(df):
    df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
    df['Contract'] = df['Contract'].map({
        'Month-to-month': 0,
        'Oneyear': 1,
        'Twoyear': 2
    })
    return df