
# Q1. Equality Check Program to input two numbers and check if they are equal


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("Both numbers are equal")
else:
    print("Numbers are not equal")

# Q2. Greater Number Program to find which number is greater


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    print(x, "is greater")
else:
    print(y, "is greater or equal")


# Q3. Minimum Finder Program to find the smallest of three numbers


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest number is:", a)
elif b <= a and b <= c:
    print("Smallest number is:", b)
else:
    print("Smallest number is:", c)


# Q4. Pass/Fail Checker Program to check pass or fail based on marks

marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# Q5. Voting Eligibility Program to check voting eligibility


age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")



# Q6. Even or Odd Program to check if a number is even or odd


num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Q7. Compare Strings Program to compare two strings


str1 = input("Enter first word: ")
str2 = input("Enter second word: ")

if str1 == str2:
    print("Both strings are same")
else:
    print("Strings are different")


# Q8. Salary Comparison Program to compare salaries of two employees

salary_a = float(input("Enter salary of Employee A: "))
salary_b = float(input("Enter salary of Employee B: "))

if salary_a > salary_b:
    print("Employee A earns more")
else:
    print("Employee B earns more or equal")


# Q9. Number Range Check Program to check if number lies between 10 and 50


num = int(input("Enter a number: "))

if 10 <= num <= 50:
    print("Number lies between 10 and 50")
else:
    print("Number is outside the range")



# Q10. Leap Year Check Program to check if a year is a leap year


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
