# Dunder methods (methods whose name starts with two underscores)

In python, methods that start with two underscores are called *dunder* (double-underscore) methods. They are sometimes also referred to as *magic* methods. These methods have special significance, since they are automatically invoked by python in certain situtations. You've seen two examples of this already: the `__init__` function is automatically (or "magically") invoked when you instantiate an object, and the `__str__` method is automatically invoked when you print an object. For example:
```python
class Time24:
    """ A class that represents a time of day on a 24-hour clock
        Default time is 0 hours 0 minutes """
    def __init__(self,h: int = 0, m: float = 0):
        # set up the instance variables. Note that this initialization
        # method does not do error checking on the values, and it should
        self.hours = h
        self.minutes = m

    # return a string formated as hour:minute. Since we're using
    # a 24-hour clock, it's 2 digits for both hours and minutes
    def __str__(self)->str:
        return f"{self.hours:02d}:{self.minutes:02d}"


time1 = Time24(12, 59)  # automatically calls __init__
print(time1)            # automatically calls __str__, outputs 12:59
```

Besides `__init__` and `__str__`, python has a long list of other dunder methods. We will learn the *rich comparison operators*, which allows us, whenever it makes sense, to compare two objects of a class using  the operators `<`, `<=`, `==`, <code>!=</code>, `>=`, and `>`.

In the work below, we will use the following `Time24` objects:
```python
time1 = Time24(12, 7)   # instantiate time2 object, represents 12:07
time2 = Time24(2, 43)   # instantiate time2 object, represents 02:43
time3 = Time24(12, 7)   # instantiate time3 object, represents 12:07
default_time = Time24() # default time is 00:00
```

## Using the == operator to compare two objects

Notice that two of the `Time24` objects above (`time1` and `time2`) represent the same time of day. What do you think is output by the following line of code?
```python
print(time1 == time3)
```
Are you disappointed to find out that the above line of code outputs `False`? By default, two objects evaluate as equal in python when they represent the identical object (stored in the same memory location). By default, python does not compare the *contents* of the objects to see if the *contents are the same*. But when dealing with objects, comparing the contents is often what we want to do. So python gives us a way to make the `==` comparison between objects compare the contents of the objects, according to a method we provide. This is called "overloading the `==` operator".

## How to overload the `==` operator
* Within the class, implement a method called `__eq__`. 
* The `__eq__` method defines in python code how to tell if two objects are equal.
* The `__eq__` method is automatically ("magically") called when you use `==` to compare two objects.
* The `__eq__` method should return a `bool`.
* In our example, we will say two `Time24` objects equal if and only if they have the same values for hour and the same values for minutes. 
* The `__eq__` method should take two parameters. The object on the
left side of `==` becomes `self`, and the object on the right side of the `==` becomes the second parameter, typically named `other`.

Include this code in the `Time24` class:
```python
    def __eq__(self, other)->bool:
        return self.hours == other.hours and self.minutes == other.minutes
```

Now the following line outputs `True`, as desired:
```python
print(time1 == time3). # automatically calls the __eq__ method from the Time24 class, time1 is self, time3 is other
```

## Using the < operator to compare two objects

We would like the following line to output `False`, since time2 is 2:43 in the morning, and time2 is in the afternoon
```python
print(time1 < time2)
```
But here's the output:
```
TypeError: '<' not supported between instances of 'Time24' and 'Time24'
```
When objects in a class have a natural linear ordering, then it makes sense to compare them with the `<` operator. To implement this in python, we provide a `__lt__` operator in our class. The `__lt__` method should return a boolean, and take two parameters. The `__lt__` method will automatically be called when the code `object < object2` is evaluated, with `object1` becoming the parameter `self`, and `object2` becoming the parameter `other`. For example, here is an implementation of `__lt__` for our `Time24` class. Insert this code into the class.
```python
    def __lt__(self, other)->bool:
        if self.hours < other.hours:
            return True
        elif self.hours > other.hours:
            return False
        else:
            return self.minutes < other.minutes
```
Here is some demo code to show you show to call
```python
print(time1 < time2)        # calls __lt__, outputs False (time2 is earlier in the day)
print(time1 < time3)        # outputs True (they are equal, so time1 isn't less than time3)
print(default_time < time2) # outputs True, midnight is earlier than any other time

```

## The other rich-comparison operators
The table below lists the names of the dunder methods to implement for each of the comparison operators.
| Operator | dunder method |
| -------- | ------- |
| `==` (equal to) | `__eq__(self, other)` |
| <code>!=</code> (not equal to) | `__ne__(self, other)` |
| `<` (less than) | `__lt__(self, other)` |
| `<=` (less than or equal to) | `__le__(self, other)` |
| `>` (greater than) | `__gt__(self, other)` |
| `>=` (greater than or equal to) | `__ge__(self, other)` |

