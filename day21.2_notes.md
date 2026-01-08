DAY 21 — MARKET MAKING (THE CORE OF REAL HFT)
This is where real money is made.
________________________________________
🎯 DAY 21 GOAL
You will understand:
•	Maker vs taker
•	Passive vs aggressive orders
•	How market makers earn spread
•	Why market making survives latency
________________________________________
🔹 PART 1 — MAKER vs TAKER (CRITICAL)
🟢 Maker
•	Places limit orders
•	Adds liquidity
•	Gets filled when someone hits your quote
•	Earns spread
•	Lower fees / rebates
🔴 Taker
•	Places market orders
•	Removes liquidity
•	Pays spread
•	Pays higher fees
•	High slippage risk
📌 HFT prefers maker, not taker.
________________________________________
🔹 PART 2 — PASSIVE vs AGGRESSIVE
Type	Order	Result
Passive	Limit	Waits for fill
Aggressive	Market	Instant fill
Market makers:
•	Quote bid & ask
•	Cancel fast if risk rises
•	Never chase price
________________________________________
🔹 PART 3 — BASIC MARKET MAKING LOGIC
Place:
•	BUY at best_bid
•	SELL at best_ask
If both fill → you earn the spread.
________________________________________
🧠 BUT THERE IS RISK
•	Inventory builds up
•	Price moves against you
•	Adverse selection
So, market makers must:
•	Control inventory
•	Adjust quotes dynamically
________________________________________
🧩 PART 4 — PYTHON: FIRST MARKET MAKER SIMULATION
TYPE & RUN THIS
best_bid = 100.00
best_ask = 100.10

buy_price = best_bid
sell_price = best_ask

inventory = 0
cash = 0

# Simulate fills
inventory += 1
cash -= buy_price

inventory -= 1
cash += sell_price

print("Final Inventory:", inventory)
print("Final Cash P&L:", cash)
________________________________________
👉 Why did this strategy make money even without predicting direction?
	This strategy made money because it earned the bid–ask spread by providing liquidity, not by predicting direction. Profit came from execution and spread capture, not price forecasts.
________________________________________PART 5: INVENTORY RISK (THE REAL DANGER)
Now you see why market making is hard.
________________________________________
🧠 WHAT IS INVENTORY RISK?
Inventory = positions you are holding.
Example:
•	You keep buying
•	Sells don’t fill
•	Inventory builds
•	Price moves against you → loss
Market makers do not want large inventory.
________________________________________
🔑 HOW MARKET MAKERS CONTROL INVENTORY
1️. Skew quotes
•	If long → lower your bid, raise your ask
•	Encourage selling, discourage buying
2️. Stop quoting one side
•	Temporarily stop buying or selling
3️. Widen spread
•	Reduce fill probability during risk
________________________________________
🧩 PYTHON: INVENTORY-AWARE LOGIC
TYPE & RUN
inventory = 5  # long inventory
best_bid = 100.00
best_ask = 100.10

if inventory > 0:
    buy_price = best_bid - 0.05
    sell_price = best_ask + 0.01
else:
    buy_price = best_bid
    sell_price = best_ask

print("Inventory:", inventory)
