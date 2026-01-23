
# 1. Program to take two numbers and print sum, difference, product, and quotient


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)

# 2. Given a = 15 and b = 4 Floor division, remainder, and power


a = 15
b = 4

print("Floor Division (a // b):", a // b)
print("Remainder (a % b):", a % b)
print("Power (a ** b):", a ** b)

# 3. Total cost of 3 pens and 2 notebooks Pen = ₹15, Notebook = ₹40

pen_price = 15
notebook_price = 40

total_cost = (3 * pen_price) + (2 * notebook_price)
print("Total Cost: ₹", total_cost)


# 4. Program to calculate average of 5 numbers

n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
n3 = float(input("Enter number 3: "))
n4 = float(input("Enter number 4: "))
n5 = float(input("Enter number 5: "))

average = (n1 + n2 + n3 + n4 + n5) / 5
print("Average:", average)

# 5. Program to print square, cube, and square root


n = float(input("Enter a number: "))

print("Square:", n ** 2)
print("Cube:", n ** 3)
print("Square Root:", n ** 0.5)


# 6. Convert total seconds into minutes and seconds

total_seconds = int(input("Enter total seconds: "))

minutes = total_seconds // 60
seconds = total_seconds % 60

print("Minutes:", minutes)
print("Seconds:", seconds)

# 7. Average speed of a car Distance = 120 km, Time = 3 hours

distance = 120
time = 3

average_speed = distance / time
print("Average Speed:", average_speed, "km/h")

# 8. Check if first number is a multiple of second
x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))

if x % y == 0:
    print(x, "is a multiple of", y)
else:
    print(x, "is not a multiple of", y)


# 9. Program to calculate Simple Interest SI = (P * R * T) / 100


P = float(input("Enter Principal: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (years): "))

SI = (P * R * T) / 100
print("Simple Interest:", SI)


# 10. Program to print rounded quotient using floor division (//)


num1 = float(input("Enter first floating-point number: "))
num2 = float(input("Enter second floating-point number: "))

print("Rounded Quotient:", num1 // num2)
