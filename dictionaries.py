# 1. Create a dictionary of 5 countries and their capitals. Print it.
countries = {
    "India": "New Delhi",
    "USA": "Washington",
    "France": "Paris",
    "Germany": "Berlin",
    "UK": "London"
}
print("1.", countries)

# 2. Access the capital of "India" from the dictionary.
print("2. Capital of India:", countries["India"])

# 3. Add a new key-value pair "Japan": "Tokyo" to the dictionary.
countries["Japan"] = "Tokyo"
print("3.", countries)

# 4. Update the capital of "USA" from "Washington" to "New York".
countries["USA"] = "New York"
print("4.", countries)

# 5. Delete the key "France" using del.
del countries["France"]
print("5.", countries)



# 6. Create a dictionary of students and marks. Use .keys() to print all student names.
students = {
    "Aman": 85,
    "Riya": 90,
    "Rahul": 78
}
print("6. Student Names:", students.keys())

# 7. Use .values() to print all marks.
print("7. Marks:", students.values())

# 8. Use .items() to print all key-value pairs.
print("8. Student Details:", students.items())

# 9. Use .get() to access the value of "Rahul" safely.
print("9. Rahul's Marks:", students.get("Rahul", "Not Found"))

# 10. Use .update() to add multiple key-value pairs in one step.
students.update({"Neha": 88, "Karan": 92})
print("10.", students)



# 11. Use .pop(key) to remove "Germany" from the dictionary.
countries.pop("Germany")
print("11.", countries)

# 12. Try popping a non-existing key using .pop() with a default value.
removed = countries.pop("Spain", "Key Not Found")
print("12.", removed)

# 13. Use .clear() to remove all elements from the dictionary.
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print("13.", temp_dict)



# 14. Create a dictionary, make a copy using .copy(), and update the copy.
original = {"x": 10, "y": 20}
copy_dict = original.copy()
copy_dict["x"] = 100
print("14. Original:", original)
print("14. Copy:", copy_dict)



# 15. Count the frequency of words in a sentence using a dictionary.
sentence = "apple banana apple orange banana apple"
words = sentence.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print("15.", frequency)

# 16. Store product names as keys and prices as values. Print products costing more than 100.
products = {
    "Pen": 20,
    "Book": 150,
    "Bag": 600,
    "Bottle": 90
}
print("16. Products costing more than 100:")
for product, price in products.items():
    if price > 100:
        print(product, ":", price)

# 17. Write a program to check if "Apple" exists as a key in a dictionary.
fruits = {"Apple": 50, "Banana": 30, "Mango": 80}
print("17.", "Apple exists" if "Apple" in fruits else "Apple does not exist")
