def is_bearish_candle(open_price, high_price, low_price, close_price):
    body_size = open_price - close_price
    upper_wick = high_price - max(open_price, close_price)
    lower_wick = min(open_price, close_price) - low_price
    
    is_full_red_body = body_size > 0 and open_price > close_price
    has_small_upper_wick = upper_wick <= abs(body_size) * 0.2  # Adjust the threshold as per your preference
    has_small_lower_wick = lower_wick <= abs(body_size) * 0.2  # Adjust the threshold as per your preference
    
    return is_full_red_body and has_small_upper_wick and has_small_lower_wick and close_price < 20

def is_bearish_hammer_candle(open_price, high_price, low_price, close_price):
    body_size = open_price - close_price
    upper_wick = high_price - max(open_price, close_price)
    lower_wick = min(open_price, close_price) - low_price
    
    is_full_red_body = body_size > 0 and open_price > close_price
    has_long_lower_wick = lower_wick >= abs(body_size) * 0.7  # Adjust the threshold as per your preference
    has_small_upper_wick = upper_wick <= abs(body_size) * 0.0  # Adjust the threshold as per your preference
    
    return is_full_red_body and has_long_lower_wick and has_small_upper_wick and close_price < 20
