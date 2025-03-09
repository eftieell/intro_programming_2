# Lists of objects

If we have many objects, we can store them in a list. This use of classes highlights their power.

## Example
Let's use the class `Rectangle` that we implemented in the previous section. For reference, here is the code:
```python
# implementation of the Rectangle class:
class Rectangle:

    # Constructor (initializer)
    def __init__(self, center_x:float = 0, center_y:float = 0, width:float = 1, height:float = 1):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height

    # Display to dudraw canvas
    def draw(self)->None:
        dudraw.filled_rectangle(self.center_x, self.center_y, self.width/2, self.height/2)

    # Compute and return area
    def area(self)->float:
        return self.width*self.height
    
    def __str__(self)->str:
        return f"center: ({self.center_x}, {self.center_y}), width: {self.width}, height: {self.height}"
```

## Instantiating (creating) a list of objects
We will now create 100 `Rectangle` objects with random centers, each with width and height of 0.02, and store them in a list. 
Please note how short and simple this code is! First create an empty list to store the rectangles. 
Then, within a for loop, instantiate (create) a new `Rectangle` object, 
passing random values for the center, and 0.02 for the width and height. 
Finally, append that new rectangle to the list of rectangles.

```python
# The following short segment of code creates 100 rectangle objects, with random centers
# and fixed width and height
rectangles = []
for i in range(100):
    new_rectangle = Rectangle(random.random(), random.random(), 0.02, 0.02)
    rectangles.append(new_rectangle)
```

Side note: the same list could be created in one line using list comprehension:
```python
rectangles = [Rectangle(random.random(), random.random(), 0.02, 0.02) for i in range(100)]
```

## Traversing (iterating over) the list of objects
Now that all 100 of our rectangles are stored in one list, we can iterate over that list, doing whatever we want with
each rectangle. For example, the following code displays all 100 rectangles to a dudraw canvas:
```python
# This content-based loop iterates over each rectangle, displaying it 
# by calling its draw() method
for rectangle in rectangles:
    rectangle.draw()
dudraw.show(10000) # display for 10 seconds
```

Note that the above loop could alternately have been implemented with an index-based loop:
```python
for i in range(len(rectangles)):
    rectangles[i].draw()
dudraw.show(10000)
```

As another example, here's a loop that calculates the total area of all of the rectangles:
```python
total_area = 0
for rectangle in rectangles:
    total_area += rectangle.area()
print(total_area)
```
Exercise for you: convert the above code to an index-based loop.

As a third example of iterating over a list of objects, here is a loop that outputs to the terminal the data stored in the `rectangle` list. 
On the second line, python automatically calls the `__str__()` method we implemented in the `Rectangle` class.
```python
for i in range(len(rectangles)):
    print(rectangles[i])
```
Exercise for you: convert the above code to a content-based loop.

## A quirk of python when printing lists of objects
It would be very natural for you to think that the following line would output the contents of each rectangle in the list `rectangles`:
```python
print(rectangles)
```
Since we have implemented `__str__()`, it seems like `__str__()` should be called for every element in the list we are outputting.
However, in python if we print our list of objects, the memory address of each object is output:
```
[<__main__.Rectangle object at 0x1024dcf10>, <__main__.Rectangle object at 0x10263df30>, <__main__.Rectangle object at 0x1032797e0>,
<__main__.Rectangle object at 0x104919900>, <__main__.Rectangle object at 0x104919960>, <__main__.Rectangle object at 0x1049199c0>,
...
```
There is a way around this. When outputting a list of objects, python automatically calls the `__repr__()` method, not the `__str__()` method.
Let's implement the `__repr__()` method in our `Rectangle` class (having it just call our existing `__str__`() method).
Add this method to our `Rectangle` class:
```python
    def __repr__(self)->str:
        return self.__str__()
```
Now when we execute the line:
```python
print(rectangles)
```
we get our desired output:
```
[center: (0.8229662378956932, 0.564174022001409), width: 0.02, height: 0.02, center: (0.16580614832245955, 0.17398244134557717), width: 0.02, height: 0.02,
center: (0.6660610136763881, 0.9802962789008293), width: 0.02, height: 0.02, center: (0.5937968938322629, 0.655517849943249), width: 0.02, height: 0.02,
...
```
It is good programming practice in python to implement a `__repr__()` method in every class.

Note: in python, there is another official purpose for `__repr__()` methods, 
so in future work you might be required to have `__repr__()` produce strings with a different format than `__str__()`.

## Video explanations
<video src="https://cs.du.edu/~ftl/1352/videos/classes1/list_of_objects.mp4" width="480" height="270" controls></video>
