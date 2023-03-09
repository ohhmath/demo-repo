
import pandas as pd

sp_500_tickers = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
sp_500_tickers = sp_500_tickers[0]
ticker_list = sp_500_tickers["Symbol"].values.tolist()


#print(ticker_list)

import datetime as dt 
import pandas as pd

import concurrent.futures as cf
from yahoofinancials import YahooFinancials

import re
import ast
import time
import requests
from bs4 import BeautifulSoup

#mathieu 