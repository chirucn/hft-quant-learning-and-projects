best_bid= 100
best_ask= 100.10

mid_price=(best_bid + best_ask)/2

print("Best Bid:", best_bid)
print("Best Ask:", best_ask)
print("Mid Price:", mid_price)



prev_mid=100.00
current_mid= 100.10
if current_mid> prev_mid:
    print("BUY signal")
elif current_mid< prev_mid:
    print("SELL signal")
else:
    print("NO TRADE")