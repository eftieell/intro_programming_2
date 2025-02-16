# Polymorphism

Object-oriented-programming really shines with the idea of polymorphism. The idea is simple and powerful. Recall in previous sections we saw that multiple classes that are related by inheritance could use method overriding so that each has a different version of a method with the same name. This means that if we have several of these objects, all of which potentially have different types, we can still sensibly store them all in one list. Then we can traverse that list, and call the method for each of them. The correct method will get called for each of them, based on each object's individual type.

# Example

Here we have the example from a previous section, more fully implemented:
```python
from random import random, randint 
import dudraw

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

    # This method overrides the draw() method in the Shape class
    def draw(self)->str:
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.x, self.y, self.radius)

class Rectangle(Shape):

    def __init__(self, x: float, y: float, w: float, h: float, c: dudraw.Color):
        super().__init__(x, y, c)
        self.width = w
        self.height = h

    def __str__(self)->str:
        return f"{super().__str__()}, rect width: {self.width:.4g}, rect height: {self.height:.4g}"

    # This method overrides the draw() method in the Shape class
    def draw(self)->str:
        dudraw.set_pen_color(self.color)
        dudraw.filled_rectangle(self.x, self.y, self.width, self.height)

class Ellipse(Shape):

    def __init__(self, x: float, y: float, w: float, h: float, c: dudraw.Color):
        super().__init__(x, y, c)
        self.width = w
        self.height = h

    def __str__(self)->str:
        return f"{super().__str__()}, ellipse x-rad: {self.width:.4f}, y-rad: {self.height:.4f}"

    # This method overrides the draw() method in the Shape class
    def draw(self)->str:
        dudraw.set_pen_color(self.color)
        dudraw.filled_ellipse(self.x, self.y, self.width, self.height)

def rand_color()->dudraw.Color:
    return dudraw.Color(randint(0, 255), randint(0, 255), randint(0, 255))

# main code block:
# Create a list of 40 shapes (10 each of Shape, Circle, Rectangle and Ellipse objects)
shapes = []
for i in range(10):
    shapes.append(Shape(random(), random(), rand_color()))
    shapes.append(Circle(random(), random(), random()*0.1, rand_color()))
    shapes.append(Rectangle(random(), random(), random()*0.1, random()*0.1, rand_color()))
    shapes.append(Ellipse(random(), random(), random()*0.1, random()*0.1, rand_color()))
# display all 40 objects
for shape in shapes:
    shape.draw()
# output a string representation of all 40 objects:
for shape in shapes:
    print(shape)

#dudraw.show(10000)
```
The implementation of these classes is the same as in the previous section. 
After orienting yourself to the code for the classes, please focus on the main code block.

In it, an empty list called `shapes` is first created. 
This list will hold references to a variety of different types of `Shape` objects.
Each time through the for-loop, a `Shape`, `Circle`, `Rectangle` and `Ellipse` object are instantiated and each appended to the list.
Note the key point here: the list `shapes` holds four different types of objects, we can treat them homogeneously. 
This is the concept of polymorphism!

After the list has been created, the next for-loop traverses the list and displays each object. 
The call `shape.draw()` works seamlessly, but don't miss the magic here: a different version of the `draw()` method is called depending on which type of object it is.
If the object is of the type `Shape`, then the `draw()` method in the parent class `Shape` is called. 
Otherwise, the appropriate overriding method is automatically invoked instead.
The last for-loop demonstrates another example of the same idea. 
This time, the `__str__()` method is called, depending on the type of the object.
If it is a `Shape`, then the `__str__()` method of the parent class is called.
But when it is one of the child classes, the child class's overriding version of `__str__()` is called. 
Each `__str__()` method in the child classes invokes the `__str__()` method of the parent to do the parent's part of the job.

