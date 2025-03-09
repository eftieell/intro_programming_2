# Implementing recursive functions

You can implement a recursive algorithm any time you can break a computation down into one or more parts that involve the same computation, but with smaller values. This is known as a *recursive relationship*. In addition to the recursive relationship, you also always need a *base case*, which tells you when to stop the recursion.

## Example 1 - computing powers

Suppose you want to write a function called `power()` that evaluates an exponential expression \\(a^n\\). For example, we want the line
``` python
print(power(2, 5))
```
to output the number 32 (since \\(2^5 = 32\\)). You already should know how to implement this iteratively (i.e., using a for-loop - try it for practice!). We'll now see how to implement it using recursion. Suppose we already knew the value of \\(2^4\\). Then it would be trivial to compute \\(2^5\\): since \\(2^5 = 2^4*2\\), we would simply multiply \\(2^4\\) by 2. So within the implementation of the `power()` function, when computing \\(2^5\\), we call the `power()` function to perform the subtask of computing \\(2^4\\). More generally, `power(a, n)` is just `power(a, n-1)*a`. This line of code expresses the mathematical recursive relationship \\(a^n = a\cdot a^{n-1}\\). Here's a partial (and flawed!) implementation that uses this idea:
```python
def power(a, n):
    return power(a, n-1)*a
```
To see the flaw with the above code, imagine the call `power(2, 0)`, which should just return the value 1. Instead, it attempts to return `2*power(2, -1)`. When `power(2, -1)` is called, the expression `2*power(2, -2)` must be evaluated. In turn, to evaluate `power(2, -2)`, the the expression `2*power(2, -3)` must be computed. Notice that the exponent will continue to decrease, and we will recurse infinitely, crashing with a `RecursionError`. This demonstrates the need for a *base case*. When the exponent is 0, rather than making a recursive call, instead we should simply return the value 1. Here's code that includes the base case:
```python
def power(a, n):
    # base case:
    if n == 0:
        return 1
    # recursive call:
    else:
        return power(a, n-1)*a

# main code block:
print(power(2, 5)) # correctly outputs 32
```
Other than error-checking (n must be a positive integer for this code to work), this is a correct and complete implementation. To summarize the key facts we needed to implement this function:
* base case: \\(a^0=1\\)
* recursive relationship: \\(a^n = a^{n-1} * a\\)

Notice how these two components appear as different cases in the code.

## Example 2 - computing factorials

Now we will implement the factorial function. Recall that the factorial of a non-negative integer n is written n!, and it is the product of all positive integers less than or equal to n. For example, \\(5! = 5\cdot4\cdot3\cdot2\cdot1\\). Note that 1! = 1 and 0! = 1. Finally, note that there is a relationship between a factorial value and the one before it. For example, \\(5! = 5 \cdot 4!\\).
As always with recursion, we start by identifying the recursive relationship, and the base case:
* base case: 0! = 1
* recursive relationship: \\(n! = n\cdot (n-1)!\\)

These two components of the recursion translate directly to two cases in the implementation:
```python
def factorial(n: int):
    # base case:
    if n == 0:
        return 1
    # recursive call:
    else:
        return n*factorial(n-1)

# main code block:
print(f"10! is {factorial(10):,}")
```
Output:
```
10! is 3,628,800
```

### Error-checking

Notice that the code above does not do error-checking. Suppose we call factorial with a negative value:
```python
print(f"uh-oh: {factorial(-1)}")
```
By starting at a negative number, the base case is eluded, and the program crashes with the output `RecursionError: maximum recursion depth exceeded`.

One might blame the caller for this error: factorials should not be computed for negative numbers. However, it is good programming practice to make our implementations robust against errors by the caller. One way to fix it is to return -1 to indicate an error state if a negative number is passed to factorial:
```python
def factorial(n: int):
    # check for errors:
    if n < 0:
        return -1
    # base case:
    elif n == 0:
        return 1
    # recursive call:
    else:
        return n*factorial(n-1)
```

## Example 3 - computing greatest common divisors

### Greatest common divisors and their recursive relationship
It's common in Computer Science to need to find the greatest common divisor (gcd) of two numbers. Recall that the greatest common divisor of two integers is the largest integer that divides both numbers. For example, gcd(25, 15) = 5, and gcd(60, 72) = 12. In grade school you learned how to find the gcd of two numbers by fully factoring each, and finding the overlap of the factors. For example, \\(60 = 5\cdot3\cdot2\cdot2\\) and \\(72 = 3\cdot3\cdot2\cdot2\cdot2\\). The shared factors are \\(3\cdot2\cdot2\\), so gcd(60, 72) = 12. 

However, when integers are large, factoring becomes computationally intractible, so the factoring method of finding gcds is not feasible. Fortunately, there is a theorem for reducing the problem to a smaller size. Divide the larger number by the smaller number, and find the remainder.
Then the gcd of the original two numbers is the same as the gcd of the smaller number and the remainder. For example, \\(72 = 1\cdot 60 + 12\\), so gcd(72, 60) = gcd(60, 12). This new problem with smaller values is easier. Since 12 goes into 60 evenly, gcd(72, 60) = gcd(60, 12) = 12. Repeatedly applying this strategy is called *the Euclidean algorithm*. We can describe this algorithm for finding gcd(a,b) (where a > b) as follows:
* base case: if b divides a, then the answer is b. Note that b divides a if `a%b == 0`
* recursive relationship: gcd(a, b) = gcd(b, r), where r is the remainder when a is divided by b. Note that ``r = a%b``.

### Implementing the `gcd()` function

The recursive implementation of gcd is easy now that we have described the base case and the recursive relationship:

```python
def gcd(a, b):
    # base case:
    if a%b == 0:
        return b
    # recursive call:
    else:
        return gcd(b, a%b)

# main code block:
print(gcd(60, 48)) # outputs 12
```

The above implementation is remarkable straight-forward! Note that it has some flaws that we have not checked or corrected:
* What if the a < b?
* What if one or both of the numbers are 0?
* What if one or both of the numbers is negative?

Completing the function to handle these errors is left to you.