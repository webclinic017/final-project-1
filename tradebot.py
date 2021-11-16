import alpaca_trade_api as tradeapi
import numpy as np
import time


domain = "https://paper-api.alpaca.markets"
Key_ID = "PKZJ2IUHPR22IWQBX83D"
SEC_Key = "du6vf2uoCvDlO3Re9uLPUtk0JfmrGm8KaTMuvisl"


api = tradeapi.REST(Key_ID, SEC_Key, domain) # connecting to the API
account = api.get_account()
print(account.status)

#Buy a stock in market price
api.submit_order(
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
)