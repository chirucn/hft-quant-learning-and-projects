# Bids (price, quantity) – highest price first
bids=[
    (100.00, 120),
    (99.95, 80),
    (99.90, 200)
    ]

# Asks (price, quantity) – lowest price first
asks=[(100.09, 100),
      (100.10, 150),
      (100.15, 100)]


# Best Bid & Ask
best_bid=bids[0][0]
best_ask=asks[0][0]

#mid price=(best_bid+best_ask)/2
mid_price=(best_bid+best_ask)/2

#spread
spread=best_ask-best_bid

if spread<0.05:
    print("Tighter Spread - More Liquidity")
else:
    print("Wider Spread - (risky) Less Liquidity")