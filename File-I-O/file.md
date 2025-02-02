# Python File I/O (Input/Output)

## 1. Introduction to File Handling in Python

File handling in Python is used to read, write, and manipulate files stored on disk. Python provides built-in functions to handle files, making it easy to perform operations like reading from and writing to files.

##### Python handles two types of files:

**Text Files**: Files containing human-readable characters (e.g., .txt, .csv, .json).
**Binary Files**: Files containing non-human-readable data (e.g., images, videos, .exe files)

## 2. Opening a File in Python

Python provides the open() function to work with files. The syntax is:

    file = open("filename", "mode")

+ "filename": The name of the file (with the path if it’s in another directory).
+ "mode": Specifies whether to read, write, or append to the file.

### File Modes in Python

| Mode|	Description|
|-------|-----------|
| 'r'	|Read mode (default). Opens the file for reading.|
| 'w'	|Write mode. Creates a new file or overwrites an existing file.|
| 'a'	|Append mode. Opens the file for writing but does not overwrite existing content.|
| 'x'	|Exclusive creation mode. Fails if the file already exists.|
| 'b'	|Binary mode. Used for non-text files (e.g., images).|
| 't'	|Text mode (default). Reads and writes strings.|

***Example of opening a file:***
    
    file = open("sample.txt", "r")  # Open the file in read mode

## 3. Closing a File

It is important to close a file after performing operations to free up system resources.
    file.close()

A better way to handle files is using the with statement, which automatically closes the file:

    with open("sample.txt", "r") as file:
    content = file.read()
    # The file is automatically closed outside the `with` block.

## 4. Reading Files
There are multiple ways to read files in Python.

### read() Method

Reads the entire file content as a single string.
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)

### readline() Method
Reads one line at a time.
    with open("sample.txt", "r") as file:
        line = file.readline()  # Reads the first line
        print(line)


### readlines() Method
Reads all lines and returns them as a list of strings.
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        print(lines)  # Output: ['First line\n', 'Second line\n']

### Looping Over a File
Efficient way to read files line by line:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())  # Remove newline characters

## 5. Writing to Files
To write to a file, use the 'w' or 'a' mode.

### write() Method
+ 'w' mode: Overwrites the file if it exists; creates a new file if it doesn’t.
+ 'a' mode: Appends to the file without deleting existing content.

    with open("output.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a test file.\n")

###  Writing Multiple Lines (writelines())
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

    with open("output.txt", "w") as file:
        file.writelines(lines)

## 6. Appending to a File
To add content without overwriting the existing file, use the 'a' mode:
    with open("output.txt", "a") as file:
        file.write("Appending this line.\n")

## 7. Working with Binary Files
To read and write binary files (e.g., images, videos), use the 'b' mode.
### Reading a Binary File
    with open("image.jpg", "rb") as file:
        binary_data = file.read()
        print(binary_data[:10])  # Print first 10 bytes

### Writing a Binary File

    with open("copy.jpg", "wb") as file:
        file.write(binary_data)

## 8. Checking if a File Exists
To prevent errors when opening a file, check if it exists using os.path.exists().

    import os

    if os.path.exists("sample.txt"):
        with open("sample.txt", "r") as file:
            print(file.read())
    else:
        print("File not found!")

## 9. Deleting a File
To delete a file, use os.remove().

    import os

    if os.path.exists("sample.txt"):
        os.remove("sample.txt")
        print("File deleted successfully!")
    else:
        print("File does not exist!")

## 10. File Handling with Exception Handling
Always handle file operations with try-except blocks to prevent crashes.

    try:
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: File not found!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

## 11. File Positioning with seek() and tell()
+ seek(offset, whence): Moves the file pointer to a specific position.
+ tell(): Returns the current file pointer position.

    with open("sample.txt", "r") as file:
        print(file.tell())  # Output: 0 (start of file)
        file.seek(5)        # Move to the 5th byte
        print(file.tell())  # Output: 5
        print(file.read())  # Read from the 5th byte onwards
## 12. Working with CSV Files
Python provides the csv module to handle CSV files.

### Reading a CSV File
    import csv

    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

### Writing to a CSV File

    import csv

    data = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]

    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


|Operation |	Method|
|-----------|----------|
|Open a file |	open("filename", "mode")|
|Close a file|	file.close()|
|Read full file|	file.read()|
|Read one line|	file.readline()|
|Read all lines|	file.readlines()|
|Write to a file|	file.write("text")|
|Write multiple lines|	file.writelines(["line1\n", "line2\n"])|
|Append to a file|	Open file with 'a' mode|
|Read binary files|	Open file with 'rb' mode|
|Write binary files|	Open file with 'wb' mode|
|Delete a file|	os.remove("file.txt")|

