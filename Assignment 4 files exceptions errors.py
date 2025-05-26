#Task 1: Read a File and Handle Errors
try:
    file1 = open("sample.txt", "r")
    print("Reading file content:")
    print("Line 1: ", file1.readline())
    print("Line 2: ", file1.readlines())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
finally:
    print("\nThe file is readable")

#Task 2: Write and Append Data to a File
a=input("Enter Text to write to the file:")

with open("output.txt", "w") as file2:
    file2.write(a  + "\n")
    print("Data successfully written to output.txt")

b=input("Enter additional text to append:")
with open("output.txt", "a") as file3:
    file3.write(b)
    print("Data successfully written to output.txt")
    print("Data successfully appended")

with open("output.txt", "r") as file4:
    print("Final content of output.txt:\n", file4.read())

