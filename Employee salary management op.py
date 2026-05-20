from functools import reduce

# Employee salaries
salary = [45000, 55000, 60000, 40000, 70000]

# Increase salary by 10%
updated_salary = list(map(lambda x: x * 1.10, salary))

# Employees earning above 50000
high_salary = list(filter(lambda x: x > 50000, salary))

# Total salary expenditure
total = reduce(lambda x, y: x + y, salary)

print("Original Salaries:", salary)
print("Updated Salaries:", updated_salary)
print("Employees earning above 50000:", high_salary)
print("Total Salary Expenditure:", total)
