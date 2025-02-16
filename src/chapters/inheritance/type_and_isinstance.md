# Determining types of objects using `type` and `isinstance`

You learned about the python `type()` function in the first weeks of programming. For example:

```python
age = 5
movie_title = "The Princess Bride"
print(type(age))          # outputs <class 'int'>
print(type(movie_title))  # outputs <class 'str'>
```

This idea extends to objects of user-defined classes. For example:
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
shape1 = Shape(0.25, 0.75, dudraw.ORANGE)
circle1 = Circle(0.5, 0.5, 0.2, dudraw.RED)
print(type(circle1)) # outputs <class '__main__.Circle'>
print(type(shape1))  # outputs <class '__main__.Shape'>
```

(The output is not simply `<class Circle>`, but rather includes `__main__`, which is the module name where the `Circle` class was defined.)

The python `type()` function returns the name of class that the object was instantiated as. But by virtue of inheritance, note that `circle1` is both a `Circle` and a `Shape`. To elicit this information from program control, we can use python's `isinstance()` function. The `isinstance()` function takes two parameters: the first is an object, and the second is a class. For example:

```python
print(isinstance(circle1, Circle))  # True (circle1 was instantiated as a Circle)
print(isinstance(circle1, Shape))   # True, by inheritance. Every Circle is a Shape
print(isinstance(shape1, Shape))    # True (shape1 was instantiated as a Shape)
print(isinstance(shape1, Circle))   # False, shape1 is not an instance of the child class Circle
```