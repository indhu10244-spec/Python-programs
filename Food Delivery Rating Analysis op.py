from functools import reduce

ratings = [3.5, 4.2, 4.8, 2.9, 4.0]

# Premium bonus
updated = list(map(lambda x: x + 0.2, ratings))

# Top restaurants
top = list(filter(lambda x: x > 4, updated))

# Average rating
total = reduce(lambda x, y: x + y, updated)
avg = total / len(updated)

print("Updated Ratings:", updated)
print("Top Restaurants:", top)
print("Average Rating:", avg)
