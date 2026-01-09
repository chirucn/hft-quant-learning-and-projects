DAY 22 — BUILDING A MINI MARKET-MAKING ENGINE (CORE)
Today you will build structure, not just ideas.
________________________________________
🎯 DAY 22 GOAL
By the end of today, you will have:
•	A looped market-making engine
•	Dynamic quoting
•	Inventory limits
•	Real P&L tracking
This becomes a GitHub project.
________________________________________
🔹 PART 1 — ENGINE MENTAL MODEL
Every market-making engine repeats this loop:
1. Observe market
2. Decide quotes
3. Place orders
4. Get fills
5. Update inventory & cash
6. Manage risk
7. Repeat
This loop runs thousands of times per second in real HFT.
________________________________________
🔹 PART 2 — BASIC ENGINE SKELETON (PYTHON)
TYPE THIS CODE (DON’T SKIP)
# Initial state
best_bid = 100.00
best_ask = 100.10	

inventory = 0
cash = 0

inventory_limit = 5
spread = 0.10
This defines your state.
________________________________________
🔹 PART 3 — QUOTING LOGIC
Market maker quotes around mid, adjusted for inventory.
mid_price = (best_bid + best_ask) / 2

if inventory > 0:
    bid_quote = mid_price - spread
    ask_quote = mid_price + spread + 0.02
elif inventory < 0:
    bid_quote = mid_price - spread - 0.02
    ask_quote = mid_price + spread
else:
    bid_quote = mid_price - spread
    ask_quote = mid_price + spread
________________________________________
🔹 PART 4 — SIMULATED FILLS
We fake fills using simple logic:
# Simulate fills
if bid_quote >= best_bid and inventory < inventory_limit:
    inventory += 1
    cash -= bid_quote

if ask_quote <= best_ask and inventory > -inventory_limit:
    inventory -= 1
    cash += ask_quote
________________________________________
🔹 PART 5 — PRINT STATE
print("Inventory:", inventory)
print("Cash:", cash)
print("Bid Quote:", bid_quote)
print("Ask Quote:", ask_quote)
________________________________________
👉 Why do we impose an inventory limit in market making?
	To manage the inventory risk
“Inventory limits are imposed to control directional exposure, mitigate adverse selection, and ensure the market maker remains neutral rather than becoming a directional trader. They protect against liquidity shocks and tail risk”

👉 Why is micro-price better than mid-price in low-liquidity markets?
	Because the mid price assumes a symmetric 50–50 market, while real markets are asymmetric.
Micro-price incorporates liquidity-weighted information from the order book, allowing us to detect true directional pressure rather than a mathematical average.

	
👉 Why do we raise the ask when inventory is long?
	Because when we are long, we must reduce inventory risk by discouraging further buys (lower bid) and encouraging profitable sells (higher ask), using quote skewing to rebalance inventory while earning spread.
________________________________________
🟦 PART 6: MARKET-MAKING ENGINE LOOP
This is where everything you learned so far comes together and starts behaving like a real trading engine.
We will not jump to code immediately. First, understand the flow.
________________________________________

🧠 WHAT IS PART 6?
Part 6 answers:
How does a market maker operate continuously, tick after tick?
A market maker is not:
•	Buy once
•	Sell once
•	Done ❌
A market maker is a looping engine:
•	Observe market
•	Quote prices
•	Get filled
•	Update inventory & cash
•	Repeat
________________________________________
🔁 THE CORE LOOP (MENTAL MODEL)
Every market-making strategy follows this exact cycle:
Market Data → Decision → Quotes → Fills → Risk Update → Repeat
Let’s break this slowly.
________________________________________
🔹 STEP 1: READ MARKET DATA
From the order book you get:
•	Best Bid
•	Best Ask
•	Bid Size
•	Ask Size
From this you compute:
•	Mid Price (reference)
•	Imbalance (liquidity pressure)
•	Micro Price (true directional price)
📌 No trading decision yet — only observation.
________________________________________
🔹 STEP 2: DETERMINE DIRECTIONAL BIAS
Using:
•	Imbalance
•	Micro-price vs Mid-price
You infer:
•	Buyers stronger?
•	Sellers stronger?
•	Neutral?
This affects:
•	Aggressiveness
•	Quote skew
•	Fill probability
⚠️ Market makers do not predict far into the future — they react to current pressure.
________________________________________


