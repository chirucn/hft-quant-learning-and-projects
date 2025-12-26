# Challenge: Implement a trading strategy that combines RSI and Moving Average for mean reversion.
price= float(input("Enter the stock price:"))
moving_average= float(input("Enter the 50 day moving average:"))
RSI= float(input("Enter the RSI value (0-100):"))


if price< moving_average and RSI<30:
    print("Buy Signal: Price below moving average and RSI indicates oversold")
elif price> moving_average and RSI>70:
    print("Sell Signal: Price above moving average and RSI indicates overbought")
else:
    print("Hold Signal: No clear trading signal")