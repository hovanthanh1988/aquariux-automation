import json

def load_test_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def modify_notification_data(file_path, symbol, size, sl, tp):
    with open(file_path, 'r') as file:
        data = json.load(file)
    sl_formatted = "{:,.1f}".format(float(sl))
    tp_formatted = "{:,.1f}".format(float(tp))
    # Update the BUY and SELL notifications dynamically
    data['market']['BUY'] = f"{symbol} - BUY ORDER placed, Size: {size} / Units: {size}. Stop Loss: {sl_formatted}. Take Profit: {tp_formatted}."
    data['market']['SELL'] = f"{symbol} - SELL ORDER placed, Size: {size} / Units: {size}. Stop Loss: {sl_formatted}. Take Profit: {tp_formatted}."

    return data