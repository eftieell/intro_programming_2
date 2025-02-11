# Classes can have a simple, or more complicated structure

We'll start with a simple class, and then show how it can be used to build more complicated and useful classes.
## A simple class
Consider the following code. Read it closely and predict the output.
```python
from __future__ import annotations
class Point:

    def __init__(self, x: float, y: float):
        # initialize the values of the point (x, y)
        self.x = x
        self.y = y

    def __str__(self)->str:
        # format the string in (x, y) form
        return f"({self.x}, {self.y})"
    
    # Change the location of this point, shifting it by the amount indicated by other.
    # Side note: notice that the header indicates that the second parameter is of type Point.
    # In order to define types that are user-defined classes, you need the import statement
    # from __future__ import annotations (and it has to be the first import).
    def shift(self, shift_by: Point)->None:
        self.x += shift_by.x
        self.y += shift_by.y
    
    
# main code block:
p1 = Point(4, 1)
print(p1)
p1.shift(Point(3, 4))
print(p1)
```
Answer:
```
(4, 1)
(7, 5)
```

# A more complicated class
We will use the `Point` class above to make a class called `Triangle`. 
Since a triangle has three vertices, our `Triangle` objects will have three instance variables 
(`self.vertex1`, `self.vertex2`, and `self.vertex3`), each of which is themself an object, of type `Point`.
This nesting of classes is common in object-oriented programming. Trace carefully through the following code and
predict the output to the terminal.

```python
class Triangle:

    def __init__(self, v1: Point, v2: Point, v3: Point):
        self.vertex1 = v1
        self.vertex2 = v2
        self.vertex3 = v3

    def __str__(self)->str:
        return f"Vertices: {self.vertex1} {self.vertex2} {self.vertex3}"

    def shift(self, shift_by: Point)->None:
        self.vertex1.shift(shift_by)
        self.vertex2.shift(shift_by)
        self.vertex3.shift(shift_by)

# main code block:
p1 = Point(4, 1)
p2 = Point(7, 1)
p3 = Point(5, 2)
t1 = Triangle(p1, p2, p3)
print(t1)
t1.shift(Point(3, 4))
print(t1)
```
Output:
```
Vertices: (4, 1) (7, 1) (5, 2)
Vertices: (7, 5) (10, 5) (8, 6)
```

The variable `t1` has three instance variables, each of which are points. 
For example, `t1.vertex1` represents the point (4, 1). Notice that since `t1.vertex` is a `Point`, 
we can actually access its two instance variables, with `t1.vertex.x` and `t1.vertex.y`. 
However, in object-oriented programming practice, by convention we never modify an
instance variable's instance variable. Instead, we rely on that class to do the modification. 
You can see an example of this in the code above: the `shift` method in the `Triangle` class does not itself change the values of each vertex. 
Instead, it calls the `Point` class's `shift()` method
to modify the `x` and `y` values of each of the three vertices.

## A class with a list as an instance variable

Below we define and use the class `Polygon`. It has one instance variable, which is a list of its vertices
(each of which is a `Point` object). 
Notice that the methods in this class will often need to traverse through that list of vertices.
In the code below, you see these loops both in the `__str__()` method and the `shift()` method. Notice two different styles of iteration (looping through index or looping through content) are used, 
so you can see different options. Carefully trace the code and predict the output to the terminal.
```python
class Polygon:
    def __init__(self, vertices:list):
        self.vertices = vertices

    def __str__(self)->str:
        result = "vertices: "
        for point in self.vertices:
            result += str(point) + " "
        return result
    
    def shift(self, shift_by: Point):
        for i in (range(len(self.vertices))):
            self.vertices[i].shift(shift_by)

# main code block:
vertices = [Point(4, 0), Point(0, 4), Point(4, 8), Point(8, 4)]
poly = Polygon(vertices)
print(poly)
poly.shift(Point(10, 20))
print(poly)
```
Output:
```
vertices: (4, 0) (0, 4) (4, 8) (8, 4) 
vertices: (14, 20) (10, 24) (14, 28) (18, 24) 
```