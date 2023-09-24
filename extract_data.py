import yfinance as yf
import time
from symbols import company_names_mappings
from main import is_bullish_candle, is_bullish_hammer_candle
from bearish import is_bearish_candle, is_bearish_hammer_candle


def get_symbol_data(ticker_symbol):
   try:
      # Download the stock data
      stock_data = yf.download(ticker_symbol, period="1wk")

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
bullish_stocks = []
bearish_stocks = []

# starts here
def trigger(company_names):
   for company in company_names:
      print(company)
      last_open, last_high, last_low, last_close = get_symbol_data(company+".NS")
      bullish_status = is_bullish_candle(last_open, last_high, last_low, last_close)
      hammer_status = is_bullish_hammer_candle(last_open, last_high, last_low, last_close)
      if bullish_status or hammer_status:
         print(f'Bullish Matched', {company})
         bullish_stocks.append(company)
      bearish_status = is_bearish_candle(last_open, last_high, last_low, last_close)
      shooting_status = is_bearish_hammer_candle(last_open, last_high, last_low, last_close)
      if bearish_status or shooting_status:
         print(f'Bearish Matched', {company})
         bearish_stocks.append(company)
     
   return bullish_stocks, bearish_stocks

trigger(company_names_mappings.values())
print(bearish_stocks)
print('------------')
print(bullish_stocks)
print("Completed...!!!")
