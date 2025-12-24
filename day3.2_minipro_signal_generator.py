# Mini Project: Trading Signal Generator Based on Moving Average

price=float(input("Enter the stock price:"))
moving_average= float(input("Enter the 50 day moving average:"))
                      
if price> moving_average*1.02:
    print("Sell Signal: Price is above moving average by more than 2%")
elif price< moving_average*0.98:
    print("Buy Signal: Price is below moving average by more than 2%")
else:
    print("Hold Signal: Price near moving average")