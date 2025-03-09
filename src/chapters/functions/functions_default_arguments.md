# Default argument values

Default argument values give a way to make it optional for the caller to pass an argument to a function.
In fact, you've already seen examples of optional arguments to functions.
Perhaps you have noticed that some functions can be called with different numbers of arguments. 
For example, you can call `dudraw.clear()` with either no arguments or one argument:
```python
dudraw.clear(dudraw.GREEN)  # clears the canvas, all pixels are now GREEN
dudraw.clear()              # this time no argument is passed - so the default is to clear with dudraw.WHITE
```
Here's another example. You may pass an argument to `print()` to specify what the end character is. But you may also leave that argument out, in which case `print()` ends with a newline.

Without the end character optional argument:
```python
# The code below puts "Hello" and "World" on two different lines, 
# since the default end character for print() is a newline ("\n"):
print("Hello,")
print("World!")
```
Output:
```
Hello,
World!
```
With the end character optional argument:
```python
# Alternately, we can pass an optional extra argument to print().
# The first print() statement below ends with a space rather than the default newline.
# So the two strings are output separated by a space, not a newline.
print("Hello,", end = " ")
print("World!")
```
Output:
```
Hello, World!
```

## How does this work?

Behind the scenes, in the definition of `dudraw.clear()` a default value for the argument is specified (namely `dudraw.WHITE`). By doing so, it allows the client code (your code) to either include or omit that argument. If you include the argument, it specifies the background color. But if you omit that argument, then the function uses the default value `dudraw.WHITE` as the color. The default value is specified in the definition of the function.

Similarly, you may include or omit an additional argument to `print()` to specify the end character. (for example, `end = " "`). If you call `print()` without the `end` parameter, then `print()` automatically uses the default end value `"\n"`.

## Defining your own functions with default argument values
If you want to create functions that can be called with or without one or more of the arguments, specify `parameter_name = default_value` in the function header. If you specify a default value, then it becomes optional to pass that argument when the function is called.
```python
# The greet() function outputs "Hello, {name}!". The default value for name is "World".
# So if no name is passed as a parameter, then the function outputs "Hello, World!"
def greet(name: str = "World"):
    print("Hello, " + name + "!")

def main():
    greet("Sami")    # outputs "Hello, Sami!"
    greet("Phyllis") # outputs "Hello, Phyllis!"
    greet()          # outputs "Hello, World!"

if __name__ == "__main__":
    main()
```

If there are two or more parameters, then mandatory arguments must come first. So always put
parameters with default values at the end of the parameter list. Here's another example (taken from python documentation <a href = "https://docs.python.org/3/tutorial/controlflow.html#default-argument-values" target = "blank">https://docs.python.org/3/tutorial/controlflow.html#default-argument-values</a>
```python
# There are three parameters. The second two parameters have default values.
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```
The above function can be called multiple ways:
- giving only the mandatory argument: `ask_ok('Do you really want to quit?')`

- giving one of the optional arguments: `ask_ok('OK to overwrite the file?', 2)`

- or even giving all arguments: `ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')`

