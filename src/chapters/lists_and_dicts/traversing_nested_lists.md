# Traversing nested lists (2D lists)

## Background

We generally use nested for-loops to traverse nested lists. You might want to begin by reviewing nested for-loops:
[https://cs.du.edu/~intropython/intro-to-programming/nested_for_loops.html](https://cs.du.edu/~intropython/intro-to-programming/nested_for_loops.html)

Also recall that we learned three ways to traverse 1D lists:
- using a content-based loop
- using an index-based loop
- using the `enumerate()` function

Example of content-based iteration:
```python
# traversing 1D lists, three different ways
cities = ["Denver", "Colorado Springs", "Pueblo"]

# example of a content-based iteration:
for city in cities:
    print(f"I love {city}")
```
Output:
```
I love Denver
I love Colorado Springs
I love Pueblo
```

Example of index-based iteration:
```python
# Example of an index-based iteration:
# Notice that we use the length of the list to tell us when to stop the loop
# Also notice that knowing the index allows us to know when we are on the last one.
# This gives us a way to put the output all on one line by treating the last city differently.
for i in range(len(cities)):
    if i == len(cities) - 1:
        print(f"I love {cities[i]}!")
    else:
        print(f"I love {cities[i]}", end = ", ")
```
Output:
```
I love Denver, I love Colorado Springs, I love Pueblo!
```

Example of using `enumerate()` to track index and value simultaneously:

```python
# example traversing a list using the enumerate() function,
# in which you keep track of index and content at the same time
for i, city in enumerate(cities):
    if i == len(cities) - 1:
        print(f"I love {city}!")
    else:
        print(f"I love {city}", end = ', ')
```
Output:
```
I love Denver, I love Colorado Springs, I love Pueblo!
```

## Loops for traversing 2D lists
Much like with 1D lists, you can traverse 2D lists three ways, 
- using a content-based nested loop
- using an index-based nested loop
- using the `enumerate()` function (access index and content simultaneously)

## Example
Let's traverse the 2D list defined below. Each inner list contains three city names from a given state. Then the outer list is a list of lists of cities from four different states.
```python
more_cities = [
    ["Denver", "Colorado Springs", "Pueblo"],
    ["Los Angeles", "San Diego", "Fresno"],
    ["Chicago", "Springfield", "Champaign"],
    ["Boston", "Worcester", "Springfield"],
]
```
### Content-based traversal of a 2D list:
```python
for row in more_cities:
    for city in row:
        print(f"I love {city}")
```
Output:
```
I love Denver
I love Colorado Springs
I love Pueblo
I love Los Angeles
I love San Diego
I love Fresno
I love Chicago
I love Springfield
I love Champaign
I love Boston
I love Worcester
I love Springfield
```
Notice that each iteration through the outer loop processes one row of the main list (in other words, `row` is one of the inner lists).
So here the variable `row` is itself a list! That's why in the inner loop we can execute another for loop, traversing through
the list `row`. In the inner loop, for each iteration through the loop, city is an entry in the list for that state. 
Giving clear names to the variables is part of documenting your code well.

### Index-based traversal of a 2D list:
```python
for row_index in range(len(more_cities)):
    for col_index in range(len(more_cities[row_index])):
        if col_index == len(row)-1:
            print(f'I love {more_cities[row_index][col_index]}!')
        else:
            print(f'I love {more_cities[row_index][col_index]},', end = " ")
```
Output:
```
I love Denver, I love Colorado Springs, I love Pueblo!
I love Los Angeles, I love San Diego, I love Fresno!
I love Chicago, I love Springfield, I love Champaign!
I love Boston, I love Worcester, I love Springfield!
```
This time the outer loop traverses over each index of rows, meaning `row_index` varies through 0, 1, 2, 3. When `row_index == 0`, we will look at the cities in Colorado, when `row_index == 1`, we will look at the cities in California, when `row_index==2`, we will look at the cities in Illinois, and when `row_index == 3`, we will look at the cities in Massachusetts. For each value of `row_index`, our inner loop has `col_index` taking the values 0, 1 and 2 (one value of `col_index` for each city in that state).
Then inside the two loops, `more_cities[row_index][col_index]` accesses the city name for the relevant row index and column index.

Important note on number of rows and number of columns: `len(more_cities)` gives the number rows. Since `more_cities` is a list of lists, its length is the number of lists (which is the number of rows, or 4). Notice that `more_cities[row_index]` is itself a list (because it is one of the rows). So `len(more_cities[row_index])` gives the number of columns in that row, or 3.

By knowing the index values (rather than just the content stored at each location), we can determine when we are on the last one
(either the last row or the last column). This gives us a way to put all of the cities for each state on one line.

### Using enumerate to traverse a 2D list, keeping track of index and content simultaneously
```python
for row_index, row in enumerate(more_cities):
    for col_index, city in enumerate(row):
        if col_index == len(row)-1:
            print(f'I love {city}!')
        else:
            print(f'I love {city},', end = " ")
```
Output:
```
I love Denver, I love Colorado Springs, I love Pueblo!
I love Los Angeles, I love San Diego, I love Fresno!
I love Chicago, I love Springfield, I love Champaign!
I love Boston, I love Worcester, I love Springfield!
```
Some programmers prefer this method most, since it allows us to know the index value ('row_index' and 'col_index'), but also to have easier access to the value stored there (just `city` instead of `more_cities[row_index][col_index]`).
