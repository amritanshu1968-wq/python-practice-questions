# Q1. Print Numbers (for loop)
# Print numbers from 1 to 10
for i in range(1, 11):
    print(i)



# Q2. Sum of Numbers (while loop)
# Sum of first 10 natural numbers
i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1
print("Sum of first 10 natural numbers =", sum)


# Q3. Multiplication Table (for loop)
# Print multiplication table of a number
num = int(input("Enter a number for table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)



# Q4. Factorial (while loop)
# Find factorial of a number
num = int(input("Enter a number for factorial: "))
fact = 1
temp = num
while num > 0:
    fact *= num
    num -= 1
print("Factorial of", temp, "=", fact)



# Q5. Reverse a Number (while loop)
# Reverse the digits of a number
num = int(input("Enter a number to reverse: "))
rev = 0
while num > 0:
    rev = rev * 10 + (num % 10)
    num //= 10
print("Reversed number =", rev)


# Q6. Even Numbers (for loop with range)
# Print all even numbers between 1 and 50
for i in range(2, 51, 2):
    print(i)



# Q7. Sum of Digits (while loop)
# Find sum of digits of a number
num = int(input("Enter a number to find sum of digits: "))
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
print("Sum of digits =", sum)


# Q8. Fibonacci Series (for loop)
# Print first 10 terms of Fibonacci series
a = 0
b = 1
print(a)
print(b)
for i in range(8):
    c = a + b
    print(c)
    a = b
    b = c
