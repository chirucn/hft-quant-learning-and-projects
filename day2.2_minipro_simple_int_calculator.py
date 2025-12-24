# Simple Interest Calculator

principal=float(input("Enter the principal amount: "))
rate=float(input("Enter the rate of interest (in %): "))
time=float(input("Enter the time period (in years): "))

# Simple Interest Calculation
simple_interest = (principal * rate * time) / 100
print("The Simple Interest is:", simple_interest)
print("The Total Amount after", time, "years is:", principal + simple_interest)