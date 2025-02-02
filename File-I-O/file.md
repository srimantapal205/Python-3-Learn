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

