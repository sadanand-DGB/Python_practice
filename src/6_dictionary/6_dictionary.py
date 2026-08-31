# making a dictionary student names as keys and their marks as values
marks = {"Abc": 85,       
         "Def": 90,
         "Ghi": 78}
print(marks)  # print the dictionary
print(marks["Def"])  # print the value of key "Def"
print(len(marks))  # length of dictionary
print(marks.keys())  # print all the keys in the dictionary
print(marks.values())  # print all the values in the dictionary
print(marks.items())  # print all the key-value pairs in the dictionary

marks["Jkl"] = 88  # adding a new key-value pair to the dictionary
print(marks)  # print the updated dictionary

marks.update({"Abc":100, "Mno": 92})  # updating the value of keys "Abc" and adding new entry as "Mno"
print(marks)  # print the updated dictionary

del marks["Ghi"]  # deleting the key-value pair with key "Ghi"
print(marks)  # print the updated dictionary

marks.pop("Def")  # removing the key-value pair with key "Def"
print(marks)  # print the updated dictionary

marks.clear()  # clearing all the key-value pairs in the dictionary
print(marks)  # print the empty dictionary