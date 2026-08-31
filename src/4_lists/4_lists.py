a = [100,36.5,50,28]  # making a list
print(a)  # print the list
print(len(a))  # length of list
print(a[0])  # first element of list
print(a[1:3])  # elements from index 1 to 2

a.sort()  # sort the list in ascending order
print(a)  # print the sorted list

a.insert(2, "apple")  # insert "apple" at index 2
print(a)  # print the updated list
a.append("banana")  # append "banana" at the end of the list
print(a)  # print the updated list 
a.remove(36.5)  # remove the element 36.5 from the list
print(a)  # print the updated list

print(a.pop(3))  # remove and return the element at index 3

