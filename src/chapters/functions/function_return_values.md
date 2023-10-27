## Review of functions

Recall that a function definition is a collection of code statements grouped together that perform a specific task.

Every function has a name that can be used to *call* the function. We also use the terms *invoke*, or *execute* to mean *run the lines of code that appear within the function definition*.

You can think of the function definition as a recipe for how to perform a task. When the function is invoked, then the task is actually performed.

Recall also that functions may take input values (called parameters) that modify or control how the function runs.

## Why use functions?

There are two main reasons that functions are useful in programming:

- Reusability

    Often we need to use the same code multiple times.
    One solution is to copy/paste the code to reuse it. One downside of that strategy is that it makes our programs much longer. But an even worse downside is that if we make a modification, we need to find and make that same change in every place we copied the code to. Functions instead allow us to efficiently invoke the same code whenever needed without making multiple copies.

- Abstraction

    Once a function has been written and tested, we don't need to know how it works anymore. We only need to remember its **name, purpose, parameters, and return value**. For example, when you use the `dudraw.circle()` function, you can just use it without bothering your mind with the distraction of how that function creates the circle. This allows us to build functions from functions already written, and this allows us to produce very complicated software much more easily.

- Code organization and readability

    Organizing  your code into a sequence of function calls allows you to focus at any time while you are programming on just the task at hand. It also makes it far easier for others to read your code and understand it.

## A function can return a value

A function can also *return* a result. You can choose the type of the returned value. If no value is returned, then the return type is `None`.

For example, the print function, as in

```python
print("Hello!")
```
takes a parameter (the input to the function is `"Hello"`), but it does not return a value.

But the `input()` function does return a value. The return type is `str`.  When the function is *invoked*, when it is done executing it returns a value. You may do whatever is useful with that return value. In the example below the value returned by the `input()` function is stored in the variable `name`:

```python
name = input("Enter your name")
```

Another example is the `random()` function, which returns a `float`. We may choose to store the value that is returned in a variable. Or we may choose to pass that return value as a parameter to another function:

```python
# Store the return value in a variable:
x_position = random()
# Pass the return value to the print function:
print(random())
```

## User-defined functions that return values

When you define a function, you only need to do so once. Once defined, however, a function may be invoked many times. You can think of a function as an opaque box that performs work with optional inputs and an optional output.

The syntax is:

```python
def function_name(optional parameters) -> return type:
    # Indented code block
    # Optional return statement
    # (Leave off the return statement if the function returns `None`)
```

Example:
Here's a function that takes a `float` parameter named `temp_f` that represents a temperature in Fahrenheit (think of `temp_f` as an input value to the function). The function then computes the conversion of the temperature to Celsius. The converted value `temp_c` of type `float` is returned (think of `temp_c` as an output value from the function).

```python
def celsius(temp_f: float) -> float:
    # compute the conversion from fahrenheit to celsius
    temp_c = (temp_f - 32) * 5 / 9
    return temp_c
```

In the example above, think of the parameter `temp_f` as a local variable of the `celsius()` function. That variable can only be accessed *within* the scope of the function. When the function completes execution, the variable `temp_f` is destroyed and can no longer be accessed. On the last line of the function, the `return` statement has the effect of sending the value `temp_c` back to the line that invoked the function. Here is a sample of how the `celsius()` function might be invoked:

```python
    user_temp_f = float(input("Please enter the temperature in Fahrenheit: "))
    user_temp_c = celsius(user_temp_f)
    print(f"{user_temp_f} degrees Fahrenheit is {user_temp_c:.1f} degrees Celsius")
```
The first line gets a `float` Fahrenheit temperature from the user.
The second line calls (invokes) the `celsius()` function. The value of the variable `user_temp_f` is passed as the parameter to the `celsius()` function. Within the `celsius()` function, that value is stored in the `temp_f` variable and the result is computed. Then the `celsius()` function returns the `float` value result. Back in the main code block, the return value from `celsius()` is stored in the `user_temp_c` variable.
The last line gives full formatted output to the user.

Note that `celsius(user_temp_f)` is actually an expression, with a value (the return value) and a type (`float`). This means we can put `celsius(user_temp_f)` in our code *anywhere* that we can validly put any expression. For example:
```python
    print(celsius(user_temp_f))
```
In the above line of code, `celsius(user_temp_f)` is an expression whose value is whatever the `celsius` function returns. That value is passed in turn as a parameter to the `print()` function! This might remind you of function composition in algebra. A more sophisticated example of this is shown below, a compression of the previous example from  three lines of code into two:
```python
user_temp_f = float(input("Please enter the temperature in Fahrenheit: "))
print(f"{user_temp_f} degrees Fahrenheit is {celsius(user_temp_f):.1f} degrees Celsius")
```

