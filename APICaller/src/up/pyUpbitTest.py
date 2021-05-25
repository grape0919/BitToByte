import requests
import json
import time

from requests.api import request

from APICaller.src.up.data.realTimeData import tickerEntry

HEADERS = {"Accept": "application/json"}

def requestToUpbit(url:str, params:dict):
    response = requests.request("GET", url, headers=HEADERS, params=params)
    time.sleep(0.1)
    return response

def getCoinList():
    url = "https://api.upbit.com/v1/market/all"

    querystring = {"isDetails":"true"}


    # 요청 1회
    response = requestToUpbit(url, querystring)

    # print(response.text)


    bitList = json.loads(response.text)
    # print(bitList)
    setBitList = []
    setBitList = [bit['market'] for bit in bitList if str(bit['market']).startswith('KRW')]
    strBitList = ','.join(setBitList)
    # print(len(setBitList))

    return strBitList


def ticker(strBitList):
    
    url = "https://api.upbit.com/v1/ticker"
    querystring = {"markets":strBitList}
    response = requestToUpbit(url, querystring)

    data = json.loads(response.text)
    # print("!@#!@# data : ", data)

    entry = tickerEntry()

    attribute = dir(entry)
    # print(attribute)
    
    entryList = []
    for bit in data:
        entry = tickerEntry()
        for att in attribute:
            setattr(entry,att,bit[att])

        entryList.append(entry._getItems_())
    
    return entryList

def tickerAll():
    return ticker(getCoinList())