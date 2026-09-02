# defining a lambda func does not require a name, it is an anonymous function

square = lambda x: x ** 2 # single argument lambda function.
print(square(5)) # This will print the square of 5, which is 25.

add = lambda a,b : a + b # multiple argument lambda function.
print(add(5, 6)) # This will print the sum of 5 and 6, which is 11.

greet = lambda name: "Hello, " + name + "!" # lambda function with a string return value.
print(greet("Sadanand")) # This will print "Hello, Sadanand!"

#lambda with a conditional expression
max_num = lambda a, b: a if a > b else b # lambda function with a conditional expression to find the maximum of two numbers.
print(max_num(5, 6)) # This will print the maximum of 5 and 6.