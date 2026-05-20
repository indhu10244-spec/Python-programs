from functools import reduce
marks=[78,45,90,32,88,67,29]
#Students passed
passed=list(filter(lambda x:x>=40,marks))
#Add grace marks
grace_marks=list(map(lambda x:x+5,marks))
#Total Marks
total=reduce(lambda x,y:x+y,marks)
average=total/len(marks)
print("Passed Students Marks:",passed)
print("Grace Marks:",grace_marks)
print("Total Marks:",total)
print("Average Marks:",average)
