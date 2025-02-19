## Recursive Structures

We can also define structures recursively. One example is the list structure.

A list is a sequence of items. 

A list could be viewed in its entirety as consisting of k individual elements.

A list could also be viewed as a recursive structure. In this view, any list is one of two possibilities:

- The list is Empty and contains no items.
- The list consists of a first item followed by another list.

This recursive definition also shows how a list could be built. For example, the Python list 

```python
['a', 'b', 'c']
```
could be built in code using:

```python
[].insert(0, 'a').insert(0, 'b').insert(0, 'c')
```
or 
```python
[].append('a').append('b').append('c')
```

In both of these examples, we are build a list which starts with 'a' and is followed by the list which starts with 'b' and is followed by the list which starts with 'c' and is followed by the list which is empty.

List Examples

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
- The sum of any other list is the first number plus the sum of the list of numbers after the first number

```python
def sum_of_items( prices_of_items : list[float] ) -> float :
    sum_of_items_helper( 0, prices_of_items )

def sum_of_items_helper( start, prices_of_items : list[float] ) -> float :
    # find the sum of the numbers in item_list
    # the sum of the empty list is 0
    if start == len( prices_of_items ) :
        return 0
    return prices_of_items[start] + sum_of_items_helper(start+1,prices_of_items)
```

another implementation :
```python
def sum_of_items( prices_of_items : list[float] ) -> float :
    if len(prices_of_items) == 0 :
        return 0
    return prices_of_items[0] + sum_of_items( prices_of_items.pop(0) )
```