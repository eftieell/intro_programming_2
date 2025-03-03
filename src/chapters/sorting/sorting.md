# Sorting - introduction

If data items are sorted, there is a very fast recursive algorithm (binary search) for locating the item you are looking for. But if data items are unsorted, you have to look at each item, one after the other, to find the item you are looking for. This is much slower. Therefore, we often store data in sorted form. Sorting is essentially important in Computer Science!

In python there are multiple built-in methods/functions to sort data.
* The python list `sort()` method.
* The python `sorted()` function.
* The numpy array `sort()` method.
* The numpy `sorted()` function.

Differences between the above methods/functions:
* `sort()` is a method (called with `listtname.sort()` or `arrayname.sort()`) that sorts the list or array in place (i.e., it modifies the list or array). It returns `None`.
* `sorted()` is a function (called with `sorted(listtname)` or `sorted(arrayname))` that returns a new sorted list (or array), leaving the original unchanged.

## The sort functions/methods we will implement

There are many strategies for sorting data. We will see four sorting algorithms in this course.
You will learn how to implement these first three:
* Selection sort
* Insertion sort
* Bubble sort

These three algorithms rely on nested loops, and are the easiest to learn and understand. So first-year Computer Science students always learn them. But they are also notoriously slow, and so are *never* used in practice!

One exampe of a better sorting algorithm is merge sort. You will see a demo of this fourth algorithm, which relies on recursion. The point of the demonstration is for you to see how much faster it runs than any of the other three algorithms.

There are many other strategies for sorting that you will see in future courses.

## Video explanations
<video src="https://cs.du.edu/~ftl/1352/videos/sorting/sorting_intro.mp4" width="480" height="270" controls></video>
