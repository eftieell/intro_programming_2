# Classes and Creating Objects

## Motivation
In python, a variable of type int, float, char, etc. can be used to store and reprsent one value.
But often one needs multiple values to represent one concept, or one object. For example:
* a point in two-dimensional space is represented by two variables (x, y),
* a rectangle has a center point, a width and a height,
* a college registrar stores many pieces of information about each student (name, address, year in school, gpa, etc.),
* a bouncing circle in an animation has an x-position, a y-position, a size, an x-velocity, a y-velocity, and a color.

We see the advantage of bundling the multiple variables that represent an object in the above examples. The x and y values for a point should be stored together, as should the multiple pieces of information about a college student's record, or information for a bouncing circle in an animation.

All high-level programming languages give you a way to package multiple variables into one object. In object-oriented languages (including python), the idea goes further. You can uses classes to package **data** together with the **code** that manages and manipulates that data.

Example: Suppose we want to write python code to store data for a rectangle, together with code to manage and manipulate that data. We would do this by implementing a class called <code>Rectangle</code>, and would specify that the class store the variables <code>center_x</code>, <code>center_y</code>, <code>width</code>, and <code>height</code>. Variables that are part of a class are called *instance variables*. We would also specify it to have built-in functions to manage the rectangle, such as a function that would compute the area of the rectangle, or a function that would draw the rectangle. Functions that are part of a class are called *methods*.

The diagram below (a modified version of a UML diagram) shows the name of the class, the instance variables and their types, and the methods (with the parameter types and return value types):

<table>
    <tr>
        <td><center>Rectangle</center></td>
    </tr>
    <tr>
      <td>Instance variables and their types:<br>
    <code>center_x: float</code><br>
    <code>center_y: float</code><br>
    <code>width: float</code><br>
    <code>height: float</code></td>
    </tr>
    <tr>
      <td>methods (along with their parameters and return types):<br>
    <code>__init__(center_x: float, center_y: float, width: float, height: float)  # constructor (initialization method)</code><br>
    <code>draw(None)->None                   # display the rectangle</code>  <br>
    <code>area(None)->float                  # compute and return the rectangle area</code><br>
    </tr> 
</table>

Once the <code>Rectangle</code> class has been implemented (either by ourselves or by someone else), just knowing the above interface allows us to use the class, even without knowing details about how it is implemented. This illustrates the concept of *abstraction*. The complexity of the implementation is hidden from the user of the Rectangle class.

## Objects
In the above example, once the <code>Rectangle</code> class has been implemented, other programmers can use that class, trusting that it was implemented correctly, without bothering themselves with how it was implemented. Any programmer wanting to store information about a rectangle and potentially compute its area or display it, would create one <code>Rectangle</code> object for each rectangle they want to represent. Each <code>Rectangle</code> object is treated like a single variable. That single variable is made up of multiple components, namely a <code>center_x</code>, <code>center_y</code>, <code>width</code> and <code>height</code>, as well as some methods (functions) for manipulating that rectangle.

Think of the Rectangle class as a "cookie cutter" that we can use to create multiple "cookies" (rectangles).

## How to create objects - example
To create a new rectangle object, we state the name of the class, and pass the required initialization parameters. This calls the constructor (or initialization method).
```python
rectangle1 = Rectangle(2, 3, 0.1, 0.2)  # create a rectangle with center (2, 3), width 0.1, height 0.2
rectangle2 = Rectangle(4, 6, 0.15, 0.3) # create a rectangle with center (4, 6), width 0.15, height 0.3
```
The first line of code above creates (or *instantiates*) a new <code>Rectangle</code> object. This object has variable name <code>rectangle1</code>, and is a bundle of four instance variables (<code>center_x</code>, <code>center_y</code>, <code>width</code> and <code>height</code>). Note that the single line of code automatically creates 4 separate variables that are bundled together. The second line of code instantiates a second new <code>Rectangle</code> object. Again, a single line of code creates a bundle of 4 variables. The code that creates those 4 variables is in the `Rectangle` class's `__init__` function.

## Using (or invoking) methods
Once we have created an object, we can invoke the methods associated with it using the expression <code>object_name.method_name()</code>.
For example, the code below outputs the area of the object <code>rectangle1</code> that we instantiated above:
```python
print(rectangle1.area())
```
The next line of code displays to the `dudraw` canvas <code>rectangle2</code> that we instantiated above:
```python
rectangle2.draw()
```
## Accessing the data elements in an object
The data for an object is stored in its instance variables. You can access these values with the expression <code>object_name.instance_variable_name</code>. The following  lines of code output the values stored in the rectangles we created above:
```python
print(f"Center point of rectangle1: ({rectangle1.center_x}, {rectangle1.center_y})")
print(f"width and height of rectangle2: width = {rectangle2.width}, height = {rectangle2.height}")
```
Note about object-oriented programming: in good object-oriented programming practice, users of a class should never modify the contents of the instance variables directly - rather the contents should be modified in the code internal to the class. Often this is done through *setter* methods (also called *mutators*).
In fact, in true object-oriented languages (such as C++ or Java), code that uses a class may not even *see* the contents of the instance variables directly - they must access them using *getter* methods (also called *accessors*).

## More about abstraction

Notice that in the examples above, we wrote code that uses a class (the <code>Rectangle</code> class) just by knowing the interface of the class (described in the UML diagram shown above). We did so above without ever having seen the code that implements the class. Doing so relies on us confidently using the code written either by someone else or ourselves at a different time. By abstracting the data and functionality of the class, we're able to implement, debug, and test the two parts of the code (i.e., implement the class, and then use the class) completely separately. Breaking the code into separate units means we can implement very large programs by writing and testing just parts of it at a time.

## Strings are objects

We've actually used classes before this. When you create a string in python, it is an object of the <code>str</code> class. For example:
```python
name = "Bessie Mae "
print(name.count('e'))           # outputs the number of e's in name
lower_case_name = name.lower()   # name.lower() returns a new string object, with all letters now lower-case
first_name = name.split()[0]     # extract the first word of the string
```
In the code above, we are invoking three different methods from the <code>str</code> class (<code>count()</code>, <code>lower()</code>, and <code>split()</code>). Notice that <code>name.count()</code>, <code>name.lower()</code>, and <code>name.split()</code> all fit the pattern <code>object_name.method_name()</code>.
You can find the official python documentation listing all available methods in the <code>str</code> class here: <a href = "https://docs.python.org/3/library/stdtypes.html#string-methods" target = "blank">https://docs.python.org/3/library/stdtypes.html#string-methods</a>

## Summary of why we use classes and objects
Programming with classes and objects:
* helps you to better organize complex code,
* makes it easier to create reusable code,
* allows you to write, test, and debug segments of code separately,
* results in code that is more maintainable,
* enables you to break down large programs into subtasks that different people can implement,
* and creates encapsulation (compartmentalizes data so that one part of a program cannot corrupt data managed by another part of the program).

## Video explanations
Motivation and concepts for classes and objects:

<video src="https://cs.du.edu/~ftl/1352/videos/classes1/classes_intro_part1.mov" width="480" height="270" controls></video>

Code example using classes and objects:

<video src="https://cs.du.edu/~ftl/1352/videos/classes1/classes_intro_part2.mp4" width="480" height="270" controls></video>


