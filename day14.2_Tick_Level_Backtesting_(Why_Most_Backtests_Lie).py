#-------------------------------------------|
### Step 1: Create a Toy Tick Market ###    |
#-------------------------------------------|
import numpy as np
import pandas as pd

np.random.seed(42)   # What seed(42) actually does
                     # Think of randomness as a deck of shuffled cards.
                     # seed(42) = choose one fixed shuffle
                     # Every time you run the code → same shuffle
                     # Change the seed → different shuffle

n_ticks=1000

#simulate mid price random walk
mid_price= 100 + np.cumsum(np.random.normal(0,0.01,n_ticks))
# A) np.random.normal(0, 0.01, n_ticks)      (B) np.cumsum(...)                           (C) 100 + ...                     Mid-price = (best bid + best ask) / 2
#    Generates 1,000 tiny price shocks           Cumulative sum                               Starting price = 100          This is what HFT models actually predict, not candle closes.What seed(42) actually does
#    Mean = 0 → no directional bias              Turns noise into a random walk
#    Std = 0.01 → very small moves (ticks)              

# Fixed Spread
spread= 0.02

# Bid -Ask Construction
bid= mid_price - spread/2
ask= mid_price + spread/2

# Create DataFrame
df = pd.DataFrame({ 
    "mid": mid_price, 
    "bid": bid, 
    "ask": ask })


#----------------------------------------------|
### Step 2: Create a Micro-Price Signal ###    |
#----------------------------------------------|
df["imbalance"]=np.random.uniform(-1,1,n_ticks) # Simulate random order book imbalance between -1 and 1
