# The difference between "identity" (`is`) and "equality" (`==`) of objects

## Identity
In a previous section (<a href="https://cs.du.edu/~intropython/intro-to-programming-2/chapters/classes/variables_are_references.html" target="_blank">variables are references</a>), we noted that variables don't store objects themselves, but rather store references to objects. Recall also that we can use the python `id()` function to find the memory address where the objects are stored.

Consider the following code:
```python
class Point:

    def __init__(self, x, y):
        # initialize the values of the point (x, y)
        self.x = x
        self.y = y

    def __eq__(self, other: Point)->bool:
        return self.x==other.x and self.y==other.y
    
    def __str__(self)->str:
        return f"({self.x}, {self.y})"

# main code block:
point1 = Point(3, 5)
point2 = Point(3, 5)
point3 = point2
print(id(point1))
print(id(point2))
print(id(point3))
```
Since `point1` and `point2` were instantiated separately, they refer to two different objects. These objects are stored at different memory locations, so their ids are different (even though their contents are the same). On the other hand, `point3` refers to the same object as `point2`, so they have the same id.

Python provides another way to determine if two variables refer to the same object, using the keyword `is`.
```python
print(point1 is point2) # outputs False, because point1 and point2 have different ids (they refer to different objects)
print(point2 is point3) # outputs True, because point2 and point3 have the same ids (they refer to the same object)
print(point1 is point3) # outputs False, because point1 and point3 have different ids (they refer to different objects)
```

## Equality

If rather than comparing identities, we want to determine if the contents of the objects are the same, recall that we learned to use `==`, which automatically calls the `__eq__()` method:
```python
print(point1 == point2) # outputs True, because the x and y values for point1 and point2 are the same.
print(point2 == point3) # outputs True, because the x and y values for point2 and point3 are the same.
print(point1 == point3) # outputs True, because the x and y values for point1 and point3 are the same.
```

## What to remember from this:

Remember that `obj1 is obj2` determines if `obj1` and `obj2` have the same identity, while `obj1 == obj2` determines if `obj1` and `obj2` have the same values.

## Video explanations
<video src="https://cs.du.edu/~ftl/1352/videos/classes2/identity_v_equality.mp4" width="480" height="270" controls></video>

