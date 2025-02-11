# Class variables

## How to create and use class variables


Recall that each object of a class has its own copy of each *instance variable*. On the other hand, there is a way to create variables that are shared by every object of the class - these are called *class variables*.

Key differences between instance variables and class variables:

* Each object has its own copy of every instance variable. But there is only one value stored for a class variable, shared by all objects.
* Instance variables are most commonly created within the `__init__()` method of a class. On the other hand, class variables are created within the class, but *outside* of any method.
* If an object makes changes to a class variable, that change is seen by every object (since the variable is shared). If an object makes changes to one of its instance variables, no other objects see a change to their own instance variables.
* To access an instance variable, we say `object_name.instance_variable_name`. But to access a class variable, we say `ClassName.class_variable_name`.

### Use case 1 - defining constants that are shared program-wide

Here's an example:
```python
class Star:

    # speed of light in miles per second
    # (this is a class variable)
    speed_of_light = 186000

    def __init__(self, name, mass, age, distance):
        self.name = name
        # store the mass, unit is number of times the mass of our sun
        self.mass = mass
        # store the age, unit is billions of years
        self.age = age
        # store the distance from earth, in light-years
        self.distance = distance

    def __str__(self)->str:
        return f"{self.name}, mass: {self.mass} times Sol, age: {self.age}x10^9 years, distance: {self.distance} l.y."

    def distance_in_miles(self)->float:
        # miles = light years * seconds per year * speed of light in miles/second
        return self.distance * (60 * 60 * 24 * 365) * Star.speed_of_light

# main code block follows:
# Note the use of named parameters in the next two lines that instantiate Star objects
alphaA = Star(name = "Alpha Centauri A", mass = 1.1, age = 5.3, distance = 4.37)
sirius = Star(name = "Sirius - the Dog Star", mass = 2.0, age = 0.2, distance = 8.6)
# Note that the next two lines automatially call the __str__() method for Star
print(alphaA)
print(sirius)
# Demonstration of calling the distance_in_miles() method (which internally uses the Star.speed_of_light class variable)
print(f"distance of {alphaA.name} from earth: {int(alphaA.distance_in_miles())} miles")
print(f"distance of {sirius.name} from earth: {int(sirius.distance_in_miles())} miles")
# Demonstration that clients of the Star class can access class variables
print(f"The speed of light is {Star.speed_of_light} miles per second.")
```
output:
```
Alpha Centauri A, mass: 1.1 times Sol, age: 5.3x10^9 years, distance: 4.37 l.y.
Sirius - the Dog Star, mass: 2.0 times Sol, age: 0.2x10^9 years, distance: 8.6 l.y.
distance of Alpha Centauri A from earth: 25633091520000 miles
distance of Sirius - the Dog Star from earth: 50444985600000 miles
The speed of light is 186000 miles per second.
```

