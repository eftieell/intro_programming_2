These are just notes from an old canvas page
Notes on Sorting Arrays
Key Points:

Algorithms are, simply put, a sequence of instructions to perform a task. Later courses will go into more detail about algorithm design, analysis, and efficiency.
Sorting algorithms are a great introduction into the world of algorithms and are also extremely useful in practice.
Bubble sort is one algorithm that is not great to use in practice, but is great for learning about sorting.
Algorithms
Although this course will not go into all the minutiae about algorithms (look forward to Intro III and Algorithms), we will get a feel for what an algorithm is, in particular by using sorting as an example.

You've likely heard the term "algorithm", perhaps when talking about a program you wrote or when discussing how YouTube suggests certain videos to you via "the algorithm". While there are technical definitions of the term, we can simply think of an algorithm as a sequence of instructions that perform some task. In this sense, pretty much any program you write could be considered an algorithm. More often, however, we use this term to refer to a sequence of instructions that can be run on various inputs, so it is more appropriate to think of an algorithm as a single method. 

Take, for example, the following method:

public static int findMin(int[] arr) {
	if (arr != null && arr.length > 0) {
		int min = arr[0];
		for (int i = 1; i < arr.length; i++) {
			if (arr[i] < min) {
				min = arr[i];
			}
		}
		return min;
	}
	return -1;
}
You've likely written code very similar to this before. This code adds some extra checks about the array that's passed in, but ultimately the task that this method is solving is finding the minimum in an array of integers. This is an example of an algorithm. It's a fairly simple algorithm, but it is an algorithm nonetheless. 

To motivate some ideas that you'll discuss in later classes, think about how fast this algorithm runs. That is, would it take the same amount of time for this method to finish executing its code if it were given an array of length 10 as opposed to an array of length 10,000? Notice how many times the for loop iterates depending on the length of the array.

Just to demonstrate usage of this method, here's some example code:

public static void main(String[] args) {
	int[] nums = new int[10];
	for (int i = 0; i < nums.length; i++) {
		nums[i] = (int) (Math.random()*50);
		System.out.print(nums[i] + " ");
	}
	System.out.println();
	System.out.println("Min: " + findMin(nums));
}
which outputs:

26 1 38 44 12 19 36 25 14 19
Min: 1
Sorting
Sorting is the quintessential algorithm in computer science. To sort means to order a sequence of element in order. The act of sorting can be useful in many situations, even outside of computer science. Perhaps you sort bills in your wallet to more easily find 1-dollar bills versus 5-dollar bills. When you play any sort of card game, you might sort the cards in your hand to better understand the distribution of your cards and therefore more easily strategize your next move. On many websites, whether it's the course schedule on PioneerWeb or a community forum like Reddit, you likely sort information by certain values to better view the content on the page.

Interestingly, sorting comes up extremely often in computer science. As you take more advanced courses, you'll see why it is so important to understand sorting algorithms because of its ubiquity. Due to its importance, there are many, many sorting algorithms out there, though only a small portion are widely used in practice. The Wikipedia page on sorting algorithm includes a list of the more popular ones: https://en.wikipedia.org/wiki/Sorting_algorithm#Comparison_of_algorithmsLinks to an external site.

Bubble Sort
As an introduction to the world of sorting algorithms, we'll start by discussing bubble sort. Bubble sort is a notoriously inefficient algorithm, one that you would never use in practice. Its beauty lies in its simplicity and intuitiveness.

Here's the idea behind bubble sort: iterate over the array, on each iteration checking adjacent pairs of values. If the values are in the correct order, we don't have to do anything. If they are in the wrong order, swap them. Therefore, on one pass over the array, we will have guaranteed that the maximum element is at the end of the array. Hence, we perform this pass over the array n times for for an array of length n.

public static void bubbleSort(int[] arr) {
	if (arr != null && arr.length > 1) {
		// Outer for-loop ensures we perform n passes.
		// Note that we don't need to use i to index the array.
		for (int i = 0; i < arr.length; i++) {
			// Inner for-loop performs a single pass,
			// swapping pairs of values that are out of order.
			for (int j = 0; j < arr.length-i-1; j++) {
				if (arr[j] > arr[j+1]) {
					// Swap
					int temp = arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = temp;
				}
			}
		}
	}
}
It is safest to ensure the array we're going to sort is not null and that it has at least two elements (otherwise there's no need to sort!). The outer loop's i variable is not used to index into the array. It mostly ensures that the inner loop executes n times. The inner loop performs the actual swaps, so j is the only variable we need to index into the array. In particular, we look at elements at indices j and j+1. If they are not in the correct order, we swap them.

The terminating condition for the inner loop is perhaps the trickiest part. We could just as easily make j go from 0 to arr.length-2 (being careful to not cause j+1 to be out of bounds). But remember the last i elements on any iteration of the outer loop are in their correct spot. After the first pass, the maximum is at the end. After the second pass, the second-largest value is at the second-to-last index, and so on. So, there's no need to check the last i spots.

For completeness, here's some example code using the method:

int[] nums = new int[10];
for (int i = 0; i < nums.length; i++) {
	nums[i] = (int) (Math.random()*50);
}

bubbleSort(nums);
for (int i = 0; i < nums.length; i++) {
	System.out.print(nums[i] + " ");
}
which outputs the randomly generated array in sorted order:

0 6 9 12 14 30 40 42 44 47 
Selection sort
You implemented selection sort in a lab. Like Bubble Sort, Selection Sort is notoriously inefficient, but easier to understand than efficient strategies that you will learn later.

Visualizations
You can find many visualizations of sorting algorithms by searching the internet. Click on this page for a few good visual depictions of sorting algorithms: Cool visual depictions of sorting algorithms 

This one is my favorite: Bubble Sort, as expressed through Hungarian folk dance.

Bubble-sort with Hungarian (&quot;Csángó&quot;) folk danceLinks to an external site.
Bubble-sort with Hungarian (&quot;Csángó&quot;) folk dance