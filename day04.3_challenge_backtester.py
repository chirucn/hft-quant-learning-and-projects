
price=100
cash=100000
shares=0

signals = ["BUY", "HOLD", "BUY", "SELL", "HOLD", "SELL"]

for signal in signals:
    if signal=="BUY" and cash >= price*10:
        cash-= price*10
        shares+=10
        print(f"BUY 10 shares | Cash:{cash}| Shares:{shares}")
    elif signal=="SELL" and shares >=10:
        cash+= price*10
        shares-=10
        print(f"SELL 10 shares | Cash:{cash}| Shares:{shares}")
    else:
        print(f"HOLD | Cash:{cash}| Shares:{shares}")
