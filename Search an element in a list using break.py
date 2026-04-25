lst = [10, 20, 30, 40, 50]

key = int(input("Enter element to search: "))

for i in lst:
    if i == key:
        print("Element found")
        break
else:
    print("Element not found")
