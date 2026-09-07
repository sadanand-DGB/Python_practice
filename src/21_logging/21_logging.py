import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program started")

try:
    marks = int(input("Enter your marks: "))       # Ask user for marks

    if marks < 0 or marks > 100:
        logging.warning("Marks are outside the valid range")
    else:
        logging.info("Marks are valid")

    result = 100 / marks
    logging.info("Result calculated successfully")

except ZeroDivisionError:
    logging.error("Cannot divide by zero")

logging.info("Program finished")