import requests
import json
import time

from requests.api import request


HEADERS = {"Accept": "application/json"}

def requestToUpbit(url:str, params:dict):
    return requests.request("GET", url, headers=HEADERS, params=querystring)

# url = "https://api.upbit.com/v1/market/all"

# querystring = {"isDetails":"true"}


# # 요청 1회
# response = requestToUpbit(url, querystring)

# # print(response.text)


# bitList = json.loads(response.text)
# # print(bitList)
# setBitList = []
# setBitList = [bit['english_name'] for bit in bitList if str(bit['market']).startswith('KRW')]
# print(len(setBitList))


# url = "https://api.upbit.com/v1/candles/days"

# querystring = {"market":"KRW-BTC","count":"1"}

# response = requestToUpbit(url, querystring)
# print(response.text)

# candle = json.loads(response.text)[0]

# print(candle)
# print('open : ', str(candle['opening_price']))
# print('trade_price : ', str(candle['trade_price']))
# # 초당 10회 / 분당 600 회


url = "https://api.upbit.com/v1/ticker"
headers = {"Accept": "application/json"}
querystring = {"markets":"KRW-BTC"}
response = requestToUpbit(url, querystring)
print(response.text)

