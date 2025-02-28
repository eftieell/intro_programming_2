# Computation using numpy arrays

Once a numpy array is created, you can access and modify it using indexing and slicing, similar to a python list.
Here are some examples:
```python
import numpy as np
# instantiate a numpy array, 10 elements, dtype of float64
a = np.empty(10)

# access elements in an array using the index values
# initialize the contents  using a loop
for i in range(a.size):
    a[i] = i+1
print(a) # outputs [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

# Indexes and slices:
print(a[0])    # use an index to access a single element, outputs 1.0
print(a[2:4])  # use a slice to access multiple elements, outputs [3. 4.]

# Modifying elements
a[0] = 0
print(a)  # output [ 0.  2.  3.  4.  5.  6.  7.  8.  9. 10.]


# Performing operations using functions that are part of numpy
print(np.sum(a))  # outputs 54.0
print(np.max(a))  # outputs 10.0
print(np.min(a))  # outputs 0.0
print(np.mean(a)) # outputs 5.4
```

## Matrix operations that are specific to numpy
In addition, many simple matrix-math operations that do not work with lists are possible with numpy arrays.
Operations like addition, subtraction, and multiplication are computed component-wise.

```python
# instantiate a numpy array
b = np.array([1, 2, 3])

# addition: the constant 2 is added to every element in b, producing a new numpy array
print(b + 2)  # outputs "[3 4 5]"

# subtraction
print(b - 2)  # outputs "[-1  0  1]"

# multiplication - the constant 2 is multiplied by every element in b, producing a new numpy array
print(b * 2)  # outputs "[2 4 6]"
```

If we combine two arrays using a mathematical operator such as addition, 
then the result is a new array, whose elements are computed by individually adding the corresponding elements in the two arrays.

```python
# addition
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)  # outputs "[5 7 9]"

# subtraction
d = b - a
print(d)  # outputs "[3 3 3]"

# multiplication
e = a * b
print(e)  # outputs "[4 10 18]"
```

## Video explanations:
<video src="https://cs.du.edu/~ftl/1352/videos/numpy/numpy_computation.mp4" width="480" height="270" controls></video>
