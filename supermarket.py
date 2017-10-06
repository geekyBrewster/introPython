shopping_list = ["banana", "orange", "apple"]

prices = {
  "banana" : 4,
  "apple" : 2,
  "orange" : 1.5,
  "pear" : 3
}

stock = {
  "banana" : 6,
  "apple" : 0,
  "orange" : 32,
  "pear" : 15
}

#Single loop to loop thru both dictionaries
for key in prices:
	print key
	print "price: " + str(prices[key])
	print "stock: " + str(stock[key])

#Figure out total inventory in $$
total = 0

for key in prices:
  total += prices[key] * stock[key]

print total

# Figure out how much the grocery list would cost
def compute_bill(food):
  total = 0
  for item in food:
      if stock[item] > 0:
        total = total + prices[item]
        stock[item] = stock[item] - 1
  return total
