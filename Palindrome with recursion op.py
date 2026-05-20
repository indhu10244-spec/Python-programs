def palindrome(word):
    if len(word)<=1:
        return True
    if word[0]==word[-1]:
        return palindrome(word[1:-1])
    else:
        return False
text=input("enter a")
if(palindrome(text)):
    print("palindrome")
else:
    print("not p")
