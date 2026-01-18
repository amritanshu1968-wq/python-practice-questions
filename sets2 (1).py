# 4. Create a set and use add() to insert a new element
s = {1, 2, 3}
s.add(4)
print("After add():", s)


# 5. Remove an element using remove() and observe what happens if the element is not present
s.remove(2)
print("After remove(2):", s)

# Uncommenting the next line will cause KeyError because 10 is not present
# s.remove(10)


# 6. Remove an element using discard() and compare it with remove()
s.discard(3)
print("After discard(3):", s)

# No error even if element is not present
s.discard(10)
print("After discard(10):", s)


# 7. Use pop() to remove a random element from a set
removed_element = s.pop()
print("Popped element:", removed_element)
print("Set after pop():", s)


# 8. Create two sets and find their union
A = {1, 2, 3}
B = {3, 4, 5}
print("Union:", A.union(B))


# 9. Create two sets and find their intersection
print("Intersection:", A.intersection(B))


# 10. Create two sets and find their difference (A - B)
print("Difference (A - B):", A.difference(B))


# 11. Use copy() to create a copy of a set and modify the copy
C = A.copy()
C.add(10)
print("Original set A:", A)
print("Copied & modified set C:", C)


# 12. Use clear() to empty a set
C.clear()
print("After clear():", C)


# 13. Convert a list with duplicates into a set to remove duplicates
lst = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(lst)
print("Set after removing duplicates:", unique_set)


# 14. Write a program to find unique characters in a string using a set
text = "programming"
unique_chars = set(text)
print("Unique characters in string:", unique_chars)
