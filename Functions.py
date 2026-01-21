#functions
# 1. Write a function that prints "Hello, World!"
def hello_world():
    print("Hello, World!")

# Function call
hello_world()


# 2. Write a function that takes a name as input and prints "Hello, <name>"
def greet_name(name):
    print(f"Hello, {name}")

# Function call
greet_name("Amritanshu")


# 3. Write a function that takes two numbers and prints their sum
def print_sum(a, b):
    print("Sum:", a + b)

# Function call
print_sum(10, 20)


# 4. Write a function that returns the square of a number
def square(num):
    return num * num

# Function call
print("Square:", square(5))


# 5. Write a function to check if a number is even or odd
def even_or_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Function call
even_or_odd(7)


# 6. Write a function that takes two numbers and returns their maximum
def maximum(a, b):
    return a if a > b else b

# Function call
print("Maximum:", maximum(15, 25))


# 7. Write a function that takes a list of numbers and returns their average
def average(numbers):
    return sum(numbers) / len(numbers)

# Function call
print("Average:", average([10, 20, 30, 40, 50]))


# 8. Write a function that counts vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Function call
print("Vowel Count:", count_vowels("Hello World"))

#9 write a function that calculates factorial of a number (using loop)
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Function call
print("Factorial:", factorial(5))

#10 write a function ti check if a string is a palindrome.
def is_palindrome(a):
    a = a.lower()              # convert to lowercase for uniformity
    if a == a[::-1]:
        return True
    else:
        return False

# Function call
print("Is Palindrome:", is_palindrome("Madam"))
#default and keyword arguments
#11 write a function that calculates simple interest(default rate =5%)
def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si

# Function call
print("Simple Interest:", simple_interest(1000, 2))


#12 write a function that takes a name and age and prints them (use keyword arguments)
def print_details(name, age):
    print("Name:", name)
    print("Age:", age)

# Function call using keyword arguments
print_details(age=20, name="Amritanshu")
