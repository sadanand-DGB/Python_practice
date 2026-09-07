# Create and write to the file
with open("dogs.txt", "w") as file:
    file.write("Dogs are friendly.\n")       # Write first sentence
    file.write("Dogs love to play.\n")       # Write second sentence


# Read the file
with open("dogs.txt", "r") as file:
    print(file.read())                       # Display content


# Append more content
with open("dogs.txt", "a") as file:
    file.write("Dogs are loyal.\n")          # Add a sentence


# Read the final content
with open("dogs.txt", "r") as file:
    print(file.read())                       # Display updated content
    