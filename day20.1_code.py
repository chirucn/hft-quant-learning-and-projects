# Simulated order book
best_bid = 100.00
best_ask = 100.10
bid_size = 100
ask_size = 50

# Previous mid
prev_mid = (best_bid + best_ask) / 2
# Current mid moves up (signal triggers BUY)
current_mid = 100.07

# Signal
if current_mid > prev_mid:
    signal = "BUY"
else:
    signal = "NO TRADE"

# Adverse selection simulation
# Suppose large orders arrive before you
filled_size = min(ask_size, 20)  # You try to buy 20, but only part fills
slippage = 0.05  # Price moves up before you fill

print("Signal:", signal)
print("Filled size:", filled_size)
print("Slippage:", slippage)
