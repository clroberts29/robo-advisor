import requests
import json
import datetime

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


# INFO INPUTS

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response = requests.get(request_url)
# print(type(response))
# print(response.status_code)
# print(response.text)

dict_response = json.loads(response.text)

last_refreshed = dict_response["Meta Data"]["3. Last Refreshed"]

dates = list(dict_response["Time Series (Daily)"].keys())

last_day = dates[0]

latest_close = dict_response["Time Series (Daily)"][last_day]["4. close"]
print(latest_close)

# INFO OUTPUTS

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
