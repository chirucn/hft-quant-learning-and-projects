# order book levels
bid_price=100.00
ask_price= 100.05

bid_qty= 200
ask_qty= 50

bids=[(bid_price, bid_qty)]
asks=[(ask_price, ask_qty)]\

#mid-price and micro-price
mid_price=[(bid_price+ask_price)/2]
micro_price=[(bid_price*ask_qty + ask_price*bid_qty)/(bid_qty+ask_qty)]

# Imbalance Calculation
imbalance=(bid_qty - ask_qty)/(bid_qty + ask_qty)

# Signals Condtional Statements
if imbalance>0.2 and micro_price>mid_price:
    signal="BUY"
elif imbalance<-0.2 and micro_price<mid_price:
    signal="SELL"
else:
    signal="HOLD"

print("Mid-Price:", mid_price)  
print("Micro-Price:", micro_price)  
print("Imbalance:", imbalance)
print("Trading Signal:", signal)
