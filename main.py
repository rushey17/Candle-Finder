#bullish candle
def is_bullish_candle(open_price, high_price, low_price, close_price):
   body_size = close_price - open_price
   upper_wick = high_price - max(open_price, close_price)
   lower_wick = min(open_price, close_price) - low_price
    
   is_full_green_body = body_size > 0 and close_price > open_price
   has_small_upper_wick = upper_wick <= body_size * 0.2  # Adjust the threshold as per your preference
   has_small_lower_wick = lower_wick <= body_size * 0.2  # Adjust the threshold as per your preference
    
    
   return is_full_green_body and has_small_upper_wick and has_small_lower_wick and close_price > 90

# hammer candles,
def is_bullish_hammer_candle(open_price, high_price, low_price, close_price):
    body_size = close_price - open_price
    upper_wick = high_price - max(open_price, close_price)
    lower_wick = min(open_price, close_price) - low_price
    
    is_full_green_body = body_size > 0 and close_price > open_price
    has_long_lower_wick = lower_wick >= body_size * 0.7  # Adjust the threshold as per your preference
    has_small_upper_wick = upper_wick <= body_size * 0.3  # Adjust the threshold as per your preference
    
    return is_full_green_body and has_long_lower_wick and has_small_upper_wick and close_price > 90
