def clean_data(df):
    df.dropna(inplace=True)  # Remove missing values
    df['Close'] = df['Close'].apply(lambda x: float(x))  # Ensure correct data type
    return df
