import alpaca_trade_api as tradeapi
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
    barset = api.get_barset('SPY', 'minute', limit=30) # using the last 5 trading days 30 min candlesticks
    bars = barset['SPY']

    week_open = bars[-1].o
    #print("open",week_open)
    week_close = bars[-1].c
    #print("close",week_close)

    percent_change = (week_close - week_open) / week_open * 100
    #print(f'SPY moved {percent_change}% over the last 5 days')


    #storing the data

    data = []
    for bar in barset["SPY"]:
        data.append(bar.c)  # getting the closing data of the stock

    data = np.array(data,dtype=np.float64) # convert the the list into numpy
    Ma = np.mean(data) # moving average
    last_price = data[-1] # the last closing price

    print("Moving Average: " + str(Ma))
    print("Last Price: " + str(last_price))







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