def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
n=int(input("enter num"))
res=fact(n)
print(f"the fact of{n} is{res}")
