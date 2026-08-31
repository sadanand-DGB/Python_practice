s1 = {1, 2, 3, 4, 4 , 5, 5} #making a set
print(s1)  # print the set  (contains only unique elements)

s2 = {3, 4, 5, 6, 7} # making another set
print(s2)  # print the set

s2.remove(3)  # remove the element 3 from the set
print(s2)  # print the updated set

s2.add(8)  # add the element 8 to the set
print(s2)  # print the updated set
s2.update({9, 10})  # add multiple elements to the set
print(s2)  # print the updated set

s1.union(s2)  # union of two sets
print(s1.union(s2))  # print the union of two sets
s1.intersection(s2)  # intersection of two sets
print(s1.intersection(s2))  # print the intersection of two sets
