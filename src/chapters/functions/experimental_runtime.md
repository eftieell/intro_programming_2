# Timing how long it takes for functions to execute

As we write more complicated code, it becomes increasingly important to make it execute quickly. 
We will start by measuring the runtime experimentally. 
Knowing how long it takes for our code to run will guide us in determining how critical it is to redesign our code to make it run more efficiently.

## Strategy for experimentally timing how long it takes for a function to run
The overall strategy is simple: 
- Record the start time
- Execute the function we are timing
- Record the finish time
- Calculate the elapsed time by subtracting the start time from the finish time

## Finding out what time it is
The function `time.time()` in the python `time` module returns the current time.
```python
import time

def main():
    start_time = time.time()  
    print(start_time)

if __name__ == "__main__":
    main()
```
Sample output:
```
1732765128.7487528
```
This function returns the current time in seconds since a fixed starting moment, which in python is set to midnight on January 1, 1970!
The actual value of the time won't be important to us, since we are not interested in what time it is. Rather, we care
about the amount of time that elapses while a function is executing.

## Timing the running of a function that takes more than a second
Here's an example of code that times how long it takes for the function `do_something()` to execute. The contents and purpose of the function are not what is important in this example - instead we are focusing on how long it takes to execute.
```python
import time

def do_something(n: int) -> None:
    # How long does this take to run?
    count = 0
    for i in range(n):
        count += 1

def main():
    # Record the start time
    start_time = time.time()
    # Execute the function
    do_something(100000000)
    # Record the finish time
    finish_time = time.time()
    elapsed_time = finish_time - start_time
    print(f"runtime for do_something(100000000): {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
```
Sample output:
```
runtime for do_something(100000000): 2.37 seconds
```
Conclusion: it takes 2.37 seconds for do_something() to execute, when the parameter is 100000000.


## Timing the running of a function that takes less than 1 second
If a function takes less than 1 second to execute, then the technique above is often not accurate.
Instead, we must execute the function multiple times (so the total elapsed time is more than 1 second), 
then divide by the number of times the function was called, to get the average execution time. You will learn this technique in a future course.

## Video explanations
<video src="https://cs.du.edu/~ftl/1352/videos/functions/measuring_runtime.mp4" width="480" height="270" controls></video>

