best_bid=100.00
best_ask=100.10

buy_price= best_bid
sell_price= best_ask

inventory = 0
cash = 0

# Simulate fills
inventory +=1
cash-=buy_price

inventory -=1
cash +=sell_price

print("Final Inventory:", inventory)
print("Final Cash P&L:", cash)


## Part 5    Inventory Aware Logic
inventory=5

if inventory>0:
    buy_price=best_bid-0.05
    sell_price=best_ask+0.01
else:
    buy_price=best_bid
    sell_price=best_ask

print("Inventory:", inventory)
print("Adjusted Buy Price:", buy_price)
print("Adjusted Sell Price:", sell_price)
