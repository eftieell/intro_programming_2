# Selection sort
Selection sort is a notoriously inefficient sorting algorithm, but easier to understand than efficient strategies that you will learn in later courses. That's why it's frequently taught to first-year Computer Science students as a great application of nested loops.

The strategy of selection sort is to reorder the array in place by repeatedly selecting the smallest remaining element in an array, then swapping it with the value in the first unsorted position of the array.

## First pass
The first pass of the algorithm performs these tasks:
* Traverse the array with a for-loop, determining the index of the smallest value in the entire array.
* Swap that value with the first element (index 0 value) in the array.

For example, suppose that the array starts with the following contents:
```python
[8, 18, 6, 47, 23, 7]
```
In the first pass, we determine that the minimum value is 6, located at index 2. Here is a sample of code that will find this information:
```python
min_index = 0
for i in range(arr.size):
    if arr[i] < arr[min_index]:
        min_index = i
```
At the end of execution, `min_index` is 2, and the minimum value of 6 is stored at `arr[min_index]`.
This tells us to swap the value stored at position 0 (an 8) with the value stored at position `min_index` (a 6). Here's the code that performs the swap:
```python
temp = arr[min_index]
arr[min_index] = arr[0]
arr[0] = temp
```
When the first pass is complete, the contents of the array are:
```
[6, 18, 8, 47, 23, 7]
```
At this point, the first element of the array is considered sorted, since it contains the final value that belongs at that position.

## Second pass
The second pass of the algorithm performs the following tasks:
* Traverse the array with a for-loop, starting at the second element (index 1), locating the second-smallest element.
* Swap that value with the second element in the array (index 1 element).

Here's the code that performs these two tasks. Notice what is different in this code from the first pass: we start with `min_index` as 1, the first position in the *unsorted* part of the array. Then when searching for the next-smallest value, the search begins not at index 0, but at index 1, the first position in the unsorted part of the array. Finally, in the swap, the value in `arr[1]` is swapped with the value at `min_index`
```python
min_index = 1
for i in range(1, arr.size):
    if arr[i] < arr[min_index]:
        min_index = i
temp = arr[min_index]
arr[min_index] = arr[1]
arr[1] = temp
```
After the second pass, the first two positions are finalized, and the contents of the array are:
```python
[6, 7, 8, 47, 23, 18]
```

## Subsequent passes
Realize that each pass through the array chooses the next-smallest element in the unsorted part of the array, and swaps that value with the next position in the array. If we create a variable `pass_number`, and have it take values from 0 to the last index in the array, then here is the code for finding the index of the next-smallest value, then swapping that value into its correct position:
```python
min_index = pass_number
for i in range(pass_number, arr.size):
    if arr[i] < arr[min_index]:
        min_index = i
temp = arr[min_index]
arr[min_index] = arr[pass_number]
arr[pass_number] = temp
```

To complete the implementation of selection sort, we just need to place this code block within a for-loop that traverses all possible values for `pass_number`. Notice that we stop `pass_number` one before the last index, since once the second-to-last value is in its correct position, the last value must be the largest element in the array.
```python
# selection sort:
def selection_sort(arr):
    for pass_number in range(arr.size-1):
        # one pass of selection sort follows.
        # first find the index of the next-smallest number:
        min_index = pass_number
        for i in range(pass_number, arr.size):
            if arr[i] < arr[min_index]:
                min_index = i
        # swap minimum of unsorted part of array with the next spot to be sorted:
        temp = arr[min_index]
        arr[min_index] = arr[pass_number]
        arr[pass_number] = temp

# main code block, small test of the selection sort function:
rand_arr = np.random.rand(10)
selection_sort(rand_arr)
print(rand_arr)
```

## Timing running of selection sort

If you need a refresher on how to time the runnning of functions, see [measuring runtime for functions](../functions/experimental_runtime.md)

The code below times how long it takes for selection sort to run with an array size of 5000:
```python
import time
rand_arr = np.random.rand(5000)
start = time.time()
selection_sort(rand_arr)
stop = time.time()
print(f"Elapsed time for array with 5000 elements: {stop-start:0.2f} seconds")
```

Sample output:
```
Elapsed time for array with 5000 elements: 1.48 seconds
```

Recall that one way to understand how fast the elapsed time for running this function grows as we increase the size of the array is to double the size of the array to see what happens to the runtime:

```python
rand_arr = np.random.rand(10000)
start = time.time()
selection_sort(rand_arr)
stop = time.time()
```

Sample output:
```
Elapsed time for array with 10000 elements: 5.73 seconds
```
When we doubled the size of the array, the time quadrupled. This significant effect on the runtime as the size of the array increases follows the pattern of \\(O(n^2)\\) algorithms. It is the \\(O(n^2)\\ runtime is what makes selection sort so devastatingly slow for large arrays.

In the first Data Structures and Algorithms course, you will learn how to determine the runtime of algorithms more completely using both experimental analysis and theoretical analysis.

## Video explanations:
Part 1:

<video src="https://cs.du.edu/~ftl/1352/videos/sorting/select_sort_part1.mp4" width="480" height="270" controls></video>

Part 2:

<video src="https://cs.du.edu/~ftl/1352/videos/sorting/select_sort_part2.mp4" width="480" height="270" controls></video>