🔹 STEP 3: ADJUST QUOTES (YOU ALREADY MASTERED THIS)
Inputs:
•	Mid price
•	Spread
•	Inventory
•	Liquidity conditions
Outputs:
•	Bid Quote
•	Ask Quote
You already know:
•	Long → lower bid, higher ask
•	Short → higher bid, lower ask
•	Flat → symmetric quotes
This is risk control, not alpha.
________________________________________
🔹 STEP 4: SIMULATE / RECEIVE FILLS
Two possible events:
•	Someone hits your bid → you buy
•	Someone lifts your ask → you sell
Key concepts:
•	Queue position
•	Liquidity
•	Slippage
•	Speed
Example:
•	Low liquidity → higher slippage
•	Long queue → worse fills
📌 You don’t always get filled.
________________________________________
🔹 STEP 5: UPDATE STATE (MOST IMPORTANT)
After every fill:
Inventory
inventory += buy_qty
inventory -= sell_qty
Cash
cash -= buy_price * qty
cash += sell_price * qty
This is where:
•	Risk accumulates
•	P&L is born
________________________________________
🔹 STEP 6: RISK CHECKS (HFT SURVIVAL RULE)
Before next iteration, you must check:
•	Max inventory limit
•	Max drawdown
•	Volatility spike
•	Spread widening
If violated:
•	Widen spreads
•	Stop quoting one side
•	Or exit market
⚠️ Most HFT blow-ups happen here.
________________________________________
🔁 STEP 7: LOOP AGAIN
The engine runs:
•	Every tick
•	Every millisecond
•	All day
No emotions. No opinions.
________________________________________
🧠 WHY THIS LOOP IS CRITICAL
Because profit does not come from one trade.
It comes from:
•	Thousands of small trades
•	Tight spreads
•	Controlled inventory
•	Superior execution
________________________________________
🔥 REAL HFT INSIGHT
Market making is not about being right — it’s about surviving while being fast.
________________________________________
👉 What is the single most dangerous thing if we forget to update inventory inside the loop?
If inventory is not updated inside the loop:
1️.  Inventory Risk Piles Up
•	You keep quoting as if you’re flat
•	In reality, you may already be heavily long or short
•	Risk becomes invisible
________________________________________
2️. Spike = Instant Loss
When volatility increases:
•	Price jumps multiple ticks
•	Your untracked inventory is marked-to-market
•	Loss appears before you can react
📌 This is how market makers blow up in seconds
________________________________________
3️. Spread Widens Against You
Because:
•	You’re forced to unwind inventory
•	Liquidity thins out
•	Slippage increases
•	You cross the spread to exit
➡️ Negative convexity
Losses accelerate faster than profits.
________________________________________
4️. Price Moves Extremes
Since:
•	You didn’t skew quotes
•	You didn’t slow one side
•	You kept feeding the same direction
This creates:
•	Adverse selection
•	Toxic flow
•	Guaranteed loss
________________________________________
🔥 THIS IS THE CORE HFT TRUTH
Inventory is the enemy. Spread is the shield. Speed is the weapon.
________________________________________
🟦 DAY 22 — PART 6
🧠 MARKET-MAKING ENGINE (FULL LOOP CODE)
Now we code everything you learned.
🎯 Goal
Simulate:
•	Continuous market making
•	Inventory-aware quoting
•	P&L tracking
________________________________________
🧪 SIMPLE MARKET ENGINE (EDUCATIONAL)
import numpy as np

# Initial state
inventory = 0
cash = 0.0
max_inventory = 10
spread = 0.10

# Simulated market data
best_bid = 100.00
best_ask = 100.10
bid_size = 120
ask_size = 80

for tick in range(20):

    # 1. Compute prices
    mid_price = (best_bid + best_ask) / 2
    imbalance = (bid_size - ask_size) / (bid_size + ask_size)

    micro_price = (
        best_bid * ask_size + best_ask * bid_size
    ) / (bid_size + ask_size)

    # 2. Inventory skew
    inventory_skew = inventory * 0.01

    bid_quote = micro_price - spread / 2 - inventory_skew
    ask_quote = micro_price + spread / 2 + inventory_skew

    # 3. Simulated fills
    if np.random.rand() > 0.5 and inventory < max_inventory:
        inventory += 1
        cash -= bid_quote
        print(f"Tick {tick}: BUY @ {bid_quote:.2f}")

    if np.random.rand() > 0.5 and inventory > -max_inventory:
        inventory -= 1
        cash += ask_quote
        print(f"Tick {tick}: SELL @ {ask_quote:.2f}")

    # 4. Mark-to-market P&L
    pnl = cash + inventory * mid_price

    print(
        f"Inventory: {inventory}, Cash: {cash:.2f}, P&L: {pnl:.2f}"
    )
    print("-" * 40)
________________________________________
🧠 WHAT THIS CODE TEACHES YOU
✔ Continuous loop
✔ Inventory-aware quoting
✔ Spread capture
✔ Mark-to-market P&L
✔ Risk control via limits
This is the DNA of real HFT systems.
________________________________________
👉 Final question before Day 23:
Why do HFT market makers prefer MANY small profits instead of a few big trades?
HFT market makers prefer many small profits because they focus on execution efficiency, spread capture, and risk control — not price prediction.
More precisely:
•	Prediction increases exposure time
•	Exposure time increases inventory risk
•	Small, fast trades reduce variance of P&L
•	Speed + repetition = statistical edge
📌 HFT = engineering, not forecasting.
