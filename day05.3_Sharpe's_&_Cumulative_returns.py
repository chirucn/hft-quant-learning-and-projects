import numpy as np

# Create array of prices using NumPy
prices= np.array([100,102,105,98,90,110,115, 120,104,108])

# Computation of Daily Returns calculation
returns= (prices[1:]/prices[:-1])

#computation sharpe ratio
Sharpe_ratio= (np.mean(returns)/np.std(returns))*np.sqrt(252) #annualized sharpe ratio

#Computation of Cumulative Returns
Cumulative_returns= np.cumprod(1+returns)

# ploting cumulative returns
import matplotlib.pyplot as plt
plt.plot(Cumulative_returns)
plt.title("Cumulative Returns Over Time")
plt.show()
