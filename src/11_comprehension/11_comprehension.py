#Comprehension is a short and concise way to create a collection.

#list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(squares)

#set comprehension
numbers = [1, 2, 3, 4, 5]
squares = {x ** 2 for x in numbers}
print(squares)

#dictionary comprehension
numbers = [1, 2, 3, 4, 5]      
squares = {x: x ** 2 for x in numbers}
print(squares)