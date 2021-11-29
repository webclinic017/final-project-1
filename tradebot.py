import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
import time


domain = "https://paper-api.alpaca.markets"
Key_ID = "PKZJ2IUHPR22IWQBX83D"
SEC_Key = "du6vf2uoCvDlO3Re9uLPUtk0JfmrGm8KaTMuvisl"


api = tradeapi.REST(Key_ID, SEC_Key, domain) # connecting to the API

#Check if the market is open

clock = api.get_clock()
print('The market is {}'.format('open.' if clock.is_open else 'closed.'))


account = api.get_account()
positions = api.list_positions() # listing all the current position

#print(account.status)
print("available positions",positions)


# available buying power
print(f'${account.buying_power} is available as buying power.')

while True:
    print("")
    print("checking price")

    #Getting Data for the stock
    data_5min = api.get_barset('SPY', 'minute', limit=5) # using the last 5 trading days 5 min candlesticks

    data_21min = api.get_barset('SPY', 'minute', limit=21) # using this for the 21 moving averages 

    data_9min = api.get_barset('SPY', 'minute', limit=9) # using this for the 9 moving averages 


    bars = data_5min['SPY']

    #storing the data

    data5 = []
    for bar in data_5min["SPY"]:
        data5.append(bar.c)  # getting the closing data of the stock

    data5 = np.array(data5,dtype=np.float64) # convert the the list into numpy
    last_price = data5[-1] # getting the last closing price

    #making the 9 nad 21 moving averages

    # the 9 moving average
    data9 = []
    for bar in data_9min["SPY"]:
        data9.append(bar.c)  

    data21 = np.array(data9,dtype=np.float64) # convert the the list into numpy

    Ma_9 = pd.Series(data9)
    last_MA_9 = Ma_9.mean()
    print("the 9 moving average", last_MA_9)

    # the 21 moving average
    data21 = []
    for bar in data_21min["SPY"]:
        data21.append(bar.c)  

    data21 = np.array(data21,dtype=np.float64) # convert the the list into numpy

    Ma_21 = pd.Series(data21)
    last_MA_21 = Ma_21.mean()
    print("the 21 moving average", last_MA_21)



    print("Last Price: " + str(last_price))

    
    print(data5)







#Buy a stock in market price
"""api.submit_order(
    symbol = "SPY", # stock ticker symbol in capital case
    qty = 1, 
    side = "buy",
    type = "market",
    time_in_force = "gtc" # good till cancel 
)
#sell a stock in market price 
api.submit_order(
    symbol = "SPY", # stock ticker symbol in capital case
    qty = 1, 
    side = "sell",
    type = "market",
    time_in_force = "gtc" # good till cancel 
)"""