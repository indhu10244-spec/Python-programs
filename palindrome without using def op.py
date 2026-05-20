palindrome=lambda x:x==x[::-1]
text=input("Enter a word:")
if palindrome(text):
    print("palindrome")
else:
    print("not palindrome")
