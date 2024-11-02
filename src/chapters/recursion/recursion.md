## Recursion

Solving a problem often involves breaking that problem down into smaller and hopefully easier to solve problems. 

When writing a program to solve a problem this often involves writing functions to solve smaller subproblems.

Suppose we want to write a function which produces the sum of the first k integers (i.e. 1 + 2 + 3 + ... + (k-1) + k).

One solution is to write a for loop which iterates over the first k integers by counting upward from 1 to k.

```python
def sum_of_k_numbers( k : int ) -> int:
    # find the sum of the integers up to and including k
    total = 0
    for number in range(k+1) :  # k+1 needed so we include k in the sum
        total += number
    return total
```

We could also count downward from k to 1:

```python
def sum_of_k_numbers_downward( k : int ) -> int:
    # find the sum of the integers up to and including k
    total = 0
    for number in range(k,0,-1) :   # 0 needed so we include 1 in the sum
        total += number
    return total
```

Another solution is to consider that the total is created by adding the first number to the total of the numbers after the first number. For this solution, we will create two functions. One function which starts the overall process and another function, a helper function, which totals some portion of the numbers.

```python
def sum_of_k_numbers( k : int ) -> int:
    # Call the helper function to 
    # find the sum of the integers up to and including k
    return sum_of_k_numbers_helper( 0, k )

def sum_of_k_numbers_helper( start : int, end : int ) -> int :
    # When start == end the total is end
    if start == end :
        return end
    return start + sum_of_k_numbers_helper( start + 1, end )
```

The first function delegates to the sum_of_k_numbers_helper by specifying where to start and end the numbers to add to the total.

The helper function contains two cases:
- When the starting number is equal to the ending number, the total is equal to the ending number (i.e. when adding the numbers starting at 13 and ending at 13, the total is 13).
- Otherwise, the total will be the starting number added to the total we get from adding the numbers after the starting number up to the ending number (i.e. when adding the numbers starting at 5 and ending at 13, the total is 5 + the total from 6 to 13).

The definition of the sum_of_k_numbers_helper function contains a call to itself. A function which calls itself it known as a *recursive function.

Writing recursive functions is allowed in Python (and most programming languages). We want to be careful to make sure that a recursive does not "run forever" by continuing to call itself with no way to stop.

The first case in the example above is known as a base case. It is a simple example of the problem with a known solution.

The second case in the example above is known as a recursive case. It shows how to divide the current problem into one or more smaller problems.

Eventually the overall problem will be divided into problems which contain base cases. The solution to those base cases can then be returned back to previous calls of the helper function which ultimately creates the overall final result.

LIST EXAMPLE

Consider a program to calculate the total cost of eating at a restaurant. One part of this program might be a function which takes a list of numbers as a parameter and produces the sum of those numbers. One version of this function might be:

```python
def sum_of_items( prices_of_items : list[float] ) -> float:
    # find the sum of the numbers in item_list
    total = 0
    for index in range( len( prices_of_items )) :
        total += prices_of_items[index]
    return total
```

This function uses iteration to access each value in the list and add it to the total.

Another solution is to view this process in a different way:
- The sum of empty list of numbers is 0
- The sum of any other list is the first number plus the sum of any numbers after the first number

```python
def sum_of_items( prices_of_items : list[float] ) -> float:
    # find the sum of the numbers in item_list
    total = 0
    for index in range( len( prices_of_items )) :
        total += prices_of_items[index]
    return total
```