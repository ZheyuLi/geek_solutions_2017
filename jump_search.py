


'''

Jump Search
Like Binary Search, Jump Search is a searching algorithm for sorted arrays. The basic idea is to check fewer elements (than linear search) by jumping ahead by fixed steps or skipping some elements in place of searching all elements.

For example, suppose we have an array arr[] of size n and block (to be jumped) size m. Then we search at the indexes arr[0], arr[m], arr[2m]…..arr[km] and so on. Once we find the interval (arr[km] < x < arr[(k+1)m]), we perform a linear search operation from the index km to find the element x.

Let’s consider the following array: (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610). Length of the array is 16. Jump search will find the value of 55 with the following steps assuming that the block size to be jumped is 4.
STEP 1: Jump from index 0 to index 4;
STEP 2: Jump from index 4 to index 8;
STEP 3: Jump from index 8 to index 16;
STEP 4: Since the element at index 16 is greater than 55 we will jump back a step to come to index 9.
STEP 5: Perform linear search from index 9 to get the element 55.

What is the optimal block size to be skipped?
In the worst case, we have to do n/m jumps and if the last checked value is greater than the element to be searched for, we perform m-1 comparisons more for linear search. Therefore the total number of comparisons in the worst case will be ((n/m) + m-1). The value of the function ((n/m) + m-1) will be minimum when m = √n. Therefore, the best step size is m = √n.

'''
import math

def jump_search(arr,x,n):
	# first decide the jumping steps which is equal to the square root of size of the array

	step = round(math.sqrt(n))
	print(step)

	# first we keep jumping until we find the blcok of the target 
	# each time we need compare the number after jumping with the target 
	# until we find the one larger or equal than x
	prev =0
	while(arr[int(min(step,n)-1)] < x ):
		prev = step

		step += step
		if prev >= n :
			return -1

	# after we finding the block we do linear search within the block 

	while(arr[int(prev)] <x):
		prev +=1 
		# if cursor reaches end of the array, not found 
		if prev == min(step,n):
			return -1


	if arr[int(prev)] ==x:
		return prev
	return -1

# Driver code to test function
arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
       34, 55, 89, 144, 233, 377, 610 ]
x = 55
n = len(arr)
 
# Find the index of 'x' using Jump Search
index = jump_search(arr, x, n)
 
# Print the index where 'x' is located
print("Number" , x, "is at index" ,"%.0f"%index)
 
# This code is contributed by "Sharad_Bhardwaj".