# Data Science, and reading `.csv` files

Python is becoming an increasingly popular choice for many applications, but in particular it has become one of the standards in the field of Data Science.

Often data scientists will open and read a `.csv` file (comma-separated values file) to pull data into a python program. Comma-separated values files (`.csv` files) follow a simple table format, and the python `csv` module has functionality that can make make it easy to open and read these files in a python program. A couple of ways to use the `csv` module are described below.

## Tabular Data

First, let's focus on a common data format known as "tabular data". This means data that is best represented as a table. You have seen this type of data in Excel spreadsheets or Google Sheets. The table represents a collection of "items" of the same type. Each row represents one "item", and each column is an attribute of that "item". The first row is a header that gives a title to each attribute. For example:

| **Name** | **Age** | **Favorite Icecream** |
| --- | --- | --- |
| Bob | 24 | Chocolate |
| Alice | 31 | Vanilla |
| John | 48 | Strawberry |

Above we see a spreadsheet of "people", where each row is a "person", and each column is an attribute of that person.

There are many different ways of working with tabular data (storing it, reading it, modifying it, analyzing it). We will see two ways to store tabular data, first using a list of lists, and second using a list of dictionaries.

---

## `.csv` files (Comma-Separated Values)

The simplest way of representing a table is to just put it in a text file. One common format is a comma-separated-values (`.csv`) file.

Each row of text will represent one item, where the attributes of that item are separated by commas. Typically, the first row of text in the file will be the names of the columns (i.e., the attributes):

```
name,age,fav_icecream
Bob,24,chocolate
Alice,31,vanilla
John,48,strawberry
```

Note: sometimes this can be hard to read visually due to the uneven width of the columns. If you're using VSCode (or a similar tool) you can install add-ons that color your table to make the columns clearer (or add spacing to align them).

### Opening and reading a `csv` file in a python program - method 1
Since a `.csv` file is just a text file, we can read it as we would normally read any text file in Python (with the open() function). But turning that text into other data structures (lists/dictionaries) is so common that Python has a built-in `csv` reader. For example, here's one way to open and read a file using the `csv` module:

```python
import csv

with open('mydata.csv') as csvfile:
    rows = csv.reader(csvfile)
    for r in rows:
        print(r)
        # each row r is a list of the values
        # [value1, value2, ...]
```

Output:
```
['name', 'age', 'fav_icecream']
['Bob', '24', 'chocolate']
['Alice', '31', 'vanilla']
['John', '48', 'strawberry']
```


The short code segment above opens the `.csv` file and creates a **list of lists** containing the data in the file.

NOTE: You can also read files with separators other than a comma:

```python
rows = csv.reader(csvfile, delimiter=';')
```

### Opening and reading a CSV file in a python program - method 2

The python `csv` module also allows us to efficiently open and read a file into a dictionary format:

```python
with open('mydata.csv') as csvfile:
    # here's the powerful step that uses the machinery of the csv module:
    rows = list(csv.DictReader(csvfile))
    for r in rows:
        print(r)
        # r is now a dictionary!
        # { column_name: attribute, ... }
```

Output:
```
{'name': 'Bob', 'age': '24', 'fav_icecream': 'chocolate'}
{'name': 'Alice', 'age': '31', 'fav_icecream': 'vanilla'}
{'name': 'John', 'age': '48', 'fav_icecream': 'strawberry'}
```
The short code segment above opens the `.csv` file and creates a **list of dictionaries**. Each dictionary in the list represents one full "Person", with all of their attributes.


## Another example
Recall the following file from previous sections ([Opening, closing and reading from files](file_open_read_close.md) and [Writing to files](file_write.md)), giving data of each student's availability for office hours:
```
Student name,8AM,9AM,10AM,11AM,12PM,1PM,2PM,3PM,4PM,5PM
Janis Joplin,Y,Y,Y,Y,Y,N,Y,N,Y,Y
Aretha Franklin,Y,Y,Y,Y,Y,N,N,Y,N,Y
Pat Benatar,Y,Y,Y,Y,N,N,Y,N,Y,Y
Deborah Harry,Y,N,Y,Y,N,Y,Y,Y,Y,N
Tina Turner,Y,Y,Y,Y,N,Y,Y,Y,Y,Y
Joan Jett,Y,Y,Y,N,Y,Y,N,Y,N,N
Stevie Nicks,N,Y,Y,Y,Y,Y,N,Y,N,N
Melissa Etheridge,N,N,Y,Y,N,N,Y,N,N,N
Grace Slick,N,N,N,N,N,Y,Y,N,Y,Y
Courtney Love,N,Y,N,N,N,N,Y,N,Y,N
```
Instead of reading and processing each line of code as we did in a previous section, we will use the `csv` module to create a list of dictionaries for each student's data:
```python
with open('OH_prefs.csv') as prefs_file:
    prefs = list(csv.DictReader(prefs_file))
# prefs is a list of dictionaries:
for student in prefs:
    print(student)
```

Output:
```
{'Student name': 'Janis Joplin', '8AM': 'Y', '9AM': 'Y', '10AM': 'Y', '11AM': 'Y', '12PM': 'Y', '1PM': 'N', '2PM': 'Y', '3PM': 'N', '4PM': 'Y', '5PM': 'Y'}
{'Student name': 'Aretha Franklin', '8AM': 'Y', '9AM': 'Y', '10AM': 'Y', '11AM': 'Y', '12PM': 'Y', '1PM': 'N', '2PM': 'N', '3PM': 'Y', '4PM': 'N', '5PM': 'Y', None: ['Y']}
etc...
```
Now that the data is stored in this list of dictionaries, we can traverse the list to count the students available at each office hours much more easily (Compare to the code in [Writing to files](file_write.md)):
```python
# Create a dictionary to store the count of students available at each hour:
student_counter = {}
# Loop through each student, and for each time in their dictionary,
# if they said 'Y' to that time, add it to the counter for that hour
for student in prefs:
    for time in student:
        if student[time] == 'Y':
            if time in student_counter:
                student_counter[time] += 1
            else:
                student_counter[time] = 1
print(student_counter)
```

Output:
```
{'8AM': 6, '9AM': 7, '10AM': 8, '11AM': 7, '12PM': 4, '2PM': 7, '4PM': 6, '5PM': 5, '3PM': 5, '1PM': 5}
```
