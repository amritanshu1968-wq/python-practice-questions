#Amritanshu shukla(1230440009)
# Q1. Print Numbers (1 to 10) using for loop
for i in range(1, 11):
    print(i)


# Q2. Sum of first 10 natural numbers using while loop
i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print("Sum =", total)


# Q3. Multiplication Table up to 10 (user input) using for loop
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# Q4. Factorial of a number using while loop
n = int(input("Enter a number: "))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("Factorial =", fact)


# Q5. Reverse a Number using while loop
n = int(input("Enter a number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reversed number =", rev)


# Q6. Print Even Numbers between 1 and 50 using for loop
for i in range(1, 51):
    if i % 2 == 0:
        print(i)


# Q7. Sum of Digits of a Number using while loop
n = int(input("Enter a number: "))
sum_digits = 0

while n > 0:
    digit = n % 10
    sum_digits += digit
    n = n // 10

print("Sum of digits =", sum_digits)


# Q8. Fibonacci Series (first 10 terms) using for loop
a = 0
b = 1

print("Fibonacci Series:")
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
    