import requests
import json
import datetime
import os
import csv
from dotenv import load_dotenv

load_dotenv()


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


# INFO INPUTS

validation = ""

while validation != "validated":
    
    symbol = (input("Please enter a valid stock ticker."))
    d=0
    for c in symbol:
        if c.isdigit():
                d = d + 1

    if len(symbol) <= 4 and d == 0:
        validation = "validated"
    else:
        if len(symbol) > 4:
            print("Invalid entry, too many characters. Please try again.")
        else:
            print("Invalid entry, symbol contains digits. Please try again.")
        
    #    if user_input in id_list:
    #        receipt_list.append(user_input)
    #        print(receipt_list)
    #    else:
    #        if isinstance(user_input, int):




# Initial validation of input

api_key = os.environ.get("api_key")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

response = requests.get(request_url)
# print(type(response))
# print(response.status_code)
# print(response.text)

dict_response = json.loads(response.text)

last_refreshed = dict_response["Meta Data"]["3. Last Refreshed"]

tsd = dict_response["Time Series (Daily)"]

dates = list(tsd.keys())

last_day = dates[0]

latest_close = tsd[last_day]["4. close"]

high_prices = []
high_price = ""
low_prices = []
low_price = ""


for p in dates:
    high_price = tsd[p]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[p]["3. low"]
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)




# INFO OUTPUTS

csv_file_path = "data\prices.csv"

#csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()
    for date in dates:
        writer.writerow({
            "timestamp": date,
            "open": tsd[date]["1. open"],
            "high": tsd[date]["2. high"],
            "low": tsd[date]["3. low"],
            "close": tsd[date]["4. close"],
            "volume": tsd[date]["5. volume"]        
        })



print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

