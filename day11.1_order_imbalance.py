# Order book levels
bids = [(100.00, 120), (99.95, 80), (99.90, 200)]
asks = [(100.05, 100), (100.10, 60), (100.15, 90)]

# Total Volume at Best Bid and Ask
bid_volume= sum(qty for price, qty in bids)
ask_volume= sum(qty for price, qty in asks) 

# Order Book Imbalance
imbalance= (bid_volume - ask_volume) / (bid_volume + ask_volume)

print("Bid Volume:", bid_volume)
print("Ask Volume:", ask_volume)
print("Order Book Imbalance:", round(imbalance, 3))