What to notice in the above example:
* The variable `speed_of_light` is defined *within* the class `Star`, but outside of any method definition. This is how we know it is a class variable.
* Since `speed_of_light` is a class variable, it is shared by all objects of the class. We use a class variable in this case to define a single constant that all objects of the class can access. (There are other uses of class variables - see below.)
* Since class variables are conventionally accessed with `ClassName.class_variable_name`, in this example all objects can access the class variable with the expression `Star.speed_of_light`. 
* Look closely at the `distance_in_miles()` method of the `Star` class. This is where you see the use of the class variable `Star.speed_of_light`.
* Notice that client code (the main code block) can also access class variables with `ClassName.class_variable_name`, as seen in the last line of the code, where `Star.speed_of_light` is output. Although viewing the values stored in a class variable from outside the class is legitimate, it is bad programming practice to modify class variables from outside the class, even though python allows it. Other object-oriented programming languages (C++, Java) have mechanisms for disallowing it.
* Technical note: in python it is also possible to access class variables using the object name (i.e., `object_name.class_variable_name` rather than `ClassName.class_variable_name`. For example, in the above code, you can use the expression `self.speed_of_light` within the class definition, or `alphaA.speed_of_light` within the client code. However, this practice is strongly discouraged, since if you attempt to mutate (modify) the class variable with this notation, a new instance variable is created with that same name rather than modifying the class variable. This causes unexpected side-effects. Thus, it is widely accepted as good python programming practice to always use the notation `ClassName.class_variable_name`.

## Other applications of class variables

### Use case 2 - counting the number of objects that have been instantiated
Because class variables are shared, we can use them to track events that occur class-wide. For example, we can use a class variable to count how many objects of a class have been instantiated. For example:

```python
class Widget:

    # The class variable Widget.count will keep track of how many Widget objects
    # have been instantiated
    count = 0

    def __init__(self, number):
        # create and initialize whatever instance variables are needed:
        self.number = number
        # This __init__() method gets called each time a Widget is instantiated, so
        # by updating the shared variable Widget.count, we can keep track of how
        #  many times this __init__() method has been called, 
        # and thus how many Widget objects there are.
        Widget.count = Widget.count + 1

# main code block:
# instantiate three Widget objects. Each time, the __init__() method is
# called, so Widget.count gets incremented
widget1 = Widget(17)
widget2 = Widget(23)
widget3 = Widget(47)
# The next line outputs 3, since Widget's __init__() method got called 3 times
print(Widget.count)
```

In the above code, the class variable `Widget.count` keeps track of the number of times a `Widget` object was instantiated. Since instantiation always calls the `__init__()` method, within that method we increment the class variable `Widget.count` to track the total number of `Widget` objects.

### Use case 3 - counting the total number of times that methods within a class have been invoked (called)

This time we will create another class variable to keep track of the total number of times any method within our class was invoked (called). We can keep track by having every method within the `Widget` class increment that shared class variable. The following code implements this idea.

```python
class Widget:

    # The class variable Widget.count will keep track of how many Widget objects
    # have been instantiated
    count = 0
    # The class variable Widget.method_calls will keep track of the total number of
    # times any method in Widget has been invoked
    method_calls = 0

    def __init__(self, number):
        # create and initialize whatever instance variables are needed:
        self.number = number
        # This __init__() method gets called each time a Widget is instantiated, so
        # by updating the shared variable Widget.count, we can keep track of how
        #  many times this __init__() method has been called, 
        # and thus how many Widget objects there are.
        Widget.count = Widget.count + 1
        # Count this call towards total method calls
        Widget.method_calls += 1

    def __str__(self)->str:
        # Count this towards total method calls:
        Widget.method_calls += 1
        # return the string representation
        return f"Widget value: {self.number}"

    def grow(self, increase):
        # This method modifies the value of the instance variable
        self.number += increase
        # Count this towards total method calls:
        Widget.method_calls += 1

# main code block:
# instantiate two Widget objects.
widget1 = Widget(17)
widget2 = Widget(23)
# increase the values stored in the widgets
widget1.grow(100)
widget1.grow(200)
widget2.grow(1000)
# output the contents of each of the two Widgets (automatically calls __str__()):
print(widget1)
print(widget2)
# output the values of the class variables:
print(f"Number of Widgets: {Widget.count}")
print(f"Number of Widget method calls: {Widget.method_calls}")
```

output:
```
Widget value: 317
Widget value: 1023
Number of Widgets: 2
Number of Widget method calls: 7
```
Carefully trace the code above to verify how the (shared) class variable `Widget.method_calls` tracks the
method calls, and confirm for yourself that there were 7 method calls in the main code block.

### Use case 4

Often it is important to give people or objects unique identification numbers. Examples of this in real life are Social Security numbers (no two individuals can share the same number) or student id numbers (every student at DU has a different 87-number). In python, one way to give every object of a class a unique id is to maintain a class variable that keeps track of the next available id to assign to each subsequent object. When an object is instantiated, in the `__init__`() method an instance variable is created to store that object's id, and it is to the next available id (stored in the class variable). Next, still within the `__init__()` method, the value of that class variable is incremented so that when the subsequent object is instantitated, its id will not collide with this or any previous object. In the example below, a class is used to represent financial transations. Each financial transaction is given its own unique transaction identification number.

```python
class FinancialTransaction:

    # The class variable FinancialTransaction.next_unique_id keeps
    # track of next available id, which will be assigned to each new
    # FinancialTransaction object. The first id assigned is 20000
    next_unique_id = 20000

    def __init__(self, source: int, destination: int, amount: float):
        # routing number and account number of source of funds
        self.source = source
        # routing number and account number for deposit
        self.destination = destination
        # dollar amount of the transaction
        self.amount = amount
        # set the id number of this transaction to the next available number
        self.id = FinancialTransaction.next_unique_id
        # Update the next available id (since we just used up the current one)
        FinancialTransaction.next_unique_id += 1
    
    def __str__(self)->str:
        return f"id: {self.id}, source: {self.source}, destination: {self.destination}, amount: {self.amount}"

# main code block:
# create two transaction objects
transaction1 = FinancialTransaction(2345678900123, 1234567800987, 1223.47)
transaction2 = FinancialTransaction(1234567800987, 9876543200987, 2319.24)
print(transaction1)
print(transaction2)
```
output:
```
id: 20000, source: 2345678900123, destination: 1234567800987, amount: 1223.47
id: 20001, source: 1234567800987, destination: 9876543200987, amount: 2319.24
```
Notice above that each id assigned is unique to that particular `FinancialTransaction` object. This technique guarantees no collisions of transaction id numbers.




