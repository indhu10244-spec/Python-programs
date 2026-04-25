print("\n====SET EXAMPLE===")
numbers={1,2,3,2,1}
print("Set:",numbers)
numbers.add(4)
numbers.discard(2) #no error if element not found 
print("Set:",numbers)
#Set Operations 
evens={2,4,6}
print("Union:", numbers|evens)
print("Insertion:", numbers&evens)
