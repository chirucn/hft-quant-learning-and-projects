🎯 DAY 19 GOAL
You will:
•	Simulate bid & ask sizes
•	Calculate order book imbalance
•	Calculate micro price
•	See how this gives a directional edge
________________________________________
🔹 PART 1 — BID & ASK SIZES (CONCEPT)
At top of book, you have:
•	Best Bid Price + Bid Size
•	Best Ask Price + Ask Size
Example:
Bid: 100.00 | Size: 500
Ask: 100.10 | Size: 200
🧠 Interpretation:
•	More buyers waiting than sellers
•	Ask side is thinner → price more likely to move up
________________________________________
📐 ORDER BOOK IMBALANCE FORMULA
imbalance = (bid_size - ask_size) / (bid_size + ask_size)
Range:
•	+1 → all buying pressure
•	-1 → all selling pressure
•	 0 → balanced
________________________________________
🔹 PART 2 — MICRO PRICE (IMPORTANT)
Instead of simple mid:
micro_price = (best_bid * ask_size + best_ask * bid_size) / (bid_size + ask_size)
📌 Heavier side pulls the price.
________________________________________
🧩 PART 3 — PYTHON CODE (TYPE THIS)
best_bid = 100.00
best_ask = 100.10

bid_size = 500
ask_size = 200

imbalance = (bid_size - ask_size) / (bid_size + ask_size)

micro_price = (
    best_bid * ask_size +
    best_ask * bid_size
) / (bid_size + ask_size)

mid_price = (best_bid + best_ask) / 2

print("Imbalance:", imbalance)
print("Mid Price:", mid_price)
print("Micro Price:", micro_price)
________________________________________

👉 If micro_price > mid_price, which side (buyers or sellers) is stronger — and why?
Buyers are stronger because the ask side has less liquidity, so price is pulled upward toward the thinner side.
________________________________________
🧩 PART 4: FIRST REAL HFT-STYLE SIGNAL
Now we combine everything you’ve learned.
________________________________________
🧠 SIGNAL LOGIC (SIMPLE BUT REAL)
IF micro_price > mid_price
AND imbalance > 0.2
→ BUY

IF micro_price < mid_price
AND imbalance < -0.2
→ SELL

ELSE → NO TRADE
This is order-book-based, not candle-based.
________________________________________
🧩 PYTHON CODE (TYPE & RUN)
if micro_price > mid_price and imbalance > 0.2:
    print("BUY signal")
elif micro_price < mid_price and imbalance < -0.2:
    print("SELL signal")
else:
    print("NO TRADE")
________________________________________
👉 Why is this order-book (micro-price + imbalance) signal better than the mid-price-only signal from Day 18?
This signal is better because micro-price and imbalance use real order-book liquidity, giving a directional edge instead of noisy mid-price changes that ignore execution and supply–demand.
