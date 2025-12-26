import pandas as pd
import matplotlib.pyplot as plt

#Load historical data of nifty 50
df=pd.read_csv("nifty_50.csv")

#convert 'Date' column to datetime format
df["Date"]=pd.to_datetime(df["Date"])

#Calculation of 20 day and 200 day moving averages
df["MA_20"]=df["Close"].rolling(window=20).mean()
df["MA_200"]=df["Close"].rolling(window=200).mean()

#Generate trading 
df["Signal"]=0
df.loc[df["MA_20"]>df["MA_200"], "Signal"]=1  #Buy signal
df.loc[df["MA_20"]<df["MA_200"], "Signal"]=-1  #Sell signal

# Detect Actual Golden Cross and Death Cross points
df["Position"]=df["Signal"].diff()

# -----------------------------
# 4. Plot Price + Moving Averages
# -----------------------------

plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["Close"], label="Close Price", alpha=0.5)    #alpha is trasparency of line
plt.plot(df["Date"], df["MA_20"], label="20-Day MA", color="green")
plt.plot(df["Date"], df["MA_200"], label="200-Day MA", color="red")

#Plot BUY Points
plt.scatter(df[df["Position"]==2]["Date"],
         df[df["Position"]==2]["Close"],
         marker="^",
         color="green",
         s=100,
         label="BUY")

#Plot SELL Points
plt.scatter(df[df["Position"]==-2]["Date"],
         df[df["Position"]==-2]["Close"],
         marker="v",
         color="red",
         s=100,
         label="SELL")


plt.title("Golden Cross Strategy(MA20 vs MA200)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()