bid= [(100.00, 500)]
ask= [(100.10, 220)]

best_bid=bid[0][0]
best_ask=ask[0][0]

bid_size= bid[0][1]
ask_size= ask[0][1]

imbalance= (bid_size-ask_size)/(bid_size+ask_size)

micro_price= (best_bid*ask_size + best_ask*bid_size)/(bid_size+ask_size)

mid_price = (best_bid + best_ask) / 2

print("Imbalance:", imbalance)
print("Mid Price:", mid_price)
print("Micro Price:", micro_price)


if micro_price > mid_price and imbalance> 0.2:
    print("BUY")
elif micro_price < mid_price and imbalance< -0.2:
    print("SELL")
else:
    print("NO TRADE")