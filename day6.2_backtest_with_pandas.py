import pandas as pd

#Load historical data of nifty 50
df=pd.read_csv("nifty_50.csv")

#computation  of 50-day moving average
df["MA_50"]=df["Close"].rolling(window=50).mean()

#generate trading signals
df["Signal"]=0
df.loc[df["Close"]>df["MA_50"]*1.02, "Signal"]=-1  #Sell signal
df.loc[df["Close"]<df["MA_50"]*0.98, "Signal"]=1   #Buy signal

#Calculate daily returns and satrategy returns
df["Return"]=df["Close"].pct_change()
df["Strategy"]=df["Signal"].shift(1)*df["Return"]

#cumulative performance
df["Cumulative"]= (1 + df["Strategy"]).cumprod()

#print results
print(df[["Date", "Close", "MA_50", "Signal", "Cumulative"]].tail())


#plot performance
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Cumulative"], label="Strategy")
plt.title ("Simple Moving Average Strategy Backtest")
plt.xlabel("Date")
plt.ylabel("Cumulative Returns")
plt.legend()
plt.grid()
plt.show()
