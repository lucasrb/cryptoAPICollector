# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 17:44:13 2018

@author: lucas.ribeiro
"""
import xlwt

from binance.client import Client
clientBinance = Client("api_key", "api_secret")

from kucoin.client import Client
client = Client("api_key", "api_secret")

from allcoin.client import Client
clientAllcoin = Client("api_key", "api_secret")

# fetch 1 minute klines for the last day up until now
klines = client.get_historical_klines_tv("BTC-USDT", Client.RESOLUTION_5MINUTES, "1 day ago UTC")

# fetch 1 minute klines for the last day up until now
klinesBinance = clientBinance.get_historical_klines("BTCUSDT", Client.RESOLUTION_5MINUTES, "1 day ago UTC")

# get symbol klines
klinesAllcoin = clientAllcoin.get_klines('eth_btc', '1day')

print (klinesBinance)


    
    
from tempfile import TemporaryFile
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

i = 0
j = 0
for list in klines:
    for double in list:
        sheet1.write(i, j, double)
        if j in (0, 1, 2, 3, 4):
            j = j + 1
        else:
            j = 0;
            i = i + 1




name = "random.xls"
book.save(name)
book.save(TemporaryFile())