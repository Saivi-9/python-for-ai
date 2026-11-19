#Running sum of 1D array
nums = [1, 4, 6, 8, 11, 16]

print(sum(nums))
runningSum = []
running_sum = 0
for i in nums:
    running_sum += i

    runningSum.append(running_sum)

print(runningSum)

#Richest Customer Wealth
accounts = [[2, 8], [5, 5], [1, 20]]

accounts_total = []
for account in accounts:
    customer_total = sum(account)
    accounts_total.append(customer_total)

print(accounts_total)
print("Max customer wealth:", max(accounts_total))


#Counter
numbers = [-3, 7, 0, 15, -8, 9, 2]

less_than_zero = []

for num in numbers:
    if num < 0:
        less_than_zero.append(num)

count = len(less_than_zero)
print(count)

print(less_than_zero)

#Largest Number without using max function
num = [12, 7, 25, 3, 18, 40, 9]

largest = num[0]

for i in num:
    if i > largest:
        largest = i


print(largest)

#Student Grade Analysis
grades = [
    [85, 90, 78],
    [60, 72, 68],
    [95, 88, 91],
    [70, 75, 80]
]

total_grades = 0
grade_total = []



for i in grades:
    total_grades = 0
    for i in i:
        total_grades += i

    grade_total.append(total_grades)

print(grade_total)

#Best student without using max
for i in range(len(grade_total)):
    print(f"Student {i + 1} Total: {grade_total[i]}")

highest_total = grade_total[0]

for i in grade_total:
    if highest_total < i:
        highest_total = i

best_student = grade_total.index(highest_total) + 1


print(f"Best Student: Student {best_student}")
print(f"Highest Total: {highest_total}")

#Functions
def greet(name):
    print("Hello!", name)

Name = input("Enter your name: ")
greet(Name)

def help(name):
    print("Helping", name)

help("Ola")


def multiply(a, b):
    print(f"The product of {a} and {b} is {a * b}")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

multiply(a, b)

#Counter


input(range)
print(range)


