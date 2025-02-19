# Implementing recursive functions

You can implement a recursive algorithm any time you can break a computation down into one or more parts with smaller values. 

For example, suppose you want to write a function called `power()` that evaluates an exponential expression \\a^n\\. For example, we want the line
``` python
print(power(2, 5))
```
to output the number 32 (since \\2^5 = 32\\). You already should know how to implement this using a for-loop (try it for practice!). We'll now talk about how to implement it using recursion. Suppose we already knew the value of \\2^4\\. Then it would be trivial to compute \\2^5\\: we would simply multiply \\2^4\\ by 2. So within the implementation of the `power()` function, when computing \\2^5\\, we call the ``power()`` function to perform the subtask of computing \\2^4\\. More generally, ``power(a, n)`` is just ``a*power(a, n-1)``. This line of code expresses the mathematical relationship \\a^n = a\cdot a^{n-1}. Here's a partial (and flawed!) implementation that uses this idea:
```python
def power(a, n):
    return a*power(a, n-1)
```
To see the flaw with the above code, imagine the call ``power(2, 0)``, which should just return the value 1. Instead, it attempts to return ``2*power(2, -1)``. 
