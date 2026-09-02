#variable length arguments (*args), when we are not sure about the number of arguments to be passed in the function
def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add(5, 6)) # This will print the sum of the arguments passed to the function.
print(add(5, 6, 7)) # This will print the sum of the arguments passed to the function.

#variable length keyword arguments (**kwargs), when we are not sure about the number of keyword arguments to be passed in the function
def info(**details):
    for key, value in details.items():
        print(key , ": " , value)

info(name="Alice", age=30, city="New York") # This will print the details passed to the function as keyword arguments.

