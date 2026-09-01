# In conditionals, we can use if, elif, and else statements to control the flow of our program based on certain conditions.

age = int(input("Enter your age: ")) #user input for age

#if-elif-else statement to determine the age category

if age >= 18:
    print("You are an adult.")

elif age >= 13:
    print("You are a teenager.")

else:
    print("You are a child.")