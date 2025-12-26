# -----------------------------
# Order Book
# -----------------------------
bids = [(100.00, 120), (99.95, 80)]
asks = [(100.05, 50), (100.10, 60)]

# Markert Buy Order
mkt_buy_size=65

price, qty= asks[0]

if mkt_buy_size<= qty:
    asks[0]=(price, qty - mkt_buy_size)
else:
    asks.pop(0)

print("Updated Asks:", asks)