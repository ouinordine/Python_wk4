#  program that reads a file and writes a modified version to a new file.

with open("input.txt", "r") as firstfile, open("input2.txt", "w") as secondfile:
    data = firstfile.read()
    modifieddata = data + "\nBon appetit!"
    secondfile.write(modifieddata)


# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

filename = input("Enter a file name to display content: ")

try:
    file = open(filename, "r")
    filedata = file.read()
    print(filedata)
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()