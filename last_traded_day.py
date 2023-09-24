import yfinance as yf
from datetime import timedelta

data = yf.download("RELIANCE.NS", period="1d")
print(type(data))
current_day = data.index[-1].strftime('%Y-%m-%d')
next_day = (data.index[-1] + timedelta(days=1)).strftime('%Y-%m-%d')
print(current_day, next_day)

tickers = ["RELIANCE.NS", "20MICRONS.NS"]
df = yf.download(tickers, start=current_day, end=next_day)
print(df)