# Inheritance versus composition ("is a" versus "has a")

In object-oriented programming (OOP), there are multiple ways that classes can interact. We've seen two of them: inheritance (in which one class *is* an extension of another class) and composition (in which one class *has* instance variables of another class). Inheritance is informally referred to as an "is a" relationship (since an object of a derived class is *also automatically* an instance of its parent class). Composition is informally referred to as a "has a" relationship (since the class owns, or has, instances of another class). To illustrate the difference, here are two examples from previoius sections.

## Inheritance relationship

In the example below, `Circle` is a derived class (child class) of `Shape`, as indicated by the class definition: `class Circle(Shape)`. The relationship is an example of inheritance.

```python
class Shape:

    def __init__(self, x: float, y: float, c: dudraw.Color):
        self.x = x
        self.y = y
        self.color = c

class Circle(Shape):

    def __init__(self, x: float, y: float, r: float, c: dudraw.Color):
        super().__init__(x, y, c)
        self.radius = r

# main code block:
circle1 = Circle(0.5, 0.5, 0.2, dudraw.RED)
print(type(circle1))              # circle1 is of type Circle
print(circle1 instanceof Circle)  # True: circle1 is an instance of Circle
print(circle1 instanceof Shape)   # True: circle1 is an instance of Shape, by inheritance
```

In the above example, the type of `circle1` is `Circle`. Python outputs
`<class '__main__.Circle'>` (since the `Circle` class is defined within the `__main__` module).
The next line determines if `circle1` is an instance of the `Circle` class, which it is since it was instantiated as a `Circle` object.
The final line determines if `circle1` is also an instance of the `Shape` class. The result is again `True`. The object `circle1` is a `Circle`, and thus is also a `Shape`, since `Circle` is a child clcass of `Shape`.

## Composition relationship

Here is an abridged version of code from a previous section ([More complex classes](../classes1/complicated_classes.md)):
```python
class Point:

    def __init__(self, x: float, y: float):
        # initialize the values of the point (x, y)
        self.x = x
        self.y = y

class Triangle:

    def __init__(self, v1: Point, v2: Point, v3: Point):
        self.vertex1 = v1
        self.vertex2 = v2
        self.vertex3 = v3

# main code block
t1 = Triangle(Point(5, 2), Point(2, 5), Point(2, 2))
print(type(t1))
print(isinstance(t1, Triangle))  # True, t1 is a triangle
print(isinstance(t1, Point))     # False, t1 is not a Point
```

In the above code, we have two classes, but they are not related by inheritance. Instead, they are related by composition, since the `Triangle` class uses the `Point` class by owning instance variables of type `Point`. 

In the main code block, note that the type of `t1` is `Triangle`
(python outputs `<class '__main__.Triangle'>`, since the `Triangle` class is defined within the `__main__` module). The next line determines if `t1` is an instance of the `Triangle` class, which it is, since `t1` was instantiated as a `Triangle`. The final line, however, outputs `False`. The object `t1` *is not a* `Point`. Rather, it *has a* `Point` as one of its instance variables.