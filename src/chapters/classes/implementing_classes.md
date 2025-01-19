# How to implement a class

The template for the simplest class looks like this:

```
class NameOfClass:

    # Every class has an __init__ method, called a constructor, or initializer.
    # Notice that __init__ takes "self" as a parameter, as does every method in a class.
    # Instance variables will be initialized here; pass the initial values as parameters
    def __init__(self, pass initial values as parameter):
        pass

    def put_your_methods_here(self, put parameters here):
        pass
```

Recall from the previous section the interface of the `Rectangle` class:

<table>
    <tr>
        <td>Rectangle</td>
    </tr>
    <tr>
      <td>Instance variables and their types:<br>
    <code>center_x:float</code><br>
    <code>center_y:float</code><br>
    <code>width:float</code>code><br>
    <code>height:float</code>code></td>
      ```
    </tr>
    <tr>
      <td>methods (along with their parameters and return types):<br>
    <code>__init__(center_x:float, center_y:float, width:float, height:float)  # constructor (initialization method)</code><br>
    <code>draw(None)->None                   # display the rectangle</code>  <br>
    <code>area(None)->float                  # compute and return the rectangle area</code><br>
    </tr> 
</table>

The code below gives an implementation of the `Rectangle class`. Explanations of each component are given in the comments of the code. The code below also shows simple usage of the `Rectangle` class. A few `Rectangle` objects are instantiated, and their methods are invoked.

```
# implementation of the Rectangle class:
class Rectangle:

    # This is the constructor (or initializer). Every method must include "self" as the 
    # first parameter. The other parameters are used to initialize the instance variables
    # In this example, the parameters are given default values
    def __init__(self, center_x:float = 0, center_y:float = 0, width:float = 1, height:float = 1):
        # Each line below creates and initializes a new instance variable for this class.
        # Every object will have its own "copy" of each instance variable.
        # From within the class, each instance variable is accessed with the 
        # expression self.instance_variable_name
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height

    def draw(self)->None:
        # The instance variables self.center_x, self.center_y, self.width, and self.height
        # give the full information about how to draw the rectangle to a dudraw canvas.
        dudraw.filled_rectangle(self.center_x, self.center_y, self.width/2, self.height/2)

    # In this and all methods, "self" refers to the object that invoked (called) this function
    def area(self)->float:
        # The product of the instance variables self.width and self.height give the area.
        # Compute the area and return it to the caller.
        return self.width*self.height
    

# main code block, demonstrating how to use the Rectangle class:
dudraw.set_canvas_size(300, 300)
dudraw.set_x_scale(0, 10)
dudraw.set_y_scale(0, 10)
# Three rectangles are instantiated below. In other words, three objects of the Rectangle
# class are created. In each case, Rectangle() automatically calls the __init__() function
# in the Rectangle class, and four instance variables are created, storing the data 
# for each rectangle. Notice that in each case, one line of code automatically creates all
# of the instance variables for that object
rectangle1 = Rectangle(2, 3, 0.1, 0.2) # create a rectangle with center (2, 3), width 0.1, height 0.2
rectangle2 = Rectangle(4, 6, 0.15, 0.3) # create a rectangle with center (4, 6), width 0.15, height 0.3
# In this instantiation, since there are no parameters, default values are used for the instance variables
rectangle3 = Rectangle()
# The area() method belonging to the Rectangle class is called, using rectangle1. 
# Within the code in the area() method, self will be rectangle1, since rectangle1 
# is the calling object.
print(rectangle1.area())
# The draw() method belonging to the Rectangle class is called. Within the draw() method,
# "self" will refer to rectangle2, since rectangle2 is the calling objects. So the
# values for width and height will automatically be those of rectangle2. 
rectangle2.draw()
dudraw.show(10000)
```





