#Backtest of signal of list of prices

prices= [100,102,105,98,90,110,115]
moving_average= 100

for price in prices:
    if price> moving_average*1.02:
        print(price,"--> Sell signal")
    elif price< moving_average*0.98:
        print(price,"--> Buy signal")
    else:
        print(price,"--> Hold")

