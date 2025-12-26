# Best Bid and Ask
bid_price=100.00
ask_price=100.05

bid_qty=200
ask_qty=500

# Mid Price
mid_price=(bid_price + ask_price)/2

# Micro price
micro_price= (bid_price*ask_qty + ask_price*bid_qty)/(bid_qty + ask_qty)

print("Bid Volume:", bid_qty)
print("Ask Volume:", ask_qty)
print("Mid Price:", mid_price)
print("Micro Price:", micro_price)