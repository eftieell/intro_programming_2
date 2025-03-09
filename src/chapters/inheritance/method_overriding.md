# Method overriding

Consider the following implementation of the `Shape` and `Circle` classes:
```python
class Shape:

    def __init__(self, x: float, y: float, c: dudraw.Color):
        self.x = x
        self.y = y
        self.color = c

    def __str__(self)->str:
        # the ".4g" formatting specification outputs at most 4 decimal places
        return f"center: ({self.x:.4g}, {self.y:.4g}), color: {self.color}"
    
    def draw(self):
        dudraw.set_pen_color(self.color)
        dudraw.point(self.x, self.y)

class Circle(Shape):

    def __init__(self, x: float, y: float, r: float, c: dudraw.Color):
        super().__init__(x, y, c)
        self.radius = r

    def __str__(self)->str:
        return f"{super().__str__()}, circle radius: {self.radius:.3g}"

# main code block:
shape1 = Shape(0.6, 0.2, dudraw.BLUE)
shape1.draw()
circle1 = Circle(0.5, 0.25, 0.075, dudraw.RED)
circle1.draw()
dudraw.show(10000)
```

Trace the main code block carefully. Notice that we instantiate a `Shape` object called `shape1`. It has instance variables `x`, `y`, and `color`. When `shape1.draw()` is called, a point is drawn to the (x, y) location, in the right color. Then a `Circle` object called `circle1` is instantiated, and its instance variables are initialized. Notice it has instance variables `x`, `y`, and `color` inherited from its parent class `Shape`, as well as an instance variable for its radius. On the next line, you might be fooled by the call `circle1.draw()`. If you're thinking that the program will crash on that line, since the `Circle` class does not have a `draw()` method, you've forgotten that `Circle` *inherits all attributes* from `Shape`. So the `draw()` method from `Shape` gets called!  Sadly, `Shape`'s `draw()` method just draws a point. This is not how we want to draw a circle. The solution is to *override* the `draw()` method.

## How to override methods

Not much to it: just implement a `draw()` method in `Circle` that does the task specific to `Circle` objects. Although `Circle` already had a `draw()` method (the one it inherited from `Shape`), we provide a second `draw()` method within the definition of `Circle`, and that method overrides the one in its parent class (base class).

```python
class Shape:

    def __init__(self, x: float, y: float, c: dudraw.Color):
        self.x = x
        self.y = y
        self.color = c

    def __str__(self)->str:
        return f"center: ({self.x}, {self.y}), color: {self.color}"
    
    def draw(self):
        dudraw.set_pen_color(self.color)
        dudraw.point(self.x, self.y)

class Circle(Shape):

    def __init__(self, x: float, y: float, r: float, c: dudraw.Color):
        super().__init__(x, y, c)
        self.radius = r

    def __str__(self)->str:
        return f"{super().__str__()}, radius: {self.radius}"

    # This method overrides the draw() method in the Shape class
    def draw(self):
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.x, self.y, self.radius)

# main code block:
dudraw.set_canvas_size(400, 400)
shape1 = Shape(0.6, 0.2, dudraw.BLUE)
shape1.draw()
circle1 = Circle(0.5, 0.25, 0.075, dudraw.RED)
# Now that Circle has its own draw() method that overrides the one in the,
# base class Shape, the line below calls the draw() method from Circle.
circle1.draw()
dudraw.show(10000)
```

## Another example

For reference, here is another example. Trace the following code carefully and predict the output. To learn well from this example, in the main code block pay close attention to which version of each method gets called. Sometimes the method in the child class calls the parent to do some of the work, and sometimes the method in the child class fully overrides the
method in the parent class.
```python
class Employee:

    # initialization method - Employees of all
    # types must have a name and an id
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id

    # produce a string representation of this Employee's information
    def __str__(self)->str:
        return f"{self.name}: id: {self.id}"
    
    def issue_paycheck(self):
        print(f"Employee {self.name} is unpaid.")

# HourlyEmployee is a child clss of Employee
class HourlyEmployee(Employee):

    def __init__(self, name: str, id: str, wage: float = 0, hours: float = 0):
        # Have base class do its part of the initialization
        super().__init__(name, id)
        # Now create instance variables specific to this derived class
        self.wage = wage
        self.hours = hours

    def __str__(self)->str:
        return f"{super().__str__()}, wage: {self.wage}, hours: {self.hours}"

    # return amount owed to worker, rounded to nearest penny
    def unpaid_wages(self)->float:
        if self.hours <= 40:
            return round(self.wage*self.hours, 2)
        else:
            # Time-and-a-half for overtime
            return round(self.wage*40 + 1.5*self.wage*(self.hours-40), 2)

    # print a paycheck to worker resetting hours worked
    def issue_paycheck(self):
        print(f"Printing paycheck for ${self.unpaid_wages()} written to {self.name}")
        self.hours = 0

# SalariedEmployee is a child clss of Employee
class SalariedEmployee(Employee):

    def __init__(self, name: str, id: str, weekly_salary: float = 0):
        # Have base class do its part of the initialization
        super().__init__(name, id)
        # Now create instance variables specific to this derived class
        self.weekly_salary = weekly_salary

    def __str__(self)->str:
        return f"{super().__str__()}, weekly_salary: {self.weekly_salary}"

    # print a paycheck to worker resetting hours worked
    def issue_paycheck(self):
        print(f"Printing weekly paycheck for ${self.weekly_salary} written to {self.name}")

# main code block:
worker0 = Employee("Winona Begay", "345176")
worker1 = HourlyEmployee("Suresh Batra", "212567", 34.50, 30)
worker2 = SalariedEmployee("Karala Lyberth", "618420", 1290.75)
print(worker0)
print(worker1)
print(worker2)
worker0.issue_paycheck()
worker1.issue_paycheck()
worker2.issue_paycheck()
```
Output:
```
Winona Begay: id: 345176
Suresh Batra: id: 212567, wage: 34.5, hours: 30
Karala Lyberth: id: 618420, weekly_salary: 1290.75
Employee Winona Begay is unpaid.
Printing paycheck for $1035.0 written to Suresh Batra
Printing weekly paycheck for $1290.75 written to Karala Lyberth
```



