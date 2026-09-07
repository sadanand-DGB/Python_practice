try:
    marks = int(input("Enter marks: "))       # Convert input to integer

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be 0-100") # Raise an exception

    print("Valid marks:", marks)

except ValueError as error:
    print("Error:", error)                    # Handle invalid input

else:
    print("Marks entered successfully")       # Runs if no error

finally:
    print("Done")                             # Always runs