## Using dunder methods to overload arithmetic operators
Suppose we have a class that it makes sense to do arithmetic with. For example, say I implement the `Point` class, where each point is a location in the (x, y) plane. In some contexts it is mathematically useful to add two points by separately adding their x and y coordinates. For example, (1, 3) + (6, 5) = (7, 8). Consider the following implementation of the `Point` class:
```python
class Point:

    def __init__(self, x: float, y: float):
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
We can "teach" python how to add objects of our `Point` class by implementing the method `__add__()` in our class. The `__add__()` method will automatically be called when python evaluates the expression `point1 + point2`. It takes two parameters, `self` and `other`, where the first summand `point1` takes the role of `self`, and the second summand `point2` takes the role of `other`. The `__add__()` method should create and return a new `Point`, whose values are the sums of the individual points. Here's the implementation, which is incorporated into the `Point` class:
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
(7, 8)
```
Note: the `__add__()` function could be condensed to one line:
```python
    def __add__(self, other: Point)->Point:
        return Point(self.x+other.x, self.y+other.y)
```
All of the arithmetic operators you are used to can be overloaded. The table below shows a partial list of arithmetic operators and the dunder methods they correspond to:

| Operator | dunder method | returns:|
| -------- | ------- | ------- |
| x+y (add) | `__add__(self, other)` | sum of x and y |
| x-y (subtract) | `__sub__(self, other)` | difference of x and y |
| x*y (multiply) | `__mul__(self, other)` | product of x and y |
| x/y (divide) | `__truediv__(self, other)` | quotient of x and y |
| x += y (adds y to x)| `__iadd__(self, other)` | modifies x by adding y, returns x |
| x -= y (subtracts y from x)| `__isub__(self, other)` | modifies x by subtracting y, returns x |
| x *= y (multiplies x by y)| `__imul__(self, other)` | modifies x by multiplying by y, returns x |
| x /= y (divides x by y)| `__itruediv__(self, other)` | modifies x by dividing it by y, returns x |


## Other dunder methods
For the scope of this course, the dunder methods above are sufficient. But if you are curious about what other dunder methods exist, here's an external website that is thorough: <a href="https://www.pythonmorsels.com/every-dunder-method/" target="_blank">https://www.pythonmorsels.com/every-dunder-method/</a>

## Video explanations
<video src="https://cs.du.edu/~ftl/1352/videos/classes2/arithmetic_dunder.mp4" width="480" height="270" controls></video>
