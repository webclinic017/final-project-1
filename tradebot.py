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

print(account.status)
print("available positions",positions)


# available buying power
print(f'${account.buying_power} is available as buying power.')

#Getting Data for the stock
barset = api.get_barset('SPY', 'day', limit=5) # using the daily candle


bars = barset['SPY']
week_open = bars[0].o
print("open",week_open)
week_close = bars[0].c
print("close",week_close)
percent_change = (week_close - week_open) / week_open * 100
print(f'SPY moved {percent_change}% over the last 5 days')





















#Buy a stock in market price
"""api.submit_order(
    symbol = "SPY", # stock ticker symbol in capital
    qty = 1, 
    side = "buy",
    type = "market",
    time_in_force = "gtc" # good till cancel 
)
#sell a stock in market price 
api.submit_order(
    symbol = "SPY", # stock ticker symbol in capital
    qty = 1, 
    side = "sell",
    type = "market",
    time_in_force = "gtc" # good till cancel 
)"""