import numpy as np

# Initial State
inventory=0
cash=0.0
max_inventory=10
spread=0.10

# Simulated Markert Data
best_bid=100.00
best_ask=100.10
bid_size=120
ask_size=80

for tick in range(20):

    # 1.Compute Prices
    mid_price=(best_bid+best_ask)/2
    imbalance=(bid_size-ask_size)/(bid_size+ask_size)
    micro_price=(best_bid*ask_size+best_ask*bid_size)/(bid_size+ask_size)

    # 2.Inventory Skew
    inventory_skew=inventory*0.01

    bid_quote= micro_price-(spread/2)-inventory_skew
    ask_quote= micro_price+(spread/2)+inventory_skew

    # 3.Simulated Fills
    if np.random.rand()>0.5 and inventory<max_inventory:
        inventory+=1
        cash-=bid_quote
        print(f"Tick {tick}: Bought at {bid_quote:.2f}, Inventory: {inventory}, Cash: {cash:.2f}")
    
    if np.random.rand()>0.5 and inventory> -max_inventory:
        inventory-=1
        cash+=ask_quote
        print(f"Tick {tick}: Sold at {ask_quote:.2f}, Inventory: {inventory}, Cash: {cash:.2f}")
    
    # M2M P&L Calculation
    pnl=cash+(inventory*mid_price)

    print(f"Tick {tick}: Mid Price: {mid_price:.2f}, Inventory: {inventory}, Cash: {cash:.2f}, P&L: {pnl:.2f}\n")

    print("-"*40)
