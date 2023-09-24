import yfinance as yf
import time

from symbols import symbols_NS as tickers
from main import is_bullish_candle, is_bullish_hammer_candle

start_time = time.time()

# Initialize empty lists to store matched tickers
bullish_tickers = []
hammer_tickers = []

def get_matched_tickers():
   start_date = "2023-09-01"
   end_date = "2023-09-02"
   
   # List of tickers to check
   # tickers = ["RELIANCE.NS", "20MICRONS.NS"]
   
   df = yf.download(tickers, start=start_date, end=end_date)
   end1 = time.time() - start_time
   print(f'Download Completed in {end1}')
   
   for ticker in tickers:
      # last_open = data["Open"][ticker]
      # last_high = data["High"][ticker]
      # last_low = data["Low"][ticker]
      # last_close = data["Close"][ticker]

      # open = last_open.iloc[0]
      # high = last_high.iloc[0]
      # low = last_low.iloc[0]
      # close = last_close.iloc[0]

      open = df[('Open', ticker)].iloc[0]
      high = df[('High', ticker)].iloc[0]
      low = df[('Low', ticker)].iloc[0]
      close = df[('Close', ticker)].iloc[0]
     
      # print(close)
      bullish_status = is_bullish_candle(open, high, low, close)
      hammer_status = is_bullish_hammer_candle(open, high, low, close)
      
      if bullish_status:
         print(f'Bullish Matched {ticker}')
         bullish_tickers.append(ticker)
      if hammer_status:
         print(f'Hammer Matched {ticker}')
         hammer_tickers.append(ticker)
   
   return bullish_tickers, hammer_tickers, end1

# get_matched_tickers()
bullish_tickers, hammer_tickers, end1 = get_matched_tickers()
print(f'Bullish Tickers {bullish_tickers}')
print(f'Hammer Tickers {hammer_tickers}')
print(f'Completed in {time.time() - start_time - end1} seconds')  # Calculate the total execution time

