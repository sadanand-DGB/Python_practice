my_tuple = (100, 35, 4.5, 2) # making a tuple

print(my_tuple)  # print the tuple
print(len(my_tuple))  # length of tuple
print(my_tuple[0])  # first element of tuple
print(my_tuple[1:3])  # elements from index 1 to 2
print(min(my_tuple))  # minimum value in the tuple
print(max(my_tuple))  # maximum value in the tuple

my_tuple2 = ("banana", 50, 28, False) # making another tuple
combined_tuple = my_tuple + my_tuple2  # concatenation of tuples
print(combined_tuple)  # print the combined tuple

print(combined_tuple.count(35))  # count the occurrences of 35 in the tuple
print(combined_tuple.index("banana"))  # find the index of "banana" in the tuple
