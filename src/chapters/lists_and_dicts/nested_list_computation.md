# Computation traversing nested lists

If we have a 2D list of numbers, we might be interested in doing computations on the numbers in the list.
- We can compute the sum, maximum, or average of all elements in the 2D list.
- We can compute the sum, maximum, or average of a specific row.
- We can compute the sum,  max/min, or average of a specific column.
- We can compute the sum, max/min, or average of each row.
- We can compute the sum,  max/min, or average of each column



The code needed to compute each of these differs in subtle, but very important ways.
We'll demonstrate this with an example.

Suppose we have a table of quiz scores for students in a course.

| Student | Quiz 1  | Quiz 2 | Quiz 3 | Quiz 4 |
| --- | --- | --- | --- | --- |
| Student 1 | 78 | 83 | 62 | 91 |
| Student 2 | 93 | 69 | 88 | 72 |
| Student 3 | 75 | 82 | 78 | 83 |

The scores are stored in this 2D list:
```python
scores = [
    [78, 83, 62, 91],
    [93, 69, 88, 72],
    [75, 82, 78, 83],
]
```

### Compute a quantity for the entire 2D list
We want to compute a quantity using all 12 elements in the 3x4 matrix. This requires us to traverse through every element
in the 2D list. We've seen previously multiple ways to do this (index-based traversal, content-based traversal, or using `enumerate()`).
We review the process with the code below, which finds the maximum value of all 12 scores in the 2D list, using index-based loops.
Notice that in this code block, the outer loop iterates over each row index, while the inner loop iterates over each column index.
This means that we visit each list element in row-major order. In other words, we first traverse every element in the first row, then every element
in the second row, then every element in the third row.
Detail: `len(scores)` gives the number of rows, while `len(scores(row_index))` gives the number of columns in a specific row.
```python
# Maximum value of all scores in the 2D list.
# In the outer loop, have the row index vary through index values 0, 1, 2, 
# and in the inner loop, have the column index vary through index values 0, 1, 2, 3.
# Before beginning, initialize the maximum to be the first score in the first list.
maximum = scores[0][0]
for row_index in range(0, len(scores)):
    for column_index in range(0, len(scores[row_index])):
        if scores[row_index][column_index] > maximum:
            maximum = scores[row_index][column_index]
print(maximum) # outputs 93
```

Notice that the given 2D list is rectangular, not jagged. In other words, each row has the same number of columns.
In this situation, we can actually reverse the order of the loops. In other words, the outer loop can vary over each of the column
indexes 0, 1, 2, 3, while the inner loop varies over each row index 0, 1, 2. Reversing the order of the loops results in us visiting the
list elements in column-major order. So we first traverse every element in the first column, then every element in the second column,
then every element in the third column, and finally every element in the fourth column. Since we are finding a result that treats every
element in the matrix equally, it's fine to switch the order. Detail: `len(scores)` gives the number of rows. But one quirk of the
column-major ordering is that the number of elements in each column must be the same. 
For the number of columns, we will just use the number of columns in the first row, `len(scores[0])`.
```python
# Maximum value of all scores in the 2D list, computed in column-major order.
# In the outer loop, have the column index vary through index values 0, 1, 2, 3
# and in the inner loop, have the row index vary through index values 0, 1, 2.
# Before beginning, initialize the maximum to be the first score in the first list.
maximum = scores[0][0]
for column_index in range(0, len(scores[0])):
    for row_index in range(0, len(scores)):
        if scores[row_index][column_index] > maximum:
            maximum = scores[row_index][column_index]
print(maximum) # outputs 93
```

### Compute a quantity for a single row
Since we calculate a quantity for only one specific row, we do not need a nested loop.
Instead, the row index never changes, but we allow the column index to traverse all possible columns.
This means that the `column_index` will vary from 0 to `len(scores)-1` 
(the number of columns is `len(scores[row_index])`).
The code below calculates the average of Student 3's scores.
```python
# Average score for student 3. The row_index of 2 doesn't change.
# The column_index varies from 0 to 3. Add up all four scores, then
# divide by the number of columns.
total = 0
for column_index in range(0, len(scores[2])):
    total += scores[2][column_index]
average = total/len(scores[2])
print(average) # outputs 79.5
```

### Compute a quantity for a single column
Now we want calculate a quantity for only one specific column. Again, no need for a nested loop.
Instead, the column index never changes, but the row index traverses over all possible rows.
This means that the `row_index` will vary from 0 to `len[scores]-1` (the number of rows is `len[scores])`.
The code below calculates the average of all students on Quiz 4.
```python
# Average score of all students on Quiz 4. The column_index of 3 doesn't change.
# The row_index varies from 0 to 2. Add up all 3 scores, then divide
# by the number of rows.
total = 0
for row_index in range(0, len(scores)):
    total += scores[row_index][3]
average = total/len(scores)
print(average) # outputs 82.0
```

### Compute a quantity for every row individually
Say we want to calculate a quantity for every row separately. Since we're finding the quantity for each row, and
the quantity requires us to look at every column, we'll need to examine every value in the matrix.
This means we must use nested for-loops. 
Since we are calculating a quantity row-wise, the outside loop *must* vary throughout the rows.
Allow the row_index to vary throughout each row, then in the inner loop compute the quantity for that single row (see two sections above).
The code below finds the average score for each student separately.
```python
# Average score for every student. The row_index changes in the outer
# loop. For each row_index, the column_index varies from 0 to 3, through
# each quiz score for that student. Add up all four scores, then
# divide by the number of columns.
for row_index in range(0, len(scores)):
    total = 0
    for column_index in range(0, len(scores[row_index])):
        total += scores[row_index][column_index]
    average = total/len(scores[row_index])
    print(average) # This line is executed 3 times, outputting 78.5, then 80.5, then 79.5
```
Since the quantity is being calculated separately for each row, 
notice that the initialization of variables must happen *inside* the outer loop, but outside the inner loop.
So the initialization `total=0` is indented, executing as the first line inside the outer loop. That total is reset to 0 for each
student. Notice also that we want to print the result separately for each student. Thus the print statement is indented two levels.
The output is executed once for each student, at the end of the computation for that student.

### Compute a quantity for every column individually
Say we want to calculate a quantity for every column separately. This computation requires us to visit every value in the matrix,
so we must use a nested for-loop. But since we are doing a column-wise computation, the outer loop must vary over each column.
A matrix must be rectangular (not jagged) for this to work. Allow the col_index to vary over every column in the outside loop. 
Then within that loop, compute the quantity you want by looking at the values for each row within that column. This means the inner
loop will vary over every possible row.
```python
# Minimum score for each quiz. The column_index changes in the outer
# loop. For each column_index, the row_index varies from 0 to 2, through
# each quiz score for that student. Each time we find a score smaller
# than we've seen yet for that quiz, update the minimum
for column_index in range(0, len(scores[0])):
    minimum = scores[0][column_index]
    for row_index in range(0, len(scores)):
        if scores[row_index][column_index] < minimum:   
            minimum =  scores[row_index][column_index]  
    print(minimum) # This line executes 4 times, outputting 75, then 69, then 62, then 72
```
Because we are doing a separate computation for each column, notice that the initialization of `minimum` happens just inside the outer
for-loop. We initialize `minimum` to the first student's score on that quiz. Then at the end of the inner loop, the output of the result
is indented one level, so it is output once for each column.




