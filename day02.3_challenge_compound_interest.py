# Compound Interest Calculator
principal=float(input("Enter the principal amount: "))
rate=float(input("Enter the rate of interest (in %): "))
time=float(input("Enter the time period (in years): "))

# Compound Interest Calculation
compound_interest= principal*((1+rate/100)**time)-principal
print("The Compound Interest is:", compound_interest)
print("The Total Amount after", time, "years is:", principal + compound_interest)