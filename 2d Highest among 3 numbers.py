a=int(input("Enter number a:"))
b=int(input("Enter number b:"))
c=int(input("Enter number c:"))
if a>=b and a>=c:
    print("Highest number a is ",a)
elif b>=a and b>=c:
    print("Highest number b is ",b)
else:
    print("Highest number c is ",c)
