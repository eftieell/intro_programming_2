# Numpy arrays

## What is numpy?
Numpy (pronounced "num-pie") is a python library for performing mathematical and numerical operations. 
It is used extensively in scientific computing, data analysis, and machine learning. 
Numpy provides a high-performance, multidimensional array object, and tools for working with these arrays.

To use numpy on your own computer you'll need to install the library. You can do so by running the following python script in VSCode:

```
import sys
import subprocess
subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
import numpy as np
```
Note that you should only need to run this script once. If it successfully installs, you should see no errors.

Once you have successfully installed numpy, the conventonal usage of numpy is to import the module at the beginning of your file like this:
```
import numpy as np
```
We can now use dot-notation on the `np` object to create and interact with numpy arrays. 
In the remainder of this text, we will assume the numpy has been imported with the line above
This means we will use `np` to access all numpy functions.

## Numpy arrays vs. Python lists

A numpy array is similar to a python list in that it is an ordered collection of elements. 
However, numpy arrays are homogeneous, meaning all elements must be of the same type. 
This allows numpy arrays to be more efficient for numerical operations and to use less memory in comparison to python lists.
While this increase in efficiency won't show up for small programs, once you begin doing extensive computations, the
increase in speed is significant.

## There are multiple ways to create numpy arrays

### Creating a numpy array from an existing python list

An existing python list can be used to produce a numpy array using the `np.array()` function:

```
c = np.array([1, 2, 3])
print(type(c))  # outputs "<class 'numpy.ndarray'>"
print(c)        # outputs "[1 2 3]"
```

### Creating a numpy array of a fixed size, contents initialized to 0, or to 1
When you create a numpy array, it's typical to create the entire array at once with a specified size.
This is different from our common strategy of creating an empty python list, then appending elements to it.
While it's possible to create an empty numpy array, and then append to or remove elements from it, for the sake
of efficiency it is far more common for us to create an array of a fixed-size and not to modify its size once
it has been instantiated.
A numpy array is similar to the "array" data type in languages like C/C++/Java. 
Learning to work with numpy arrays will help prepare you to write code in those languages, including systems-level programs.


The `np.zeroes(size: int)` function instantiates a numpy array of the given size, initializing all values to 0.
These values can then be changed later, filling the array with data from some source.

```
a = np.zeros(5) # Create an array of zeros with length 5
print(a)        # outputs [0 0 0 0 0]
```

The `np.ones(size: int)` function instantiates a numpy array of the given size, initializing all values to 1.
```
b = np.ones(10) # Create an array of ones with length 10
print(b)        # outputs [1 1 1 1 1 1 1 1 1 1]
```

The `np.empty(size:int)` function instantiates a numpy array of a given size, without initializing its values.
This means that space in memory is reserved for the array, but whatever values happened to be in memory at
the moment the array was instantiated remain as the values in that array.
```
c = np.empty(3) # Create an array with length 10, contents uninitialized
print(c)        # outputs, for example, [-2.68156159e+154 -2.68156159e+154  4.70372193e+00]
```

Notice that when the contents of a numpy array are output to the terminal, the values are separated just by spaces, not by commas.
This is a visual reminder to you that you are using a numpy array, not a python list.


## Every python array stores one data type (called `dtype`)
The data type (`dtype`) of a numpy array determines the type of elements it can hold. 
Common dtypes include int, float, bool, and string. 
When creating a numpy array, the `dtype` can be specified explicitly, otherwise it is inferred from the input data.
You cannot modify the dtype of a numpy array after it has been instantiated.

Examples:
```
a = np.array([1, 2, 3])      # type is inferred to be an int
print(a.dtype)               # outputs int64
b = np.array([1, 2, 3], dtype = float) # Specifying dtype when creating an array
print(b.dtype)               # outputs float64
c = np.array([1, 2, 3.5])    # the dtype of float is inferred from input data
print(c.dtype)               # outputs float64
d = np.zeros(5)              # np.zeroes by default uses dtype of float
print(d.dtype)               # outputs float64
e = np.zeros(3, dtype = int) # you can specify the dtype
print(e.dtype)               # # outputs int64
```

## Using numpy arrays
Once a numpy array is created, you can access and modify it using indexing and slicing, similar to a python list.
Here are some examples:
```
# instantiate a numpy array, 5 elements, dtype of int
a = np.array([1, 2, 3, 4, 5])

# Accessing elements:
print(a[0])    # use an index to access a single element, outputs 1
print(a[2:4])  # use a slice to access multiple elements, outputs [3 4]

# Modifying elements
a[0] = 0
print(a)  # outputs [0 2 3 4 5]

# Performing operations using functions that are part of numpy
print(np.sum(a))  # outputs 14
print(np.max(a))  # outputs 5
print(np.mean(a)) # outputs 2.8
```

## Matrix operations that are specific to numpy
In addition, many simple matrix-math operations that do not work with lists are possible with numpy arrays.
Operations like addition, subtraction, and multiplication are computed component-wise.

```
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

```
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
