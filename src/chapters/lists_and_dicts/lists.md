# Review of python lists

A python list is a built-in data structure that holds an ordered collection of values. 
Python lists are mutable (the contents can be modified after creation), and can store any data type. If the individual elements of a list are each themselves a list, the result is a *nested list* (or *2D list*).
## Creating new lists

There are several ways to create new lists in python:

- List literals: write the comma-separated contents within square brackets, storing the list in a variable:
  
```python
# contents of lists can be any type
greek_letters = ['alpha', 'beta', 'gamma', 'delta']
some_primes = [385351, 217739, 854123, 769733, 898091]
# lists can be nested
scores = [[94, 78, 56], [67, 82, 91]]
```

- Create an empty list, then append elements within a loop:
```python
ten_odds = []
for i in range(10):
    ten_odds.append(2*i+1)
print(ten_odds)  # outputs [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# get input from user, appending each entry into list:
friends = []
num_friends = int(input("How many friends? "))
for i in range(num_friends):
    friend_name = input("Enter a name: ")
    friends.append(friend_name)
print(friends)
```

- Use python's built-in `list()` function (called a 'constructor').
Pass any existing iterable (list, range object, tuple, string, dictionary) as the parameter,
and a new list will be created using its data.
```python
greek_letters = ['alpha', 'beta', 'gamma', 'delta']
# create a new list, a copy of an existing list
copy_of_greek_letters = list(greek_letters)
# changing the copied list does not affect the original
copy_of_greek_letters.append('epsilon')
print(copy_of_greek_letters)  # alpha through epsilon
print(greek_letters) # still just alpha through delta

# create a list of the individual characters in a string
letters = list('haleakala') # letters is now ['h', 'a', 'l', 'e', 'a', 'k', 'a', 'l', 'a']
# create a list from the elements in a range object
values = list(range(1, 10)) # values is now [1, 2, 3, 4, 5, 6, 7, 8, 9]

# create a dictionary literal:
numbers = {1: 'one', 2: 'two', 3: 'three'}
# create a list of the keys from an existing dictionary:
nums = list(numbers.keys())         # nums is [1, 2, 3]
# create a list of the values from an existing dictionary:
num_names = list(numbers.values())  # num_names is ['one', 'two', 'three']
# create a list of the (key, value) tuple pairs from an existing dictionary:
num_items = list(numbers.items())   #num_items is [(1, 'one'), (2, 'two'), (3, 'three')]
```

## Accessing elements in a list
You can access (view or change) each element in a list using its index value 
(the number of its location in the list) within square brackets. For example, `list_name[index]`.

Elements in a list are indexed starting at 0, so `list_name[0]` gives the value of the first element of the list,
and `list_name[i]` gives the value of the i+1st element in the list.

You can find out the number of elements in a python list with `len(list_name)`. 
So the value of the last element of a list is `list_name[len(list_name)-1]`. 
Alternately, in python, you can use an index of -1 for the last element of a list, so `list_name[-1]` is the value of the last element.
(Note that using an index value of -1 is not part of Java or C++, and will result in an index out of bounds error)

```python
languages = ["C++", "python", "Java", "Perl", "JavaScript", "R", "Go", "Rust", "Haskell", "Perl"]

# Access the first element in a list with an index value of 0
# Outputs "I can program in C++""
print(f"I can program in {languages[0]}")

# Access the last element in a list with an index value of len(languages)-1 or -1:
# Both of the next lines output "I can program in Perl"
print(f"I can program in {languages[len(languages)-1]}")
print(f"I can program in {languages[-1]}")

# Lists are mutable, so you can modify the value of an element in the list using its index:
# This changes the first language in the list from "C++" to "C#"
languages[0] = "C#"
```

## Removing elements from a list
There are multiple ways to remove an element from a list in python. Here are two ways:
- Use the `remove()` list method. The parameter you pass is the *value* you want to remove. 
So the `remove()` method traverses through the list until it reaches the *first* instance of the value. That value is then removed from the list.
Details: this method does not return a value. If the value you want to remove is not found in the list, python throws a `ValueError`.

```python
# Remove the first instance of "Perl" from the list
languages.remove("Perl")
```

- Use the `pop()` list method. The parameter you pass is the *index* you want to remove.
Details: the `pop()` method returns the value of the element it removed. If the index you pass as a parameter is invalid, python throws an `IndexError`.

```python
# Remove the index 1 element (2nd element) from the list
removed = languages.pop(1)
print(removed)   # the output is "python", and "python" is no longer in the list
```
- Similar to `pop()`, you can use the `del` keyword to remove an element at a specific index. Details: the value stored at that index is not returned. If the index is invalid, python throws an `IndexError`.
```python
# Remove the index 0 element (first element) from the list
del languages[0]
```

## Traversing lists
You can traverse lists three different ways:
- you can use an index (index-based traversal), or 
- you can traverse directly through the values of the list (content-based traversal), or
- you can traverse using `enumerate()`, which tracks both index and content.

### Example showing three techniques for traversing a list:

```python
# index-based traversal through list:
# Here, i iterates over all indexes in the list (0 through len(languages)-1)
for i in range(len(languages)):
    print(f"I can program in {languages[i]}")

# content-based traversal through list:
# Here, language iterates over all values stored in the list
for language in languages:
    print(f"I can program in {language}")

# traversal through list using enumerate()
# (allows you to track index and value simultaneously)
# Here, one variable (i) holds the index and another (language) holds the value
for i, language in enumerate(languages):
    # Separate the phrases with commas
    if i != len(languages) - 1:
        print(f"I love {language}", end = ', ')
    # when you get to the last language, end sentence with an exclamation point
    else:
        print(f"I love {language}!")
```

Note that above in the use of `enumerate()`, we access the value with the variable `language`.
But instead, since the index is available, we could have used `languages[i]`.

## The `in` keyword
You can use the `in` keyword to determine if a value exists anywhere in the list. It returns a True/False result.
```python
if "Java" in languages:
    print("Java is in the list")
```

## List methods

There is a long list of methods you can use to help you manipulate lists. Please see [Official python documentation on lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) for detailed information.




