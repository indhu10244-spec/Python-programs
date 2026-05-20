def palindrome(text):
    if text==text[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")
word=input("enter a word")
palindrome(word)
