# Review of producing animations using the dudraw graphics package

Basic information about creating drawings using `dudraw` can be found here: [dudraw basics](https://cs.du.edu/~intropython/intro-to-programming/dudraw_quickstart.html). This section assumes you can create basic drawings, and contains a review of how to animate drawings using the `dudraw` package.

Here is the basic outline of a `dudraw` animation program:

```python
import dudraw

def main():
    # set up the dudraw canvas

    # initialize the attributes of object you are animating (position, size, etc.)

    # main animation loop (infinite loop, later we will give a way for users to quit)
    while True:
        # clear background

        # redraw the next frame

        # display the frame and pause

        # Prepare for next frame by advancing the attributes of the animated object(s)
        #  (move position, change size, etc.)

        # Check for user input (key presses or mouse presses)


if __name__ == "__main__":
    main()

```

Check for key presses by using `dudraw.next_key()`, which returns a single character if a key was pressed, and returns an empty string (`''`) if no key has been pressed since the most recent query.

Check for mouse clicks using `dudraw.mouse_clicked()`. Sometimes you may need to recognize if the mouse is currently pressed and not yet released (so you can process dragging of the mouse). Then use `dudraw.mouse_is_pressed()`. Occasionally you may also need the supporting functions `dudraw.mouse_dragged()` and `dudraw.mouse_released()`.

Here's a simplest example of an animation:
```python
import dudraw

# Animates a circle moving to the upper right.
# Quits when user types 'q'. When mouse is clicked,
# the circle's position sets to the clicked position.
def main():
    # set up the dudraw canvas
    dudraw.set_canvas_size(400, 400)
    # no call to dudraw.set_x_scale() or dudraw.set_y_scale()
    # means we are accepting the default of x in [0, 1] and y in [0, 1]

    # initialize the position of the circle
    x = 0.1
    y = 0.5

    # 
    key = ''
    # main animation loop (infinite loop, later we will give a way for users to quit)
    while key.lower() != 'q':
        # clear background
        dudraw.clear(dudraw.LIGHT_GRAY)

        # redraw the next frame. The circle has a radius of 10 pixels.
        dudraw.filled_circle(x, y, 0.025)

        # display the frame and pause (20 milliseconds = 50 frames per second)
        dudraw.show(20)

        # Prepare for the  next frame by moving circle, one pixel
        x += .0025
        y += .0025
        # Save keypress to check for 'q' next time through the loop
        key = dudraw.next_key()
        # if the mouse has been clicked, reset the x, y position to
        # the clicked location
        if dudraw.mouse_clicked():
            x = dudraw.mouse_x()
            y = dudraw.mouse_y()        


if __name__ == "__main__":
    main()
```

[comment]: <> (https://github.com/user-attachments/assets/a540b4c6-e952-4814-bfbc-bac4b4b0f837)
Here's a video demonstrating the above code running:

<video src="https://cs.du.edu/~ftl/1352/videos/simplest_animation.mov" width="320" height="320" controls></video>



To animate more complex objects, create a function that displays the object at position given by parameters. (or, once you have learned to use classes, perhaps you will implement a method of a class to draw the object). Here's an example. Notice that very little of the `main()` function changed!

```python
import dudraw
import random

def draw_rocket(x: float, y: float)->None:
    # rectangle, main body of rocket:
    dudraw.set_pen_color(dudraw.WHITE)
    dudraw.filled_rectangle(x, y, 0.03, .125)
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.rectangle(x, y, 0.03, 0.125)
    # cone at top of rocket (drawn as a rectangle)
    dudraw.set_pen_color(dudraw.WHITE)
    dudraw.filled_triangle(x-0.03,y+0.125, x+0.03, y+0.125, x, y+0.2)
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.triangle(x-0.03,y+0.125, x+0.03, y+0.125, x, y+0.2)
    dudraw.set_font_size(8)
    dudraw.text(x, y, "NASA")
    # draw a bunch of circles, to look like smoke:
    print(int(y*80))
    for _ in range(int(y*80)):
        y_offset = random.uniform(max(0,y-0.25), y-0.125)
        x_offset = random.uniform((y_offset-y)*0.2, (y-y_offset)*0.2)
        size = random.uniform(0.0125, 0.025)
        red = random.randint(50, 255)
        green = random.randint(0,red//2)
        dudraw.set_pen_color_rgb(red, green, 0)
        dudraw.filled_circle(x+x_offset, y_offset,size)
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.circle(x+x_offset,y_offset,size )

# animate a rocket taking off:
def main():
    # set up the dudraw canvas
    dudraw.set_canvas_size(400, 400)

    # no call to dudraw.set_x_scale() or dudraw.set_y_scale()
    # means we are accepting the default of x in [0, 1] and y in [0, 1]

    # initialize the position of the rocket
    x = 0.5
    y = 0.125

    # 
    key = ''
    # main animation loop (infinite loop, later we will give a way for users to quit)
    while key.lower() != 'q':
        # clear background
        dudraw.clear(dudraw.LIGHT_GRAY)

        # redraw the next frame. The circle has a radius of 10 pixels.
        draw_rocket(x, y)

        # display the frame and pause (20 milliseconds = 50 frames per second)
        dudraw.show(20)

        # Prepare for the  next frame by moving rocket, upwards one pixel
        y += .0025
        # Save keypress to check for 'q' next time through the loop
        key = dudraw.next_key()
        # if the mouse has been clicked, reset the x, y position to
        # the clicked location
        if dudraw.mouse_clicked():
            x = dudraw.mouse_x()
            y = dudraw.mouse_y()        


if __name__ == "__main__":
    main()
```

Here's a video demonstrating the code above running:

[comment]: <> (ttps://github.com/user-attachments/assets/9ff759bf-cddf-48fc-a6a8-1f6540f618ec)

<video src="https://cs.du.edu/~ftl/1352/videos/rocket_animation.mov" width="320" height="320" controls></video>





