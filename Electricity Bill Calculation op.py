from functools import reduce

bills = [450, 1200, 800, 300, 1500]

# Add GST
gst_bills = list(map(lambda x: x * 1.18, bills))

# Pending bills
pending = list(filter(lambda x: x > 500, gst_bills))

# Total collection
collection = reduce(lambda x, y: x + y, gst_bills)

print("Bills with GST:", gst_bills)
print("Pending Bills:", pending)
print("Total Collection:", collection)
