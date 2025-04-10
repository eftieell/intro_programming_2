## Opening files

Before reading from a file (input) or writing to a file(output), the program must *open* the file.

The `open()` function returns a file object, which can then be used for reading, writing or appending to a file.

```python
some_file = open('<path/file_name>', mode  = <'string'>')
```
If the file we're trying to open is in the same directory (folder) as the program we're running, then `file_name.extension` is sufficient. If the file is stored somewhere else in the file system, then we specify a full path to the file. If the file we are trying to open does not exist, the program will crash with a `FileNotFound` exception.

Modes:

| Mode      | Name | Details |
| --------- | ---- |---------|
| `'r'`      | Read | Fails if the file doesn't exist (`'r'` is the default if the mode is unspecified')|
| `'w'`      | Write | File is created if it doesn't exist. Overwrites existing content if the file already exists. |
| `'a'`      | Append | File is created if it doesn't exist. Adds to the end of existing file.|
| `'r+'`      | Read/write | Open file for reading and writing. Fails if the file doesn't exist.|
| `'w+'`      | Write/read | Writing and reading. Overwrites existing content if the file already exists.|
| `'a+'`      | Append/read | Open file for reading and appending, create file if it doesn't exist.|

## Reading from a text file

There are multiple ways to read text data from a file. These examples assume that the file object `some_file` has already been opened.

- Read the entire contents of the file into one string:

    ```python 
    giant_string = some_file.read()
    ```

- Read the file into a `list` of lines. The contents are broken at each `\n` in the file, and `lines_list` is a list of strings:

    ```python 
    lines_list = some_file.readlines()
    ```

- Read the lines with a loop:

    ```python
    for line in some_file:
        # The variable line (type str) contains the next line in the file
        # Code to process each line goes here
        # You might need to strip the terminating '\n' from each line
        # There might be final empty lines of just '\n'
    ```

- Use a context manager, which combines opening/reading/closing within one organized block. This makes for more readable and organized code and is the preferred technique.

    ```python
    with open(...) as some_file:
        # All code involving the file 'some_file' goes here
    # No need to close file, it is closed automatically at end of indented block
    ```

 ## Closing files

When done reading a file, unless you are using a context manager, always close the file object by calling its `close()` method:
```python
some_file.close()
```
If you don't make a practice of this, you are tying up memory resources. This problem typically doesn't show up until you write larger programs. If you leave too many files unclosed, then your program could slow down or even crash.

Once you call `some_file.close()`, you can no longer read from that file.

## Reading from files without context manager versus with context manager

<table>
<tr><td>No context manager:</td><td>Using context manager:</td></tr>

<tr>
<td nowrap>

```python
a_file = open('foo.txt', 'r')

for line in a_file:
    # process line

a_file.close()
```
</td>
<td nowrap>

```python
with open('foo.txt', 'r') as a_file:
    for line in a_file:
        # process line
# file is closed automatically
```
</td>
</tr>
</table>

## Putting it all together

The code snippets below open a file called `names.txt` that is stored in a directory (folder) called `data_files`. It contains a comma-separated list of names.

In this example, the entire contents of the file are stored in one string.
```python
# open the file names.txt, which is stored in a directory called
# data_files within this working directory. This is a relative path.
a_file = open("data_files/names.txt")
# Read the entire contents of the file into one string
giant_string = a_file.read()
# output the entire contents of the file
print(giant_string)
a_file.close()
```
The output is the entire content of the file `names.txt`, which for the purpose of this example is:
```
Janis Joplin,Aretha Franklin,Pat Benatar,Deborah Harry,Tina Turner,Joan Jett,Stevie Nicks,Melissa Etheridge,Grace Slick,Courtney Love
```

In the following code snippet, the contents of the file are split into a list of separate strings.
```python
a_file = open("data_files/names.txt")
# Read the entire contents of the file into one string, then process that
# list by stripping whitespace from the beginning and end of the string.
# The names are separated by commas, so split them at each comma
# into separate strings
name_list = a_file.read().strip().split(",")
# output the list of names
print(name_list)

# or output the names one at a time:
for name in name_list:
    print(name)
a_file.close()
```
The output for `print(name_list)` is:
```
['Janis Joplin', 'Aretha Franklin', 'Pat Benatar', 'Deborah Harry', 'Tina Turner', 'Joan Jett', 'Stevie Nicks', 'Melissa Etheridge', 'Grace Slick', 'Courtney Love']
```
The output for the for loop is:
```
Janis Joplin
Aretha Franklin
Pat Benatar
Deborah Harry
Tina Turner
Joan Jett
Stevie Nicks
Melissa Etheridge
Grace Slick
Courtney Love
```

The following code snippet shows how to use a context manager to open and read the same file.
```python
# Use a context manager to open and read the file
with open("data_files/names.txt") as a_file:
    # Read the entire contents of the file into one string,
    # then strip white space and split at the commas:
    names_list = a_file.read().strip().split(",")

# Use loop to output names:
for name in names_list:
    print(name)
```

## Processing multi-line files
The following shows the contents of a file `OH_prefs.csv`. This file contains the data for each student of which office hours they are available for.
```
Student name,8AM,9AM,10AM,11AM,12PM,1PM,2PM,3PM,4PM,5PM
Janis Joplin,Y,Y,Y,Y,Y,N,Y,N,Y,Y
Aretha Franklin,Y,Y,Y,Y,Y,N,N,Y,N,Y,Y
Pat Benatar,Y,Y,Y,Y,N,N,Y,N,Y,Y
Deborah Harry,Y,N,Y,Y,N,Y,Y,Y,Y,N
Tina Turner,Y,Y,Y,Y,N,Y,Y,Y,Y,Y
Joan Jett,Y,Y,Y,N,Y,Y,N,Y,N,N
Stevie Nicks,N,Y,Y,Y,Y,Y,N,Y,N,N
Melissa Etheridge,N,N,Y,Y,N,N,Y,N,N,N
Grace Slick,N,N,N,N,N,Y,Y,N,Y,Y
Courtney Love,N,Y,N,N,N,N,Y,N,Y,N
```
Our goal is to read this file and transform it into a list of counts for how many students are available at each office hour. Please use this exercise to practice reading from a file, using lists, as well as algorithmic thinking.

```python
def get_oh_prefs(file_name: str)->list[int]:
    """
    read contents of file file_name and returns a list that contains
    the number of students available at each hour of the day

    parameters:
        filename: file to read (type: str)
    return:
        count of number of students available at each hour (type: list[int])
    """

    # Create a list, initialized with 10 0's
    hours_prefs = []
    for i in range(10):
        hours_prefs.append(0)

    # read the file
    with open(file_name, 'r') as a_file:
        # Each line in the file corresponds to one student
        for line in a_file:
            # student_prefs will contain 'Y's and 'N's
            student_prefs = line.strip().split(",")
            # ignore the first entry in the line, which is the name
            for i in range(1,len(student_prefs)):
                # If they said 'Y', then count them for this time of day
                if student_prefs[i] == 'Y':
                    # Remember that i=0 is the  name
                    hours_prefs[i-1] += 1
    return hours_prefs

def main():
   hours_list = get_oh_prefs('data_files/OH_prefs.csv')
   print(hours_list)

# Run the program:
if __name__ == '__main__':
    main()
``` 