# 1. Create a set of 5 colors and print it
colors = {"red", "blue", "green", "yellow", "black"}
print("Colors set:", colors)


# 2. Create a set of numbers with duplicates and check how Python handles duplicates
numbers = {1, 2, 3, 2, 4, 1, 5}
print("Set with duplicates removed:", numbers)


# 3. Write a program to loop through a set and print each element
print("Looping through the set:")
for num in numbers:
    print(num)


# 4. Create a set and use add() to insert a new element
s = {1, 2, 3}
s.add(4)
print("After adding an element:", s)


# 5. Remove an element using remove() and observe what happens if the element is not present
s.remove(2)
print("After removing element 2:", s)

# Uncommenting the next line will raise KeyError because 10 is not present
# s.remove(10)


# 6. Remove an element using discard() and compare it with remove()
s.discard(3)
print("After discarding element 3:", s)

# No error even though element is not present
s.discard(10)
print("After discarding non-existing element:", s)


# 7. Use pop() to remove a random element from a set
removed = s.pop()
print("Randomly removed element:", removed)
print("Set after pop():", s)


# 8. Create two sets and find their union
a = {1, 2, 3}
b = {3, 4, 5}
union_set = a.union(b)
print("Union of two sets:", union_set)
