import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#------------------------------
# 1. Load Data
# -----------------------------
df = pd.read_csv('nifty_50.csv')
df["Date"]= pd.to_datetime(df["Date"])

# -----------------------------
# 2. Strategy Logic (Golden Cross)
# -----------------------------
df["MA_20"]= df["Close"].rolling(window=20).mean()
df["MA_200"]= df["Close"].rolling(window=200).mean()

df["Signal"]=0
df.loc[df["MA_20"] > df["MA_200"], "Signal"]=-1   # Buy Signal
df.loc[df["MA_20"] < df["MA_200"], "Signal"]= -1  # Sell Signal

# -----------------------------
# 3. Returns
# -----------------------------
df["Mkt_Returns"]= df["Close"].pct_change()
df["Strategy_Returns"]= df["Signal"].shift(1)*df["Mkt_Returns"]

# -----------------------------
# 4. Cumulative Returns
# -----------------------------
df["Cum_Mkt_Returns"]= (1 + df["Mkt_Returns"]).cumprod()
df["Cum_Strategy_Returns"]= (1 + df["Strategy_Returns"]).cumprod()

# -----------------------------
# 5. Sharpe Ratio
# -----------------------------
sharpe_ratio= (df["Strategy_Returns"].mean()/ df["Strategy_Returns"].std())* np.sqrt(252)

# -----------------------------
# 6. Maximum Drawdown
# -----------------------------
rolling_max= df["Cum_Strategy_Returns"].cummax()    #Tracks highest equity so far
drawdown= (df["Cum_Strategy_Returns"]-rolling_max)/rolling_max     #Measures % fall from peak

max_drawdown= drawdown.min()   #Worst drawdown

# -----------------------------
# 7. CAGR
# -----------------------------
days=(df["Date"].iloc[-1]- df["Date"].iloc[0]).days
years= days/365.0

cagr= (df["Cum_Strategy_Returns"].iloc[-1])**(365.0/days)-1

# -----------------------------
# 8. Print Report
# -----------------------------
print("QUANT PERFORMANCE REPORT")
print("----------------------------")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
print(f"Max Drawdown: {max_drawdown:.2%}")
print(f"CAGR: {cagr:.2%}")

# -----------------------------
# 9. Plot Comparison
# -----------------------------
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Cum_Mkt_Returns'], label="Buy & Hold", alpha=0.7)
plt.plot(df['Date'], df['Cum_Strategy_Returns'], label="Golden Cross Strategy", linewidth=2)

plt.title("Strategy vs Buy & Hold")
plt.xlabel("Date")
plt.ylabel("Cumulative Returns")
plt.legend()
plt.grid(True)
plt.show()

