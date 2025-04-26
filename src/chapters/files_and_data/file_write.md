## Writing to text files

Text file objects have a method `write(text: str)->int` which writes text to a file and returns the number of characters written.

```python
a_file.open("foo.txt", "w")
a_file.write('some inspiring words \n')
a_file.write('and more inspiring sentences.\n)
```
Unlike python's `print()` function, a newline is not automatically included in a call to `write()`. So the newline must be part of the text you are writing to the file.

Writing to a computer's disk is expensive in run-time, so by default most languages buffer their output (in a temporary list), saving it to write in larger chunks. This means that after a call to `write()`, the data is not yet actually stored in the file. You can request that the program send the buffered data immediately to the disk by calling the `flush()` method.
```python
a_file.flush()
```
When you call `a_file.close()`, the buffer is automatically flushed. So if the text you are writing to a file isn't showing up, check for either a missing call to `flush()` or to `close()`.

## Example
The previous section ended with a program that reads from a file and processes the data, producing  a list of the number of students available for office hours at each hour of the day. We will now extend that program to write the computed results to a file. Examine the contents of the function `write_results_to_file()`. Notice its use of a context manager to write to a file. Notice that each new line is written to the file within a loop. Finally, note that the data will not actually show up in the file until the file is automatically closed at the end of the `with` block (the block that uses a context manager). 

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
        # Read the contents of the header line. We will ignore this line.
        header_line = a_file.readline()
        # Each line in the file corresponds to one student
        for line in a_file:
            # student_prefs will contain 'Y's and 'N's
            student_prefs = line.strip().split(",")
            # ignore the first entry in the line, which is the name of the student
            for i in range(1,len(student_prefs)):
                # If they said 'Y', then count them for this time of day
                if student_prefs[i] == 'Y':
                    # Remember that i=0 is the  name
                    hours_prefs[i-1] += 1
    return hours_prefs

def write_results_to_file(file_name: str, results: list[str])->None:
    hours = ['8AM','9AM','10AM','11AM','12PM','1PM','2PM','3PM','4PM','5PM']
    # open the file for writing
    with open(file_name, "w") as a_file:
        # for each hour of the day, output the time and its student count
        for i in range(len(hours)):
            a_file.write(f"{hours[i]} : {results[i]}\n")


def main():
    hours_list = get_oh_prefs('data_files/OH_prefs.csv')
    write_results_to_file('data_files/OH_results.txt', hours_list)

# Run the program:
if __name__ == '__main__':
    main()
```

Contents of `data_files/OH_prefs.csv` before the program runs:
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
Contents of `data_files/OH_results.txt` after the program has run:
```
8AM : 6
9AM : 7
10AM : 8
11AM : 7
12PM : 4
1PM : 5
2PM : 7
3PM : 5
4PM : 6
5PM : 5

```