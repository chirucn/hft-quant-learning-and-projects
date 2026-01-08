
DAY 20 will cover:
•	Why this signal still loses money
•	Adverse selection (market maker’s nightmare)
•	When NOT to trade even with strong signals
•	Turning signals into rules
________________________________________
🔥 DAY 20 START QUESTION
Before I teach, answer this:
👉 If many traders see the same BUY signal, what happens to the price and your fill?
Think about:
•	queue position
•	slippage
•	adverse selection
Reply with your best guess — even if unsure.

If many traders see the same BUY signal:
•	Liquidity on the ask side gets consumed quickly
•	Slippage increases (you pay more than expected)
•	Your queue position is long, so you may get partially filled or not at all
This is called adverse selection — a core HFT risk.
________________________________________ 🔹 PART 1: ADVERSE SELECTION
🔑 CORE IDEA
Even a “perfect” signal can lose money if:
•	You arrive late in the queue
•	Price moves before your order fills
•	Spreads widen due to other participants
In HFT: execution > prediction
________________________________________
🔹 PART 2: RULES TO AVOID LOSSES
1.	Only trade when enough liquidity exists
2.	Avoid market orders in thin books
3.	Cancel and update orders fast if imbalance reverses
4.	Always track queue position
________________________________________
🧩 TODAY’S MINI TASK
Write 3 short rules in your notebook for “when NOT to trade” based on what you just learned.
Use your own words.
1.	When liquidity is low → don’t trade
2.	When queue position is too long → cancel or wait
3.	When micro-price/imbalance reverses quickly → don’t enter
 
PART 2: PYTHON SIMULATION OF ADVERSE SELECTION
We will simulate a “naive” signal and see how it can lose money if the market moves or queue is long.
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

👉 Why did we only fill part of the order and pay slippage?
	We only filled part of the order and paid slippage because faster traders consumed the available liquidity first, pushing the price up before our order could fully execute.
 
