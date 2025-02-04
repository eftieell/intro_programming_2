# Review of python dictionaries

A python dictionary is a built-in data structure that holds (key, value) pairs. The key/value pairs are called *items*.
The purpose of a dictionary is to store these pairs in a way that makes it very efficient to look up the value given the key.
Python dictionaries are mutable (the contents may be modified after creation). 
The keys themselves must be of an immutable type, but the values may be any data type 
(including dictionaries and lists, making for a nested data structure).

## Creating new dictionaries

There are several ways to create new dictionaries:

- Dictionary literals: Each key and value is separated with a colon, while the key:value pairs are separated by commas.
  Then the comma-separated pairs are placed within a pair of curly braces:
  
```python
# dictionary literal for looking up state capitals:
state_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    # etc...
}
```

- Create an empty dictionary, then append elements within a loop (this strategy is especially useful
for building a dictionary from data stored in a file):
```python
student_ids = {}
name = ""
while name != ".":
    name = input("Student name? (Enter . to finish) ")
    if name != ".":
        id = input("Student id? ")
        student_ids[name] = id # this makes name:id be a key:value pair in the dictionary
```

- Create a dictionary using the `dict()` function. This constructor allows you to pass the information in a variety of forms.
```python
# Create a copy of an existing dictionary:
copy_state_capitals = dict(state_capitals)

# Create a dictionary from a list of tuples (each tuple is a key/value pair)
numbers_to_words = dict([(1, 'one'), (2, 'two'), (3, 'three')])

# Create a list of tuples by zipping together two separate lists,
# the first is the list of keys, the second is the matched list of values.
# Then create a dictionary from that zipped list of tuples
numbers_to_words = dict(zip([1, 2, 3], ['one', 'two', 'three']))
```

The number of items (i.e., the number of key/value pairs), is given by `len(dictionary_name)`.

## Looking up values in the dictionary using square brackets or the `get()` method
Given a key, you can look up the associated value in a dictionary using square brackets. 
The keys act much like the index in a list, but they do not have to be integers!
Put the key within square brackets (`dictionary_name[key]`). This expression gives the value associated with that key.

```python
# Using the state_capitals dictionary defined above, this line outputs "Juneau"
print(state_capitals["Alaska"])

# Using the numbers_to_words dictionary created above:
# find out the user's age, then output it in words
age = int(input("How old are you? "))
print(f"You are {numbers_to_words[age]} years old!")
```
Sample output:
```
How old are you? 3
You are three years old!
```

Alternately, you can look up the value associated with a key using the `get()` method. Pass the key as a parameter.
```python
age = int(input("How old are you? "))
print(f"You are {numbers_to_words.get(age)} years old!")
# output is identical to the code above
```

## What if the key you're trying to access isn't in the dictionary?

If you try to access a non-existent key in a dictionary with `dictionary_name[key]`, python crashes with a `KeyError`. 
You can address this issue in multiple ways:
- Use the python dictionary `get()` method. If the key is not found, it will not crash - instead it returns `None`
```python
state = input("What state's capital do you want to know? ")
print(f"The capital of {state} is {state_capitals.get(state)}.")
```
Sample output:
```
What state's capital do you want to know? Minneshota
The capital of Minneshota is None.
```

- Use the `in` keyword to confirm the key is in the dictionary before accessing it:
```python
state = input("What state's capital do you want to know? ")
if state in state_capitals:
    print(f"The capital of {state} is {state_capitals[state]}.")
else:
    print(f"{state} is not a valid state.")
```
Sample output:
```
What state's capital do you want to know? Minneshota
Minneshota is not a valid state.
```

- Use a try/except block to catch the `KeyError` (covered in a later section).

## Modifying elements in a dictionary using square brackets or the `update()` method
By putting `dictionary_name[key]` on the left side of an assignment statement, 
you can change the value associated with that key (if the key is already in the dictionary), 
or create a new item with the given key/value (if the key is not already in the dictionary).
```python
# The key 3 is already in the dictionary, so the next line changes its value
numbers_to_words[3] = 'trois'

# The next line adds a new item into the dictionary, with key 4 and value `four`
numbers_to_words[4] = 'four'
```
Alternately, you can use the `update()` method, particularly if multiple new key/value pairs are to be added at once:
```python
# adds two new key value pairs (5, 'five') and (6, 'six') to the numbers_to_words dictionary
numbers_to_words.update({5: 'five', 6: 'six'})
```

## Removing items from a dictionary using the `pop()` method or the `del` keyword
Use the `pop()` method (pass the key as the parameter) to remove a key/value pair from the dictionary. 
Detail: `pop()` returns the value associated with the deleted key. If the key is not in the dictionary, this call will raise a `KeyError`.
```python
# removes the item ("Alaska", "Juneau") from the state_capitals dictionary
state_capitals.pop("Alaska")
```
Alternately, you can delete an item from a dictionary using the `del` keyword. A `KeyError` is raised if the key is not in the dictionary.
```python
del state_capitals["Alaska"]
```
