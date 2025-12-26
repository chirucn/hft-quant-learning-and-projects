import numpy as np

# Create array of prices using NumPy
prices= np.array([100,102,105,98,90,110,115, 120,104,108])

# Computation of Daily Returns calculation
returns= (prices[1:]/prices[:-1])

#Define signal: 1 for Buy, -1 for Sell
signals= np.where(returns>0, 1, -1)

#Simulate portfolio performance
initial_cash= 100000
position_size= 1000 #invest 1000 per signal
cash= initial_cash+np.sum(signals*returns*position_size)

#Print results
print("Prices:", prices)
print("Daily Returns (%):", np.round(returns*100,2), "%")
print("Signals (Buy=1, Sell=-1):", signals)
print("Final Cash after Strategy:", cash)
print("Total Profit/Loss;", cash-initial_cash)
