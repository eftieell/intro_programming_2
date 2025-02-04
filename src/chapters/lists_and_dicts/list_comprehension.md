# List Comprehension

List comprehension is a convenient strategy built into python for creating lists by manipulating existing 
lists, range objects, or other iterable objects. (Note that list comprehension is not part of Java or C++,
but you will see it again in other functional programming languages.)

The idea of list comprehension is to include the definition of a loop within the one line that creates the list.

### Example 1

Here is some code that creates a list of the first ten positive odd integers:
```python
ten_odds = []
for i in range(10):
    ten_odds.append(2*i+1)
```
Notice that the expression `2*i+1` gives the values to append to the list,
while the code `for i in range(10)` gives the values to use for the variable `i`. In list comprehension, 
both of these are embedded into the one-line definition of the list. The line below creates
the identical list:
```python
ten_odds = [2*i+1 for i in range(10)]
```

## Generate new lists using any iterable object

The examples below demonstrate that you can use list comprehension to create new lists, by traversing any iterable object.

### Example 2
Consider this list:
```python
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```
That sam list can be defined more robustly using list comprehension:

```python
digits = [str(i) for i in range(10)]
```
With practice, you'll use list-comprehension creatively in a wide variety of applications.

### Example 3
You can create lists using list comprehension by looping over *any* iterable object. Here we iterate over an existing list:
```python
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
primes_squared = [prime*prime for prime in primes]
```
For reference, here is the code that accomplishes the same task using a for-loop:
```python
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
primes_squared = []
for prime in primes:
    primes_squared.append(prime*prime)
```

### Example 4
You can break a string into a list of its individual characters:
```python
letters = [character for character in 'Hello, World']
# letters = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd']
```

### Example 5
You can create a list from an existing dictionary's keys, or values:
```python
us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    # etc...
}
# state_names is a list of all of the state names (a list of the keys extracted from us_state_to_abbrev dictionary)
state_names = [state_name for state_name in us_state_to_abbrev.keys()]
# abbreviations is a list of all of the state abbreviations (a list of the values extracted from us_state_to_abbrev dictionary)
abbreviations = [abbrev for abbrev in us_state_to_abbrev.values()]
```
## List Comprehension and conditionals
We've seen list comprehension of the form

**new_list = [*value* for *variable* in *iterable*]**

Now we'll add a conditional (an if-clause) to restrict some of the values from being included in the list:

**new_list = [*value* for *variable* in *iterable* if *conditional_expression*]**

### Example 6
Yet another strategy for producing a list of the first ten odd numbers:
```python
ten_odds = [i for i in range(20) if i%2==1]
```

### Example 7
Extract all of the upper-case letters from an existing string:
```python
letters = [character for character in 'Hello, World' if character.isupper()]
# letters = ['H', 'W']
```

### Example 8
A more involved example, extracting from the state-to-abbreviations dictionary all state abbreviations that start with a vowel.
```python
us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    # etc...
}
vowel_abbrev = [abbrev for abbrev in us_state_to_abbrev.values() if abbrev[0].lower() in "aeiou"]
# vowel_abbrev = ['AL', 'AK', 'AZ', 'AR', 'ID', 'IL', 'IN', 'IA', 'OH', 'OK', 'OR', 'UT']
```
## Nested loops in list comprehension
The iteration within a list comprehension can be a nested loop:
```python
digits = ['1', '2', '3']
letters = ['a', 'b', 'c']
new_list1 = [digit + letter for digit in digits for letter in letters]
# new_list1 = ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
```
Note that the nested loop above does *not* create a nested list - it is still a 1D list, constructed with a nested loop.

As always with nested loops, it matters which loop is on the outside. 
In the above example, the first for statement (`for digit in digits`) is the outside loop,
while the second for statement (`for letter in letters`) is the inside loop.
This means that we start with the first element in the outside loop (`digit = '1'`), and entirely complete
the inside loop (`for letter in letters`) before proceeding to the next element in the outside loop (`digit = '2'`).
After completing the inside loop (`for letter in letters`) entirely with `digit = '2'`, we then move to the next element
of the outer loop (`digit = '3'`).
This explains the order that the elements are appended to the list (all of the 1s, then all of the 2s then all of the 3s): `new_list1 = ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']`.

Notice what happens when we switch the order of the two for-loops. 
```python
digits = ['1', '2', '3']
letters = ['a', 'b', 'c']
new_list2 = [digit + letter for letter in letters for digit in digits]
# new_list2 = ['1a', '2a', '3a', '1b', '2b', '3b', '1c', '2c', '3c']
```
The outer for-loop is now `for letter in letters` and the
inner for-loop is now `for digit in digits`. This means that elements using `letter = 'a'` are all appended before moving on to
all elements using `letter = 'b'`, and finally all elements using `letter = c`. 
The list therefore starts with all the 'a's, then all the 'b's, then all the 'c's: `new_list2 = ['1a', '2a', '3a', '1b', '2b', '3b', '1c', '2c', '3c']`

## Creating nested lists with a 2D list comprehension
You can also use list comprehension to create nested lists. At first the syntax seems similar to list comprehension with nested loops,
but notice the all-important extra set of list brackets (`[]`):
```python
digits = ['1', '2', '3']
letters = ['a', 'b', 'c']
nested_list = [[digit + letter for letter in letters] for digit in digits]
# nested_list = [['1a', '1b', '1c'], ['2a', '2b', '2c'], ['3a', '3b', '3c']]
```
Here we have a list comprehension with the loop `for digit in digits`. For each of those digits, an entire list is created,
resulting in a list of lists. Each internal list is itself created with a list comprehension (`[digit + letter for letter in letters]`)
So we have a nested list-comprehension (not a list comprehension with nested loops). The makes the result a nested list. 
(`nested_list = [['1a', '1b', '1c'], ['2a', '2b', '2c'], ['3a', '3b', '3c']]`).




