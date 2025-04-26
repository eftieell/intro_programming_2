## Files and Exceptions

Exceptions and errors are unexpected events in a program. Here are some errors you are already familiar with:

<table>
<tr><td>Exception</td><td>Cause</td><td>Example</td></tr>
<tr><td>

`SyntaxError`

Parsing error, program doesn't run
</td>
<td>Invalid code</td>
<td>

```python
3+y = x
```
</td></tr>
<tr>
<td>

`IndentationError`

Parsing error, program doesn't run
</td>
<td>Invalid indentation</td>
<td>

```python
for in range(5):
print("hello") # tab missing at start of line
```
</td>
</tr>
<tr>
<td>

`NameError`

Run-time exception
</td>

<td>Variable not initialized before use</td>
<td>

```python
print(x) # x not initialized
```
</td>
</tr>
<tr>
<td>

`TypeError`

Run-time exception
</td>
<td>Data types used incorrectly</td>
<td>

```python
s = 'hello' + 3
# perhaps the programmer meant 'hello' + str(3)
```
</td>
</tr>
<tr>
<td>

`ValueError`

Run-time exception
</td>
<td>Wrong value passed to a function</td>
<td>

```python
int("hello") # Can't convert this string to an int
```
</td>
</tr>
<tr>
<td>

`IndexError`

Run-time exception
</td>
<td>Invalid index used</td>

<td>

```python
a_list = [1, 2]
a_list[5] = 9
```

</td>
</tr>
<tr>
<td>

`FileNotFoundError`

Run-time exception
</td>
<td>
A file of given name doesn't exist
</td>
<td>

```python
open('no_such_file.txt','r')
```
</td>
</tr>
</table>

Run-time errors can be detected and processed as part of the program. This means that you can write code to address the error and recover from it gracefully, rather than the program just crashing. This is done with a `try-except` code block. Place the code that has the chance of producing a runtime exception within the `try` part of a `try-except` block, then process the potential exception in the `except` block. The `except` block is only executed in case of the  runtime exception named. Here's an example of how to process a user input error:
```python
try:
    age = int(input("Input your age: "))
except ValueError:
    print('Error: Age must be a whole number')
```

Here's a sample output showing with the user sees:
```
Input your age: Sue
Error: Age must be a whole number
```
In the above code, instead of the program crashing with the `ValueError`, the error is *caught* by the `try` block and *handled* by the `except` block. It is common to put a `try-except` block within a loop, giving the opportunity for the code to repeat execution until no error occurs.

```python
age = None # initialize age to an invalid value
# Keep trying to get valid input until finally
# age is a valid integer
while age is None:
    try:
        age = int(input("Input your age: "))
    except ValueError:
        print('Error: Age must be a whole number.')
print(f'Your age is {age}'
```
Sample output:
```
Input your age: Sue
Error: Age must be a whole number.
Input your age: 27.5
Error: Age must be a whole number.
Input your age: 27
Your age is 27
```

It is very common practice to put opening of a file within a `try-except` block.
```python
file_name = input("What is the name of the file? ")
try:
    with open(file_name) as a_file:
        # code to process contents of file
except FileNotFoundError:
    print(f'Error: could not open "{file_name}"')
```

## Best practices for when to handle exceptions

Catching errors during standard running of a progam is good programming practice, since unhandled exceptions cause the program to crash.

From now on, you should be using `try-except` blocks to handle errors that legitimately occur during the running of programs, in particular to respond to invalid input entered by the user. However, do *not* use `try-except` blocks to mask errors in your own code. For example, if your program has a bug in which you traverse a list past its end and crash with an `IndexError`, never stop your program from crashing by wrapping the incorrect lines of code within a `try-except` block. Instead always fix the underlying bug.