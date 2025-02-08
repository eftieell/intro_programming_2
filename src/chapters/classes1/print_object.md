# How to output the contents of an object to the terminal

For reference, in this section we will continue developing the `Rectangle` class created in the previous section:
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
```

The following line of code instantiates (creates) an object of type `Rectangle`:
```python
rectangle1 = Rectangle(2, 3, 0.1, 0.2) # create a rectangle with center (2, 3), width 0.1, height 0.2
```

Now suppose we want to output the contents of rectangle to the terminal. Naturally, we would try the following:
```python
print(rectangle1)
```
Disappointingly, the output to the terminal might look something like this:
```
<__main__.Rectangle object at 0x100afbfd0>
```
When we output the contents of the rectangle object to the terminal, python by default outputs the location in memory where
the object is stored. It does so because we have not included in the definition of the `Rectangle` class what format the output 
of a `Rectangle` object should look like. To fix this issue, we must include a method called `__str__` in the `Rectangle` class.
Its job is to build and return a string in the right format. If we have provided a `__str__` method, then python will automatically
look for and call that method when we ask it to print an object.  Here is the `__str__` method that we now include in the `Rectangle` class:
```python
    # produce a string to represent this rectangle. Note that python will automatically call this method 
    # to produce a string whenever print(rectangle_object) is executed
    # Example of what the formatted string will look like: center: (0.4, 1.2), width: 0.3, height: 0.5
    def __str__(self)->str:
        return f"center: ({self.center_x}, {self.center_y}), width: {self.width}, height: {self.height}"
```

After adding the `__str__` method to the `Rectangle` class, when we execute the lines
```python
rectangle1 = Rectangle(2, 3, 0.1, 0.2) # create a rectangle with center (2, 3), width 0.1, height 0.2
print(rectangle1)
```
the output is 
```
center: (2, 3), width: 0.1, height: 0.2
```
