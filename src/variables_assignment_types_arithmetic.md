## Variables in python

- The purpose of a *variable* is to store information within a program while it is running.
- A variable is named storage in computer memory. Use the name to access the value.
- To store a value in a variable, use the = operato (called the assignment operator). 
- For example, the line of code
`hourly_wage = 16.75`
stores the value 16.75 in the variable called `hourly-wage`
- You can change the value of a variable with another assignment statement, such as 
`hourly_wage = 17.25`
- Every value has a type (`int` for integers, `float` for decimals, `str` for text). In python, when you store a value in a variable (with =), that variable then automatically has a type. For example, after the above assignment, `hourly_wage` is of type `float`


## Rules and conventions for naming variables in python

- The first character must be a letter or an underscore. For now, stick to letters.
- The remaining letters must be letters, numbers or underscores.
- No spaces are allowed in variable names
- Valid examples: `_pressure`, `pull`, `x_y`, `r2d2`
- Invalid examples, these are NOT legal variable names: `4th_dimension`, `%profit`, `x*y`, `four(4)`, `repo man`
- In python, it's a conventiion to use `snake case` to name variables.This means that we use all lower-case letters and we separate words in the variable name with underscores. Examples include `age`, `x_coordinate`, `hourly_wage`, `user_password`
- If the value stored in a variable is a true constant (in other words, its value will never change during the program), then we use all caps: `COURSE_ENROLLMENT_LIMIT`, `MAX_PASSWORD_ATTEMPTS`
- It is crucial that you choose names for variables that are descriptive. The variable names must help the reader of your program to understand your intention.

## Typical way we visualize variables
We usually draw variables by putting the value in a box, and labelling the box with the name of the variable:

![Visual representation of a variable](img/variables_assignment_types_arithmetic/depiction_of_variable.png)

## Types of variables
Each variable has a name, a value, and a type. Types are necessary because different kinds of data are stored differently within the computer's memory. For now, we will learn three different types, for storing signed (positive or negative) whole numbers, decimals, and text 


| Variable Type | Description |Examples |
| -------- | -------- | --------|
| Numerical type | `int` | Signed integer type that stores whole numbers (no decimal) | 0, 7, -5|
|Numerical type | `float` | Signed decimal value | 0.5, 20.0, -18.2, 2.5e3 = 2.5x10^3|
| String type (Text) | `str` | Any number of characters surrounded by "" or ''| "Hello", 'world', '9'|

## Creating variables - assignment operators

A variable is created or declared when we assign a value to it using the assignment operator `=`. In python, the code looks like this:
`variable_name = <value>`
Notice that the left hand side of an assignment must be a variable name
Examples:
```python
# The next line stores an int value of 200 in the variable named age
age = 200
# The next line stores a float value of 7.5 in the variable named height
height = 7.5
# The next line stores a string (text) value of 'Chewbacca' in the variable named age
name = 'Chewbacca'
```

Non-example:
```python
# The following line is an error, don't do this!
200 = height
```
After creating a variable, you can change the value stored in a variable with another assignment operator at any time. This is called *reassignment*
```python
age = 201
```

## Finding out the type of a variable or value

The `type()` function in python will return the type of either a variable or a value. Here's an example that shows how to use it:
```python
x = 5
print(type(x))
print(type("Wow!"))
print(type(3.14159))
```
The output of the above code will be:
```
<class 'int'>
<class 'str'>
<class 'float'>
```

# Casting (changing the type) of a variable or value

You can change the type of a value (called “casting”) using the `int()`, `float()` and `str()` functions. For example:
- `int(23.2)` (rounds down, or truncates the float value 23.2 to the int value 23)
- `float("23")` (outputting the result will give 23.0 rather than 23)
- `str(23)` (the result is the text "23" rather than the number 23)
- `int('23')` (the result is a conversion of the string "23" into a numerical integer value of 23)
- `int("23.5")` results in an error
- `float("hello")` results in an error

# Doing arithmetic in python

Here are the basic arithmetic operators in python. In these examples, assume
```python
x = 11
y = 4
```
|Operator|Description|Syntax|Output|
| ----- | ----- | ----- | ----- |
|`+`|Addition |`x+y`|`15`|
|`*`|Multiplication |`x*y`|`44`|
|`-`| Subtraction | `x-y`|`7`|
|`/`| Decimal division (type is a float)| `x/y`|`2.75`|
|`//`| Integer division (type is an int, result of division is truncated)|`x//y`|`2`|
|`%`|Modulus (remainder when first operand is divided by the second)| `x%y`|`3`
|`**`|Exponentiation (raises the first  to the power of the second )|`x**y`|`14641`|

Warning note: In python, `^` is **not** an exponent!

## Order of operations

The order of operations in python is similar to the order you are familiar with in math:
parentheses, exponentiation, multiplication/division/modulus in order from left to right, addition/subtraction in order from left to right.
