from read_data import extract_column_data
from extract_data import trigger

csv_file_path = r'C:/Users/BTC - 0014/Documents/my repositories/bullish candle finder/Candle-Finder/data/fo.csv'
column2_data = extract_column_data(csv_file_path)
bullish_stocks, bearish_stocks = trigger(column2_data)
print("Completed...!!!")
print(f'Bullish FNO {bullish_stocks}')
print(f'Bearish FNO {bearish_stocks}')