## Boolean functions

Note that a function may return a value of type `bool`. These are called *boolean functions*, and just as before, the return value can be used as an expression. For example:

```python
# Return True if the first digit of the number is even,
# otherwise return False
def first_digit_even(number: int) -> bool:
    # Keep dividing by 10 until the number is less than 10
    while number >= 10:
        number = number // 10

    # Now we have a one-digit number. See if that digit is even
    return number%2 == 0
```

The `while`-loop repeatedly divides by 10 using integer division (shifting the number to the right), until only one digit remains. That digit is the first digit of the original number. Then on the last line, the expression `number%2==0` evaluates to `True`  if that first digit is even, and `False` if that first digit is odd. The `True` or `False` value gets returned.

Here's an example of a code snippet that uses the function:

```python
user_num = int(input("Enter an integer: "))
if first_digit_even(user_num):
    print(f"The first digit of {user_num} is even.")
else:
    print(f"The first digit of {user_num} is odd.")
```

## Putting it all together

The following example code defines and uses a boolean function `is_prime()` that determines whether or not an integer is prime.
A prime number is an integer bigger than `1` that is divisible only by `1` and itself.

```python
def is_prime(number: int) -> bool:
    """
    A function that determines whether or not a number is prime
    parameters:
        number: a positive integer greater than 1 (type: int)
    return:
        True if number is prime, False otherwise (type: bool)
    """

    # tester is a possible factor. Start at 2 and we will increase it
    tester = 2

    while tester < number:
        if number % tester == 0:
            # We now know that tester divides number, so
            # we know the answer - number is not prime!
            # The function teriminates, returning False
            return False
        else:
            tester += 1

    # We only reach this line if no return False above every occurred.
    # This means that the number has no factors and thus it is prime
    return True
    
def main():
    # The user inputs an integer and we determine if it is prime
    num = int(input("Enter an integer to test for primality: "))
    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

# Run the program:
if __name__ == '__main__':
    main()
```

Key points:

- The input for this function is an integer bigger than 1 (our program would be improved if we checked for this condition).
- The output is a boolean (`True` if `number` is prime, `False` otherwise).
- It's helpful for boolean functions to have names that reflect that they return a `True/False` result. Here, `is_prime()` reads like a question that has a yes/no answer. When we call the function, the line
`if is_prime(23):` makes sense when we read it.
- A function should only perform one task. Here, the job is to determine whether or not the number is prime. The function does *not* output the result to the console. The function just returns the result to the line that invoked it. It's up to the caller to interact with the user. This philosophy makes for more flexible and reusable functions.
- Within the loop of the `is_prime()` function, we can only return `False`, never `True`. Because only by completing the entire loop can we know that `number` has no factors (other than `1` and itself). The `return True` can thus only happen after the loop has completed.
- The program could be made to run more efficiently by stopping the loop when `tester` reaches the square root of `number`.

By placing the code to determine whether a number is prime into a separate function, we can now re-use it in  multiple ways. For example, here is a new `main()` function that outputs all primes less than `1000`:

```python
def main():
    # Output all primes less than 1000, testing each number one by one
    for i in range(2, 1000):
        if is_prime(i):
            # output the number if it is prime:
            print(i, end = " ")
    # Move output to a new line
    print()
```
You should notice how simple it was to create this new program. The `is_prime()` function did not need to be rewritten or even thought about.

Here is yet another example. This time we will build another layer on top of the `is_prime()` function by creating a function called `next_prime()` to give the next prime larger than a specific integer. Notice that `next_prime()` itself uses `is_prime()`, so its job is made straightforward and easy to understand. By the use of these two functions, the interface with the user in `main()` is also very straightforward. This organization and structure makes code easier to read and understand, easier to fix if it has an error, and easier to enhance or modify if we choose to later. Notice that the contents of `is_prime()` are not shown here, since that function is identical to before.

```python
def is_prime(number: int) -> bool:
    # contents not shown - it's unchanged from before!

def next_prime(number: int) -> int:
    """
    Return the first prime greater than or equal to number
    parameters:
        number: input value for which we need to return the next prime (type: int)
    return:
        a prime value greater than or equal to number (type: int)
    """
    # start from number, and increment until we find the next prime
    while not is_prime(number):
        number += 1
    # The loop has terminated, so the current value of number must be the next prime.
    return number
    

def main():
    n = int(input("Give me a number and I will tell you the next prime: "))
    print(f"The next prime is {next_prime(n)}")

# Run the program:
if __name__ == '__main__':
    main()
```