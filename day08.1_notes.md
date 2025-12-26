***DAY 8 – Market Microstructure (Foundation of HFT)***

> HFT is NOT indicators.
> HFT is order flow, speed, and microstructure.

If you understand Day 8 deeply, you’ll understand why HFT firms make money.

🎯 Goal of Day 8
You will understand:
>What an order book is ?
>Bid vs Ask
>Spread
>Liquidity
>Slippage
>Why speed matters ?
>Why retail traders lose ?

No heavy coding today — this is mental model day.

🧩 PART 1: How a Market Actually Works
🏦 The Order Book (Limit Order Book – LOB)

At any moment:
    Buyers (Bids)	Price	 Sellers (Asks)
    120 lots	    100.00	   40 lots
    80 lots	        99.95	   60 lots
    200 lots	    99.90	   90 lots

> Bid = highest price someone is willing to BUY
> Ask = lowest price someone is willing to SELL
> Mid Price = (Bid + Ask) / 2
> Spread = Ask − Bid
👉 HFT lives inside the spread

🧠 PART 2: Why the Spread Exists

Spread exists because of:
> Risk (price may move)
> Adverse selection (smart traders trade against you)
> Latency (someone else may be faster)
Market makers earn the spread thousands of times per second.

🧩 PART 3: Liquidity (Most Important Concept)

🔹 High Liquidity
>Tight spread
>Large order sizes
>Easy to enter/exit

🔹 Low Liquidity
>Wide spread
>Small sizes
>Slippage is huge

HFT strategies only work where:
>Liquidity is massive + latency matters

Examples:
>NIFTY futures
>BANKNIFTY
>CME ES, NQ
> FX majors

🧩 PART 4: Slippage (Silent Killer)

Example:
    You click BUY at 100.00
    Actual fill = 100.05

    That 0.05 loss × 1000 trades = death.
HFT focuses more on slippage reduction than prediction.

🧩 PART 5: Why Retail Strategies Fail in HFT

Retail strategies:
> Indicators (RSI, MACD)
> Low frequency
> Market orders
> No latency control

HFT strategies:
> Order book imbalance
> Limit orders
> Microsecond decisions
> Queue position optimization

🧠 PART 6: HFT Profit Equation (VERY IMPORTANT)

Profit= Edge × Frequency − Costs

Where Costs =
 Spread
 Fees
 Slippage
 Latency losses
If costs > edge → strategy dies.

🧩 PART 7: Visual Mental Model

Think of the market as:
    A battlefield of queues, not prices.

Whoever is:
> Faster
> Closer to exchange
> Better positioned in queue
…wins.

📝 DAY 8 CHALLENGE (MANDATORY)

Answer in your own words (write in notebook or here):

What is the bid–ask spread?
Why does liquidity matter for HFT?
Why do market orders hurt HFT strategies?
Explain slippage with your own example
Why do HFT firms colocate servers near exchanges?

This thinking matters more than code.