Notice that each operator is actually the negation of one of the other operators. For example, `>=` is the negation of `<`. You can use this to shorten your code. The following is the complete implementation of rich comparison operators for our `Time24` class:
```python
class Time24:
    """ A class that represents a time of day on a 24-hour clock
        Default time is 0 hours 0 minutes """
    def __init__(self,h: int = 0, m: float = 0):
        # set up the instance variables. Note that this initialization
        # method does not do error checking on the values, and it should
        self.hours = h
        self.minutes = m

    # return a string formated as hour:minute. Since we're using
    # a 24-hour clock, it's 2 digits for both hours and minutes
    def __str__(self)->str:
        return f"{self.hours:02d}:{self.minutes:02d}"
    
    def __eq__(self, other)->bool:
        return self.hours == other.hours and self.minutes == other.minutes

    def __lt__(self, other)->bool:
        if self.hours < other.hours:
            return True
        elif self.hours > other.hours:
            return False
        else:
            return self.minutes < other.minutes
        
    def __le__(self, other)->bool:
        if self.hours < other.hours:
            return True
        elif self.hours > other.hours:
            return False
        else:
            return self.minutes <= other.minutes
        
    def __ne__(self, other)->bool:
        return not self==other
    
    def __gt__(self, other)->bool:
        return not self <= other
    
    def __ge__(self, other)->bool:
        return not self < other
```

## Using dunder methods to overload arithmetic operators
Suppose we have a class that it makes sense to do arithmetic with. For example, say I implement the `Point` class, where each point is a location in the (x, y) plane. In some contexts it is mathematically useful to add two points by separately adding their x and y coordinates. For example, (1, 3) + (6, 5) = (7, 8). Consider the following implementation of the `Point` class:
```python
class Point:

    def __init__(self, x, y):
        # initialize the values of the point (x, y)
        self.x = x
        self.y = y

    def __str__(self)->str:
        # format the string in (x, y) form
        return f"({self.x}, {self.y})"
```
    
We wish the following code would output (7, 8):
```python
point1 = Point(1, 3)
point2 = Point(6, 5)
point3 = point1 + point2
print(point3)
```
But instead here's the output:
```
TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
```
We can "teach" python how to add elements of our `Point` class by implementing the method `__add__` in our class. The `__add__` method will be automatically called when python evaluates the expression `point1 + point2`. It takes two parameters, `self` and `other`, where the first summand `point1` takes the role of `self`, and the second summand `point2` takes th role of `other`. The `__add__` method should create and return a new `Point`, whose values are the sums of the individual points. Here's the implementation, which is incorporated into the `Point` class:
```python
    def __add__(self, other: Point)->Point:
        newx = self.x + other.x
        newy = self.y + other.y
        new_point = Point(newx, newy)
        return new_point
```
Now, the code
```python
point1 = Point(1, 3)
point2 = Point(6, 5)
point3 = point1 + point2
print(point3)
```
outputs
```
(7. 8)
```
Note: the `__add__` function could be condensed to one line:
```python
    def __add__(self, other: Point)->Point:
        return Point(self.x+other.x, self.y+other.y)
```
All of the arithmetic operators you are used to can be overloaded. The table below shows a partial list of arithmetic operators and the dunder methods they correspond to:

| Operator | dunder method | returns:
| -------- | ------- | ------- |
| x+y (add) | `__add__(self, other` | sum of x and y |
| x-y (subtract) | `__sub__(self, other)` | difference of x and y |
| x*y (multiply) | `__mul__(self, other)` | product of x and y |
| x/y (divide) | `__truediv__(self, other)` | quotient of x and y |
| x += y (adds y to x)| `__iadd__(self, other)` | modifies x by adding y, returns x |
| x -= y (subtracts y from x)| `__isub__(self, other)` | modifies x by subtracting y, returns x |
| x *= y (multiplies x by y)| `__imul__(self, other)` | modifies x by multiplying by y, returns x |
| x /= y (divides x by y)| `__itruediv__(self, other)` | modifies x by dividing it by y, returns x |


## Other dunder methods
For the scope of this course, the dunder methods above are sufficient. But if you are curious about what other dunder methods exist, here's an external website that is thorough: <a href="https://www.pythonmorsels.com/every-dunder-method/" target="_blank">https://www.pythonmorsels.com/every-dunder-method/</a>
