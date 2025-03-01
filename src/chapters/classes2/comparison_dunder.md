# Comparing objects using dunder methods (methods whose name starts with two underscores)

In python, methods that start with two underscores are called *dunder* (double-underscore) methods. They are sometimes also referred to as *special methods* or *magic methods*. These methods have special significance, since they are automatically invoked by python in certain situtations. You've seen two examples of this already: the `__init__()` function is automatically (or "magically") invoked when you instantiate an object, and the `__str__()` method is automatically invoked when you print an object, and the `__repr__` method is automatically invoked for each object when you print a list of objects. For example:

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

    def __repr__(self)->str:
        return self.__str__()

time1 = Time24(12, 7)   # automatically calls __init__ to initialize to 12:07
time2 = Time24(2, 43)   # automatically calls __init__ to initialize to 02:43
time3 = Time24(12, 7)   # automatically calls __init__ to initialize to 12:07
default_time = Time24() # also calls __init__, default time is 00:00
times = [time1, time2, time3, default_time]
print(time1)            # automatically calls __str__, outputs 12:07
print(times)            # automatically calls __repr__ for each object
```

Carefully read and trace the code above, paying special attention to how `__init__()` automatically gets called when we instantiate an object, how `__str__()` automatically gets called when we print an object, and how `__repr__()` automatically gets called when we print a list of objects.

Besides `__init__()` and `__str__()`, and `__repr__` methods, python has a long list of other dunder methods. First, we will learn the *rich comparison operators*, which allows us, whenever it makes sense, to compare two objects of a class using  the operators `<`, `<=`, `==`, <code>!=</code>, `>=`, and `>`.

## Using the == operator to compare two objects

Notice that two of the `Time24` objects above (`time1` and `time2`) represent the same time of day. What do you think is output by the following line of code?
```python
print(time1 == time3)
```
Are you disappointed to find out that the above line of code outputs `False`? By default, two objects evaluate as `==` in python when they represent the identical object (in other words, they stored in the same memory location, refer to the same object, or have the same `id()`). Said differently, when evaluating `==` for two objects, by default python does not compare the *contents* of the objects to see if the *contents are the same*. But when dealing with objects, comparing the contents is usually exactly what we want `==` to do. So python gives us a way to make the `==` comparison between objects compare the contents of the objects, according to a method we provide. This is called "overloading the `==` operator".

## How to overload the `==` operator
* Within the class, implement a method called `__eq__()`. 
* The `__eq__()` method defines in python code how to tell if two objects are `==`.
* The `__eq__()` method is automatically ("magically") called when you use `==` to compare two objects.
* The `__eq__()` method should return a `bool`.
* In our example, we will say two `Time24` objects equal if and only if they have the same values for hour and the same values for minutes. 
* The `__eq__()` method should take two parameters. The object on the
left side of `==` becomes `self`, and the object on the right side of the `==` becomes the second parameter, typically named `other`.

Include this code in the `Time24` class:
```python
    def __eq__(self, other)->bool:
        # Evaluate two Time24 objects as "==" if both of their instance variables (hours and minutes) are equal
        return self.hours == other.hours and self.minutes == other.minutes
```

Now the following line outputs `True`, as desired:
```python
print(time1 == time3)  # automatically calls the __eq__ method from the Time24 class, time1 is self, time3 is other
```

Whenever you overload the `==` operator by implementing `__eq__()` in your class, you should also overload the <code>!=</code> operator by implementing `__ne__()` in your class. Rather than modifying the code in `__eq__()`, in `__ne__()` you can just return the logical negation of the result of `__eq__()`. Include this method in the `Time24` class:

```python
    def __ne__(self, other)->bool:
        return not self==other  # notice that this calls __eq__() automatically
```

## Using the < operator to compare two objects

We would like the following line to output `False`, since time2 is 2:43 in the morning, and time2 is in the afternoon:
```python
print(time1 < time2)
```
But here's the output:
```
TypeError: '<' not supported between instances of 'Time24' and 'Time24'
```
When objects in a class have a natural linear ordering, then it makes sense to compare them with the `<` operator. To implement this in python, we provide a `__lt__()` method in our class. The `__lt__()` method should return a boolean, and take two parameters. The `__lt__()` method will automatically be called when the code `object < object2` is evaluated, with `object1` becoming the parameter `self`, and `object2` becoming the parameter `other`. For example, here is an implementation of `__lt__()` for our `Time24` class. Insert this code into the class.
```python
    def __lt__(self, other)->bool:
        if self.hours < other.hours:
            return True
        elif self.hours > other.hours:
            return False
        else:
            return self.minutes < other.minutes
```
Here is some demo code to show how the `__lt__()` method gets called:
```python
print(time1 < time2)        # calls __lt__(), outputs False (time2 is earlier in the day)
print(time1 < time3)        # outputs True (they are equal, so time1 isn't less than time3)
print(default_time < time2) # outputs True, midnight is earlier than every other time

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

## Video explanations
<video src="https://cs.du.edu/~ftl/1352/videos/classes2/comparison_dunder.mp4" width="480" height="270" controls></video>
