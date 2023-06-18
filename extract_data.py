import yfinance as yf
import time
from symbols import company_names_mappings
from main import is_bullish_candle


def get_symbol_data(ticker_symbol):
   try:
      # Download the stock data
      stock_data = yf.download(ticker_symbol, period="1d")

      # Get the last OHLC prices
      last_open_price = stock_data["Open"].iloc[-1]
      last_high_price = stock_data["High"].iloc[-1]
      last_low_price = stock_data["Low"].iloc[-1]
      last_close_price = stock_data["Close"].iloc[-1]

      return round(last_open_price, 2), round(last_high_price, 2), round(last_low_price, 2), round(last_close_price, 2)


   except IndexError:
      print(f"No data available for symbol: {ticker_symbol}")
      return 0,0,0,0
   except Exception as e:
      print(f"An error occurred: {e}")
      return 0,0,0,0


start_time = time.time()
bullish_list = []
for company in company_names_mappings.values():
   print(company)
   last_open, last_high, last_low, last_close = get_symbol_data(company+".NS")
   status = is_bullish_candle(last_open, last_high, last_low, last_close)
   if status:
      print(f'Matched', {company})
      bullish_list.append(company)

print("Completed...!!!")
print(bullish_list)