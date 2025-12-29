### DAY 14 – Tick-Level Backtesting & Why Most Backtests Lie ###

Today you learn why 99% of retail backtests are useless
and how HFTs think about backtesting.

🎯 Goal of Day 14

You will understand:
> Why candle backtests fail for HFT
> Look-ahead bias
> Execution bias
> Latency illusion

What “realistic backtesting” actually means

## PART 1: Why Candle Backtests Are Useless for HFT ##

Candles hide:
> Order book dynamics
> Queue position
> Partial fills
> Slippage
> Latency
HFT operates inside the candle.

## PART 2: The 4 Big Backtesting Lies ##
❌ Lie 1: Instant execution
Reality: Orders wait in queues.

❌ Lie 2: No slippage
Reality: Slippage eats profits.

❌ Lie 3: Zero latency
Reality: Microseconds decide profit or loss.

❌ Lie 4: Perfect fills
Reality: Partial or no fills.

## PART 3: “Thought Backtest” Example ##

Strategy edge: +0.01%
Latency cost: −0.02%

📉 Strategy dies — even if signals are “correct”.

## PART 4: HFT-Style Backtesting Mindset ##

HFTs ask:
> Can I enter first?
> Will I get filled?
> Can I exit safely?
> Is edge > costs?
If not — strategy is dead.

📝 DAY 14 CHALLENGE (MANDATORY)

Answer in your notes or here:

1️⃣ Why does candle data hide HFT reality?
2️⃣ Name two backtesting biases
3️⃣ Why can a strategy with correct prediction still lose money?
4️⃣ What matters more in HFT: prediction or execution?


> Because candles are aggregated summaries, not the market itself.
  But HFT reality lives inside the candle.
  Candles hide:
    > Order book dynamics
    > Queue position
    > Partial fills
    > Slippage
    > Latency

> Look-ahead bias and Execution bias

> Due to spread, liquidity down, latency and slippage, (costs > edge)

>Execution