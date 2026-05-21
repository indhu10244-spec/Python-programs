from functools import reduce

temps_c = [36.5, 37.0, 39.2, 38.5, 36.8]

# Convert to Fahrenheit
temps_f = list(map(lambda x: (x * 9/5) + 32, temps_c))

# Fever patients
fever = list(filter(lambda x: x > 100, temps_f))

# Average temperature
total = reduce(lambda x, y: x + y, temps_f)
avg = total / len(temps_f)

print("Temperatures in Fahrenheit:", temps_f)
print("Fever Patients:", fever)
print("Average Temperature:", avg)
