text = input("Enter a string: ")

for ch in text:
    if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
        continue
    print(ch, end="")
