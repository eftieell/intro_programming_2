# Insertion sort

The final easy-to-implement but notoriously-slow sort algorithm we will study is insertion sort.

Like selection sort and bubble sort, insertion sort also is on average a \\(O(n^2))\\) algorithm. However, insertion sort has some redeeming features:
* It is easy to understand, sorting similarly to how humans would sort a stack of papers or a poker hand.
* Like selection sort and bubble sort, the sorting happens in place. This means it does not use extra memory.
* It is efficient for arrays that are already largely sorted.
* It is stable. This means it does not rearrange elements that have the same value.
* The list can be sorted as it is received (you don't need to have the entire list before you start the sorting process).

## Basic idea of insertion sort
Insertion sort reorders a list in place. The left-hand side of the array is sorted, while the right-hand side is the unsorted portion. With each pass of the sorting process, the cutoff between unsorted and sorted moves to the right. On each pass, consider the next element of the array (the first one in the as-yet-unsorted portion). This element is slid to the left until it is in the correct position.

## Example of sorting an array with the insertion sort algorithm

For example, suppose we start with this array:
```
[8 | 18  6  47  23  7]
```
The vertical bar shows the dividing line between the sorted portion of the list (on the left) and the unsorted portion of the list. There is only one number (8) in the unsorted part of the list. Since there is only one number, it is automatically in the correct order.

### First pass
We now consider the leftmost element of the unsorted portion of the list (18). We slide it left, inserting it in the correct position of the sorted portion. The insertion involves comparing the number to insert (18) to the number on its left, swapping if the number to insert is smaller. This swapping process continues leftward until the number to insert is larger than the number on its left. This time, the first compare shows that 18 > 8, so no swapping is needed at all. Here is the list after this pass:
```
[8  18 | 6  47  23  7]
```

### Second pass
We again look at the leftmost element of the unsorted portion of the list (6). We compare it to the number on its left, and 18 > 6. Thus we swap:
```
[8  6  18 | 47  23  7]
```
Continuing to insert 6 in the correct location, we compare to its neighbor to the left. 8 > 6, so we swap again:
```
[6  8  18 | 47  23  7]
```
The number 6 has been inserted into the left-hand side of the list, so the left portion is fully sorted.

### Third pass
We now insert 47 into the sorted part of the list. Since 18 < 47, no swapping is necessary:
```
[6  8  18  47 | 23  7]
```

### Fourth pass
We now insert 23 into the sorted part of the list. As before, we compare to the number on its left. First 47 > 23, so we swap. Then 18 < 23, so no swap is needed, nor any additional compares.
```
[6  8  18  23  47 | 7]
```

### Last pass
We insert 7 into the sorted part of the list. Notice that 5 compares and 4 swaps are needed to move 7 leftward to its proper position. Comparing to the leftmost element, 6 < 7, shows that the insertion of the final element is complete:
```
[6  7  8  18  23  47]
```
## Online sorting

Notice that if additional data are added after the insertion sort is complete, those elements can be inserted into the list once they are received. This ability to process the values piece-by-piece in a serial fashion is known as "online sorting". Online sorting is useful when data is arriving in a continuous stream, such as a live data stream.

## Time efficiency considerations
While insertion sort is on average a \\(O(n^2)\\), algorithm, if an already-sorted list is processed with insertion sort, the insertion of each new element requires only one compare, and no swapping. Thus, the algorithm runs in \\(O(n)\\) time in this best case scenario. If the list is largely sorted, few extra compares and swaps are needed. So insertion sort is actually an efficient algorithm for lists that are mostly sorted, but have just a few elements out of place.

## Video explanations:
<video src="https://cs.du.edu/~ftl/1352/videos/sorting/insertion_sort.mov" width="480" height="270" controls></video>