### PART - I ###

🔹 STEP 1 — What is a variable?
    A variable is a named box that stores a value.
    Example:
        x = 10
    x → name of the box
    = → assignment (put value into box)
    10 → value stored
📌 In trading terms:
    A variable is like memory for prices, volume, cash, etc.

🔹 STEP 2 — What is a list?
    A list stores multiple values in order.
        prices = [100, 100.1, 100.05, 100.2, 100.15]
    Think of it as:
    index:   0     1       2        3       4
    price: 100  100.1   100.05   100.2   100.15

📌 Why lists matter in trading:
    Price over time
    Tick data
    Order book levels

🔹 STEP 3 — What is a for loop?
    A loop means:
        “Do the same thing for each value in the list”
    for p in prices:
    print(p)

    This means:
        Take first price → store in p
        Print it
        Move to next price
        Repeat until list ends
    🧠 IMPORTANT:
        p is temporary
        It changes every iteration

🔹 STEP 4 — What is an if condition?
    An if checks a rule.
        if p > 100.1:
    This asks:
    Is the current price greater than 100.1?
    If YES → do one thing
    If NO → do something else

🔹 STEP 5 — FULL CODE (READ LINE BY LINE)
prices = [100, 100.1, 100.05, 100.2, 100.15]

for p in prices:
    if p > 100.1:
        print("Price moved up:", p)
    else:
        print("No strong move:", p)

What happens:
Python takes first price → p = 100
Checks 100 > 100.1 → ❌ False
Prints: No strong move: 100
Repeats for each price


Why do we need a loop instead of checking prices one by one?
    We use a loop to automatically repeat the same action over many prices instead of writing the logic again and again.


### PART - II ###

1️⃣ Bid, Ask, Spread (Quick Lock-In)

Bid → highest price buyers are willing to pay
Ask → lowest price sellers are willing to sell
Spread = Ask − Bid

📌 Tight spread = high liquidity
📌 Wide spread = low liquidity

2️⃣ Why Trades Happen at Bid or Ask

Market buy → hits the ask
Market sell → hits the bid

Trades don’t happen at mid-price unless liquidity magically appears.

3️⃣ Mid Price (Fair Reference)
mid = (best_bid + best_ask) / 2

Used for:
Fair value estimation
Risk measurement
Not execution

4️⃣ Why Market Orders Are Dangerous (HFT View)

Market orders:
Cross the spread
Cause slippage
Reveal urgency
Lose queue priority

HFT avoids them unless forced.


👉 Why liquidity and tight spread are critical for HFT / market making?
    Liquidity allows large trades without moving the price
    Tight spread reduces transaction (execution) cost
    High liquidity improves fill probability of limit orders
    Tight spread makes market making profitable and safer
    Low liquidity increases slippage and adverse selection risk