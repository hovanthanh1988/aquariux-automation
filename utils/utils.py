import json

def load_test_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def modify_notification_data(file_path, symbol, order_type, entry_price = 0, size =0, sl = 0, tp = 0):
    with open(file_path, 'r') as file:
        data = json.load(file)
    sl_formatted = "{:,.1f}".format(float(sl))
    tp_formatted = "{:,.1f}".format(float(tp))
    entry_price_formatted = "{:,.1f}".format(float(entry_price))
    # Update the BUY and SELL notifications dynamically
    if order_type == "market":
        data["market"]['BUY'] = f"{symbol} - BUY ORDER placed, Size: {size} / Units: {size}. Stop Loss: {sl_formatted}. Take Profit: {tp_formatted}."
        data["market"]['SELL'] = f"{symbol} - SELL ORDER placed, Size: {size} / Units: {size}. Stop Loss: {sl_formatted}. Take Profit: {tp_formatted}."
    elif order_type == "edit_open_position":
        data["edit_open_position"]['BUY'] = f"{symbol} - BUY ORDER updated, Size: {size} / Units: {size}. Entry Price: {entry_price_formatted}. Stop Loss: {sl_formatted}. Take Profit: {tp_formatted}."
        data["edit_open_position"]['SELL'] = f"{symbol} - SELL ORDER updated, Size: {size} / Units: {size}. Entry Price: {entry_price_formatted}. Stop Loss: {sl_formatted}. Take Profit: {tp_formatted}."
    elif order_type == "Limit":
        data["Limit"]['BUY'] = f"{symbol} - BUY LIMIT ORDER placed, Size: {size} / Units: {size}. Price: {entry_price_formatted}. Stop Loss: {sl_formatted}. Take Profit: {tp_formatted}."
        data["Limit"]['SELL'] = f"{symbol} - SELL LIMIT ORDER placed, Size: {size} / Units: {size}. Price: {entry_price_formatted}. Stop Loss: {sl_formatted}. Take Profit: {tp_formatted}."
    elif order_type == "Stop":
        data["Stop"]['BUY'] = f"{symbol} - BUY STOP ORDER placed, Size: {size} / Units: {size}. Price: {entry_price_formatted}. Stop Loss: {sl_formatted}. Take Profit: {tp_formatted}."
        data["Stop"]['SELL'] = f"{symbol} - SELL STOP ORDER placed, Size: {size} / Units: {size}. Price: {entry_price_formatted}. Stop Loss: {sl_formatted}. Take Profit: {tp_formatted}."
    return data