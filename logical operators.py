# Q1. Pass in Both Subjects (and)
math = int(input("Enter Math marks: "))
science = int(input("Enter Science marks: "))
if math >= 40 and science >= 40:
    print("Pass")
else:
    print("Fail")

# Q2. Eligible for Discount (or)
amount = int(input("Enter purchase amount: "))
member = input("Do you have membership card (yes/no): ")
if amount > 1000 or member == "yes":
    print("Discount Available")
else:
    print("No Discount")

# Q3. Not Divisible by 3 (not)
num = int(input("Enter number: "))
if not num % 3 == 0:
    print("Not divisible by 3")
else:
    print("Divisible by 3")

# Q4. Teenager Check (and)
age = int(input("Enter age: "))
if age >= 13 and age <= 19:
    print("Teenager")
else:
    print("Not a Teenager")

# Q5. Voting & Driving Eligibility
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")
if age >= 18 and age <= 70:
    print("Eligible to Drive")
else:
    print("Not Eligible to Drive")

# Q6. Valid Exam Candidate
attendance = int(input("Enter attendance percentage: "))
assignment = input("Assignment submitted (yes/no): ")
if attendance >= 75 and assignment == "yes":
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")

# Q7. Leap Year (using and / or)
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

# Q8. Weekend or Holiday
day = input("Enter day: ")
holiday = input("Is it a holiday (yes/no): ")
if day == "Sunday" or holiday == "yes":
    print("Relax")
else:
    print("Work Day")

# Q9. Multiple of 3 and 5
num = int(input("Enter number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")

# Q10. Login Validation
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")
