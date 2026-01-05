### Where does latency come from? ###
### (Think: from signal → exchange → fill → confirmation)

DAY 15 — WHERE LATENCY COMES FROM (FULL ANSWER)

Latency is total time from idea → filled trade → confirmation.
It comes from multiple layers, not just “internet speed”.

1️⃣ Strategy / Decision Latency
    Time taken to:
    > Read market data
    > Update order book
    > Compute signals (micro-price, imbalance, logic)
💥 Python loops, pandas, logging → too slow

2️⃣ Software Latency
    > Language overhead (Python vs C++)
    > Garbage collection
    > OS context switches
    > Inefficient data structures

💡 HFT uses:
    > C / C++
    > Pre-allocated memory
    > Lock-free code

3️⃣ Network Latency
    Time for packets to travel:
    > Your server → exchange
    > Exchange → your server

    Includes:
    > Physical distance (speed of light limit)
    > Number of network hops
    > Router & switch delays
💥 This is why co-location exists.

4️⃣ Exchange Processing Latency
    Exchange time to:
    > Validate order
    > Match in order book
    > Update queue
    > Send confirmation
 Even exchanges have microsecond delays.

5️⃣ Queue Position Latency (MOST IMPORTANT)
    Even if your order arrives:
    > If others are ahead → you wait
    > Market moves → you miss fill
This kills most “good” signals.

6️⃣ Market Impact & Spread Cost
    Latency causes:
    > You cross the spread
    > You chase moving prices
    > Slippage increases
Hidden but deadly.

🧠 BIG REALIZATION (THIS IS KEY)
> In HFT, being right too late = being wrong