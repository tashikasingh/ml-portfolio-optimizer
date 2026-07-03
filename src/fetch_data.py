import yfinance as yf
import pandas as pd
import os

# Define the stocks we want in our portfolio
TICKERS = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

# Date range for historical data
START_DATE = "2019-01-01"
END_DATE = "2025-01-01"

def fetch_data(tickers, start, end):
    """Download historical price data for given tickers."""
    print(f"Fetching data for: {tickers}")
    data = yf.download(tickers, start=start, end=end)
    return data

def save_data(data, filename="data/raw_prices.csv"):
    """Save data to CSV, creating the data folder if needed."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    data.to_csv(filename)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    df = fetch_data(TICKERS, START_DATE, END_DATE)
    save_data(df)
    print(df.head())