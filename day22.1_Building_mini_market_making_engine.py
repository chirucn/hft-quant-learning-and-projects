#PART-2: Basic Engine Skeleton
best_bid=100.00
best_ask=100.10

inventory=0
cash=0

inventory_limit=5
spread=0.10

#PART-3: Quotation Logic
mid_price=(best_bid+best_bid)/2

if inventory > 0:
    bid_quote=mid_price-spread
    ask_quote=mid_price+spread+0.02
elif inventory < 0:
    bid_quote=mid_price-spread-0.02
    ask_quote=mid_price+spread
else:
    bid_quote=mid_price-spread
    ask_quote=mid_price+spread

#PART-4: Simulated Fills
if bid_quote>=best_bid and inventory<inventory_limit:
    inventory+=1
    cash-=bid_quote

if ask_quote<=best_ask and inventory< -inventory_limit:
    inventory-=1
    cash+=ask_quote


#PART-5: Print State
print("Inventory:", inventory)
print("Cash:", cash)
print("Bid-Quote:", bid_quote)
print("Ask-Quote:", ask_quote)
