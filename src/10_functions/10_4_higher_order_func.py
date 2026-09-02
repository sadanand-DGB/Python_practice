# HOF takes func as arg or it returns a func as output. It is a func that operates on other funcs, either by taking them as arguments or by returning them.
# common HOFs are map(), filter() and reduce().

numbers = [1, 2, 3, 4, 5] 

#map() applies the given function to each item of the iterable (numbers) and returns a list of the results.  
result = map(lambda x: x ** 2, numbers) # map() applies the given function to each item of the iterable (numbers) and returns a list of the results.
print(list(result)) # This will print the squares of the numbers in the list.

#filter() applies the given function to each item of the iterable (numbers) and returns a list of the items for which the function returns True.
result2 = filter(lambda x: x % 2 == 0, numbers) 
print(list(result2)) # This will print the even numbers in the list.

#reduce() applies the given function cumulatively to the items of the iterable (numbers), from left to right, so as to reduce the iterable to a single value.
from functools import reduce   
result3 = reduce(lambda x, y: x + y, numbers) 
print(result3) # This will print the sum of the numbers in the list.