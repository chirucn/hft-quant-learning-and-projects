# Create array of prices using NumPy
import numpy as np
prices= np.array([100,110,98,105,85,108,115])
print(prices)
print(type(prices))

#Vectorized operations
returns= (prices[1:]/prices[:-1])*100
print("Daily returns (%):", returns)


# Numpy Statistics for Quants
mean_return= np.mean(returns)
std_return= np.std(returns)
max_return= np.max(returns)
min_return= np.min(returns)

print("Mean return:", mean_return)
print("Std return:", std_return)
print("Max return:", max_return)
print("Min return:", min_return)