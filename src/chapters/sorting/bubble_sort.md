# Bubble Sort

A second easy-to-implement but unusably-slow sort algorithm is bubble sort.

Here's the idea behind bubble sort: for the first pass, iterate over the array, on each iteration checking *adjacent* pairs of values. If the values are in the correct order, we don't have to do anything. If they are in the wrong order, swap them. Therefore, on one pass over the array, we will have guaranteed that the maximum element is at the end of the array. The algorithm is called "bubble sort" because you can imagine that on this first pass, the highest value has bubbled up through the array to its rightful last position in the array. Now repeat the process: the second pass "bubbles" the second-largest value to the second-to-last position in the array. Each subsequent pass takes the next-highest value to its correct position in the array. If the array has length n, then n-1 passes are needed.

For example, consider the array
```
[12  5  7  3]
```
**First pass**: We iterate over the array, comparing each element to the one *following* it, swapping if necessary. 

* First compare the value at index 0 to the value at index 1. Since 12 > 5, the two values are swapped:
```
[5  12  7, 3]
```

* Now compare the value at index 1 to the value at index 2. Since 12 > 7, the two values are swapped:
```
[5  7  12  3]
```
* Now compare the value at index 2 to the value at index 3. Since 12 > 3, the two values are swapped:
```
[5  7  3  12]
```

This is the end of the first pass. We see that 12 has bubbled up to its final position.

**Second pass**: We iterate again over the array exactly as before. Note that we don't need the last compare, since 12 is already guaranteed to be in its correct position. We will compare values at index 0 and 1, then values at index 1 and 2.
* Comparing values at index 0 and index 1, since 5 < 7, no swap is performed, and the array stays as-is.
* Comparing values at index 1 and index 2, since 7 > 3, the two values are swapped:
```
[5  3  7  12]
```
This is the end of the second pass. Now 7 and 12 have both bubbled to their final positions.

**Third pass**: We iterate again over the array, this time stopping before comparing to either of the last two elements. This means just one compare and potential swap is needed.
* Comparing values at index 0 and index 1, since 5 > 3, the two values are swapped:
```
[3  5  7  12]
```

The array has 4 elements, so 3 passes are needed. At the end of the third pass, the array is completely sorted.

## Timing running of bubble sort
Timing of running of bubble sort, as we did with selection sort, suggests that bubble sort is also a \\(O(n^2)\\)algorithm, and thus, like selection sort, is *never* used in practice. In the first Data Structures and Algorithms course, you will learn how to determine the runtime of algorithms more completely using both experimental analysis and theoretical analysis.