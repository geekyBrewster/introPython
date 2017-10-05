meal = 44.50
tax = 6.75 / 100
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total) # "%.2f" is an argument specifier for a floating pt w/ 2 decimals

# With Python installed, can run app using 'python tipCalculator.py' in the terminal
