# writing in a file
# with open("test.txt", "w") as file:
#     file.write("Hello, this is a test file.\n")
#     file.write("We are learning file handling in Python.\n")

# reading a file as a whole
# with open("test.txt", "r") as file:
#     content = file.read()
#     print("File Content:\n", content)

# append mode
# with open("test.txt", "a") as file:
#     file.write("This line is added later.\n")

# reading file line by libe
with open("test.txt", "r") as file:
    for line in file:
        print(line.strip())
