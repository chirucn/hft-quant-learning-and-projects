# Create first dataframe
import pandas as pd
data = {
    "Date": ["2025-12-01", "2025-12-02", "2025-12-03", "2025-12-04"],
    "Price": [100, 102, 101, 105]
}

df= pd.DataFrame(data)
print(df)


#Read real CSV file into dataframe
import yfinance as yf 
nifty = yf.download("^NSEI", start="2020-01-01", end="2025-12-01")
nifty.to_csv("nifty50.csv")

print("Downloaded!")

df1= pd.read_csv("nifty_50.csv")
print(df1.head())

#Compute moving averages
df1["MA_50"]=df1["Close"].rolling(window=50).mean()
print(df1[["Date","Close","MA_50"]].head(10))
df1.head(60)