# Nested data structures

Data structures can be nested in a variety of ways. We've seen examples of nested lists (lists of lists).
But you can also create lists of dictionaries, dictionaries whose values are lists, or dictionaries whose values are dictionaries.
This section gives you some examples of these structures, and how to traverse them in useful ways.

## Example of a list of dictionaries
Here's an example of a list, each element of which is a dictionary. Try to understand what the meaning and use of this list is.
```python
payroll  = [
    {"first_name": "Logan", "last_name": "Aster", "wage": 15.70, "hours": 37},
    {"first_name": "Apurva", "last_name": "Lennie", "wage": 24.00, "hours": 15},
    {"first_name": "Noel", "last_name": "Kingsley", "wage": 22.50, "hours": 25},
]
```
This list is used by a payroll department. Each element of the list is a dictionary that contains the pay data for a single employee.

Try the following exercises (there are multiple ways to solve each question!)
1. Output the wage of the second person in the list (index 1)
2. Create a list of last names
3. Output the total pay for a person whose last name is "Kingsley"
4. Find the total dollar amount to be paid to all employees

Solutions:
1. Output the wage of the second person in the list (index 1)
```python
print(payroll[1]['wage'])
```

2. Create a list of last names
```python
   last_names = []
   for i in range(len(payroll)):
       last_names.append(payroll[i]['last_name'])
```
or
```python
    last_names = [payroll[i]['last_name'] for i in range(len(payroll))]
```
or
```python
    last_names = [employee['last_name'] for employee in payroll]
```

3. Output the total pay for a person whose last name is "Kingsley"
```python
   for employee in payroll:
       if employee['last_name'] == 'Kingsley':
           print(f"{employee['wage']*employee['hours']:.2f}")
```

4. Find the total dollar amount to be paid to all employees
```python
   total = 0
   for i in range(len(payroll)):
       total += payroll[i]['wage']*payroll[i]['hours']
   print(f"{total:.2f}")
```

## Example of a dictionary with lists as values
Suppose we have a table of quiz scores for students in a course.

| Student | Quiz 1  | Quiz 2 | Quiz 3 | Quiz 4 |
| --- | --- | --- | --- | --- |
| Alice | 78 | 83 | 62 | 91 |
| Bob | 93 | 69 | 88 | 72 |
| Charlie | 75 | 82 | 78 | 83 |

One way to store this data is to use a dictionary where the key is the name of the student, and the value is a list of their scores.
```python
scores = {
    'Alice': [78, 83, 62, 91],
    'Bob':[93, 69, 88, 72],
    'Charlie': [75, 82, 78, 83],
}
```
Exercises:
1. What type is the expression `scores['Alice']`

Answer: It is a list!

2. What is output by `print(scores['Alice'])`?

Answer: `[78, 83, 62, 91]`

3. What is output by `print(scores['Alice'][1])`?

Answer: `83`

4. What expression will tell you how many scores Bob has?

Answer: `len(scores['Bob'])`

5. What expression will give Charlie's last score?

Answer: `scores['Charlie'][-1]` or `scores['Charlie'][len(scores['Charlie'])-1]`

6. How do you find the average of Bob's scores?

Answer:
```python
total = 0
for score in scores['Charlie']:
    total += score
average = total/len(scores['Charlie'])
```
or
`average = sum(scores['Charlie'])/len(scores['Charlie'])`


## Example of a dictionary of dictionaries
Here is a dictionary, where each key is a state abbreviation. The value for each state is a dictionary with (city name/population) as (key,value) pairs.
```python
populations = {
    "CO": {"Denver": 2897000, "Colorado Springs": 488664, "Pueblo": 111424},
    "IL": {"Chicago": 8901000, "Springfield": 205519, "Champaign": 88343},
    "CA": {"Los Angeles": 12488000, "San Diego": 3295000, "Fresno": 795000},
    "MA": {"Boston": 653833, "Worcester": 207621, "Springfield": 153672 }
}
```
The keys for the `populations` dictionary are "CO", "IL", "CA", and "MA". The expression `populations["CA"]` evaluates to an
entire dictionary, which can itself be indexed with its keys "Los Angeles", "San Diego", and "Fresno". Thus the expression
`populations["CA"]["Los Angeles"]` evaluates to 12488000. Since the dictionary is nested, we need two index values to access the lowest level of data.

Try the following exercises (there are multiple ways to solve each question!)
1. Ask the user for a state abbreviation and city name, and output the population
2. Output all of the state abbreviations on one line
3. Output all 12 of the city names on one line
4. Find the total population of the listed Colorado cities
5. Find the total population of all 12 cities
6. Flatten the structure into a single dictionary where the keys of the form "Denver, CO", and the values are the corresponding population

Solutions:

1. Ask the user for a state abbreviation and city name, and output the population:
```python
state = input("Enter the state abbreviation: ")
city = input ("Enter the city name: ")
# Note that this code is flawed, since it does not error checking. The program
# will crash if the user enters an invalid state or an invalid city.
print(f"The population of {city}, {state} is {populations[state][city]}")
```

2. Output all of the state abbreviations on one line
```python
# Recall that iterating through a dictionary means iterating through the keys.
# So state iterates over the values "CO", "IL", "CA", "MA"  
for state in populations:
    print(state, end = " ")
print()
```

3. Output all 12 of the city names on one line
```python
for state in populations:
    for city in populations[state]:
        print(city, end= " ")
print()
```

4. Find the total population of the listed Colorado cities
```python
total = 0
for city in populations["CO"]:
    total += populations["CO"][city]
print(total)
```

5. Find the total population of all 12 cities
```python
total = 0
for state in populations:
    for city in populations[state]:
        total += populations[state][city]
print(total)
```

6. Flatten the structure into a single dictionary where the keys of the form "Denver, CO", and the values are the corresponding population
```python
flat_populations = {}
for state in populations:
    for city in populations[state]:
        flat_populations[city + ", " + state] = populations[state][city]
```
Note that it would not have worked to create one dictionary with just the city names and corresponding populations. Keys must be unique - but there are two cities with the same name! So adding the second "Springfield" to the dictionary would have overwritten the first "Springfield". Cities within states though, are required to have distinct names (you can't have two towns named Springfield within the same state), so we didn't run into this issue with our original structure. This is why the question asked you to produce a new key, that included the name of the city together with the state abbreviation.

One subtle point in the above code is the creation of that new key. The expression `city + ", " + state` is a string concatenation, building the name in the form "city, state".
