#creating a function that returns a value
def add(n1, n2):
    return n1 + n2

result = add(5, 6) # This will return the sum of n1 and n2, and assign it to the variable 'result'.
print(result) # This will print the value of 'result' to the console.

#creating a function without the return value
def add(n1, n2):
    print(n1 + n2)  

result = add(5, 6) # This will print the sum of n1 and n2 to the console, but it will not return anything. If you try to assign the result to a variable, it will be None.
print(result) # This will print 'None' to the console, because the function does not return anything.