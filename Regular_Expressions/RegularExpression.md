# Regular Expressions (RegEx) in Python

Regular Expressions (RegEx) in Python are used for searching, matching, and manipulating text patterns. Python provides the re module to work with regular expressions.

## 1. Importing the re Module
To use regular expressions in Python, you need to import the re module:

    import re

## 2. Basic Functions of re Module
### re.match()
Tries to match a pattern only at the beginning of the string.
Returns a match object if found, else returns None.

Example:

    import re

    text = "Hello World"
    pattern = r"Hello"

    match = re.match(pattern, text)

    if match:
        print("Match found:", match.group())
    else:
        print("No match found")
Output:

    Match found: Hello
    Since "Hello" is at the beginning of text, it returns a match.

### re.search()
Searches the entire string for the first occurrence of the pattern.
Returns a match object if found, else None.

Example:

    text = "Welcome to the world of Python"
    pattern = r"world"

    match = re.search(pattern, text)

    if match:
        print("Match found at position:", match.start())
    else:
        print("No match found")
Output:

    Match found at position: 11

### re.findall()
Returns all occurrences of the pattern in the string as a list.
Example:

    text = "abc 123 xyz 456 abc 789"
    pattern = r"abc"

    matches = re.findall(pattern, text)
    print(matches)

Output:

    ['abc', 'abc']
### re.finditer()
Similar to findall(), but returns an iterator yielding match objects instead of a list of strings.
Example:

    text = "apple orange apple banana apple"
    pattern = r"apple"

    matches = re.finditer(pattern, text)

    for match in matches:
        print("Match found at:", match.start())

Output:

    Match found at: 0
    Match found at: 14
    Match found at: 27

### re.sub()

Replaces all occurrences of a pattern with a specified replacement string.
Example:

    text = "Hello 123, Welcome 456!"
    pattern = r"\d+"  # Matches any digit sequence
    new_text = re.sub(pattern, "###", text)
    print(new_text)
Output:
    Hello ###, Welcome ###!
    
### re.split()
Splits the string by occurrences of the pattern.
Example:
    text = "apple,banana;cherry orange"
    pattern = r"[,; ]"  # Matches comma, semicolon, or space

    words = re.split(pattern, text)
    print(words)
Output:

    ['apple', 'banana', 'cherry', 'orange']
## Regular Expression Metacharacters

|Metacharacter	|Description|	Example|
|--------------|-------------|-----------|
|.	|Matches any character except newline	|"c.t" matches "cat", "cut", "c9t"|
|^	|Matches the start of the string	|^Hello matches "Hello world" but not "world Hello"|
|$	|Matches the end of the string	|world$ matches "Hello world" but not "world Hello"|
|*	|Matches 0 or more occurrences	|"ab*" matches "a", "ab", "abb", "abbb"|
|+	|Matches 1 or more occurrences	|"ab+" matches "ab", "abb", "abbb" but not "a"|
|?	|Matches 0 or 1 occurrence	|"ab?" matches "a" and "ab", but not "abb"|
|{n}	|Matches exactly n occurrences	|"a{3}" matches "aaa" but not "aa"|
|{n,}	|Matches at least n occurrences	|"a{2,}" matches "aa", "aaa", "aaaa"|
|{n,m}	|Matches between n and m occurrences	|"a{2,4}" matches "aa", "aaa", "aaaa" but not "a"|
|\d	|Matches any digit (0-9)	|"Item \d" matches "Item 1", "Item 9"|
|\D	|Matches any non-digit	|"\D+" matches "Hello" but not "123"|
|\s|	Matches any whitespace character	|"Hello\sWorld" matches "Hello World"|
|\S	|Matches any non-whitespace character	|"\S+" matches "Hello" but not " "|
|\w	|Matches any word character (a-z, A-Z, 0-9, _)	|"Hello\w" matches "Hello1"|
|\W	|Matches any non-word character	|"Hello\W" matches "Hello!"|
|`	|`	|Matches either pattern on left or right|
|()|	Groups patterns	|"(abc)+" matches "abc", "abcabc"|

## 4. Using Flags in Regular Expressions
Python re module provides flags to modify search behavior.

|Flag|	Description|
|---------|----------|
|re.IGNORECASE (re.I)	|Case-insensitive matching|
|re.MULTILINE (re.M)	|Multi-line matching (^ and $ match at line boundaries)|
|re.DOTALL (re.S)	|Allows . to match newline characters|

Example:

    text = "HELLO world"
    pattern = r"hello"

    match = re.search(pattern, text, re.IGNORECASE)
    print(match.group())  # Output: HELLO
## 5. Compiling Regular Expressions
To improve performance, you can compile a regex pattern and reuse it multiple times.

Example:

    pattern = re.compile(r"\d+")  # Compiling a pattern

    text = "Order 123, Item 456"
    matches = pattern.findall(text)
    print(matches)  # Output: ['123', '456']

## 6. Practical Example: Extracting Email Addresses

    text = "Contact us at support@example.com or sales@mywebsite.org"

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    emails = re.findall(pattern, text)
    print(emails)
Output:
    ['support@example.com', 'sales@mywebsite.org']