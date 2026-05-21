from functools import reduce

orders = [250, 1200, 560, 50, 3000, 80]

# Remove small orders
valid_orders = list(filter(lambda x: x >= 100, orders))

# Apply discount
discounted = list(map(lambda x: x * 0.8 if x > 1000 else x, valid_orders))

# Total revenue
revenue = reduce(lambda x, y: x + y, discounted)

print("Valid Orders:", valid_orders)
print("Discounted Prices:", discounted)
print("Total Revenue:", revenue)
