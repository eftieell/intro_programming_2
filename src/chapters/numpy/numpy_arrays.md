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

## Creating numpy arrays - multiple options

### Creating a numpy array from an existing python list

An existing python list can be used to produce a numpy array using the `np.array()` function:

```
c = np.array([1, 2, 3])
print(type(c))  # outputs "<class 'numpy.ndarray'>"
print(c)        # outputs "[1 2 3]"
```

### Creating a numpy array of a fixed size
When you create a numpy array, it's typical to create the entire array at once with a specified size.
This is different from our common strategy of creating an empty python list, then appending elements to it.
While it's possible to create an empty numpy array, and then append to or remove elements from it, for the sake
of efficiency it is far more common for us to create an array of a fixed-size and not to modify its size once
it has been instantiated.
A numpy array is similar to the "array" data type in languages like C/C++/Java. 
Learning to work with numpy arrays will help prepare you to write code in those languages, including systems-level programs.

Below you'll see four `np` functions for creating arrays:

* The `np.zeros(size: int)` function instantiates a numpy array of the given size, initializing all values to 0.
These values can then be changed later, filling the array with data from some source.

```python
a = np.zeros(5) # Create an array of zeros with length 5
print(a)        # outputs [0 0 0 0 0]
```

* The `np.ones(size: int)` function instantiates a numpy array of the given size, initializing all values to 1.
```python
b = np.ones(10) # Create an array of ones with length 10
print(b)        # outputs [1 1 1 1 1 1 1 1 1 1]
```

* The `np.empty(size:int)` function instantiates a numpy array of a given size, without initializing its values.
This means that space in memory is reserved for the array, but whatever values happened to be in memory at
the moment the array was instantiated remain as the values in that array.
```python
d = np.empty(3) # Create an array with length 10, contents uninitialized
print(d)        # outputs, for example, [-2.68156159e+154 -2.68156159e+154  4.70372193e+00]
```

* The `np.random.rand(size:int)` method instantiates a numpy array of a given size, initialized with random values in the interval [0,1).
```python
e = np.random.rand(4). # Create an array with 4 random values
print(e)               # outputs, for example, [0.04434599 0.71186025 0.14798285 0.96437171]
```

Notice that when the contents of a numpy array are output to the terminal, the values are separated just by spaces, not by commas.
This is a visual reminder to you that you are using a numpy array, not a python list.

## Use the `size` attribute to find the size of an existing numpy array.

Numpy arrays have a `size` attribute, which gives the total number of elements in the array:
```python
f = np.array([5, 0, -5])
print(f.size)  # outputs 3
```

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
d = np.zeros(5)              # np.zeros by default uses dtype of float
print(d.dtype)               # outputs float64
e = np.zeros(3, dtype = int) # you can specify the dtype
print(e.dtype)               # outputs int64
```

In numpy arrays, the type `int64` has a fixed size of 64 bits (8 bytes). This means that the integers that can be stored have a minimum value of -9,223,372,036,854,775,808 and a maximum value of 9,223,372,036,854,775,807 (inclusive). This is unlike the python `int` type, which can hold to an unlimited value, increasing behind the scenes the storage space used to store the number.

## Video explanations:
<video src="https://cs.du.edu/~ftl/1352/videos/numpy/numpy_arrays.mp4" width="480" height="270" controls></video>
