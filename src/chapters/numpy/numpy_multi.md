# Two-dimensional and multi-dimensional numpy arrays

A multidimensional array is an array of arrays, in much the same way a multidimensional list is a list of lists. One of Numpy's strengths is the tools it has for making it easier to work with higher-dimensional arrays.

## Creating multi-dimensional numpy arrays from an existing python list

Use the `numpy.array()` function, much like you saw for one-dimensional array, but pass a two-dimensional python list (a list of lists) as the argument. Note: the nested list you pass must be rectangular (not jagged), so it must have the same number of elements in each row.

```python
# Creating a 2D-Numpy array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
```

## The `shape` attribute of an array

 You can find out the number of rows and columns in a multi-dimensional `numpy` array using the `shape` attribute, which is a tuple giving the number of rows, then the number of columns. For example:
 ```python
 arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
 print(arr_2d)
 print(arr_2d.shape).
 ```
Output:
```
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
(4, 3)
```
Notice the following in the above output:
* When you output the contents of a `numpy` array, the rows are each given on a separate line (unlike python lists).
* The shape of the above `numpy` array is (4, 3), since it has 4 rows and 3 columns. Use `arr_2d.shape[0]` and `arr_2d.shape[1]` to individually access the number of rows and number of columns.

## Creating fixed-size multidimensional `numpy` arrays

You can use the `np.zeros()`, `np.ones()`, `np.empty()`, and `np.random.rand()` functions we saw in a previous section to create multidimensional lists. Instead of passing the size (and potentially a `dtype`) as arguments, pass the `shape` (and potentially a `dtype`) as arguments. For example:

```python
arr_zero = np.zeros(shape = (2, 3), dtype = int)
print(arr_zero)
```
Output:
```
[[0 0 0]
 [0 0 0]]
 ```
 The other three commands work analogously.

## Bonus information: `numpy` arrays with three dimensions (or higher)

Though we will not do so in this course, you can create three-dimensional `numpy` arrays or python lists (or even higher dimensions) by increasing the level of nesting. This is not just fun, but also phenomenonally useful in data science, mathematics, physics, geography, and other fields. For example:
```python
# nesting of 2 arrays that are each shape 3x4:
arr_3d = np.zeros(shape = (2, 3, 4), dtype = int)
print(arr_3d)
```
Output:
```
[[[0 0 0 0]
  [0 0 0 0]
  [0 0 0 0]]

 [[0 0 0 0]
  [0 0 0 0]
  [0 0 0 0]]]
```

# Accessing Elements: using comma-based indexing

Recall that for nested python lists, we use a pair of square brackets to indicate *each* index. This notation highlights that a nested list in python is a list of lists.
For example:

```python
# using python lists:
list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# Access the element in row index 0, column index 2:
print(list_2d[0][2]) # Output: 3
```

In contrast, with `numpy` arrays, we use one pair of square brackets, separating the index values with a comma:
```python
# using numpy arrays:
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# Access the element in row index 0, column index 2:
print(arr_2d[0, 2])  # Output: 3
```

To accommodate naive users, python does allow you to use the double-bracket style of indexing even with `numpy` arrays:
```python
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(arr_2d[0, 2])  # Output: 3
print(arr_2d[0][2])  # Also outputs 3, but this style is highly discouraged
```
But you should avoid this syntax for indexing in `numpy` arrays, because with it you lose the efficiency improvement that `numpy` arrays provide over python lists.

## Slicing `numpy` arrays

Slicing in `numpy` arrays is more powerful than in python lists, since it allows you to slice along columns in addition to rows. For example, the following code allows you to create a `numpy` array from a single column of a 2D array. This allows you to do numerical computations on individual rows and columns much more fluidly!

```python
# Create a 2D Numpy array
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])

# Access a single column of the Numpy array
numpy_column = arr[:, 1] # include all the rows, and only the second column (index 1 column)
# Compute and output the sum of the individual column:
print(sum(numpy_column))
```

Compare the above to the analogous code using python lists
```python
# Create a 2D Python list
lst = [[1,2,3], [4,5,6], [7,8,9]]

# Access a single column of the Python list
python_column = [row[1] for row in lst] # iterate over the rows grabbing the second column
print(python_column)
print(sum(python_column))
```


