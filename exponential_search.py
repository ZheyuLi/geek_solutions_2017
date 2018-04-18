'''

Exponential search involves two steps:

Find range where element is present
Do Binary Search in above found range.
How to find the range where element may be present?
The idea is to start with subarray size 1 compare its last element with x, then try size 2, then 4 and so on until last element of a subarray is not greater.
Once we find an index i (after repeated doubling of i), we know that the element must be present between i/2 and i (Why i/2? because we could not find a greater value in previous iteration)

Below is implementation of above steps.

'''

def binarySearch( arr, l, r, x):
    if r >= l:
        mid =int(l + ( r-l ) / 2)
         
        # If the element is present at the middle itself
        if arr[mid] == x:
            return mid
         
        # If the element is smaller than mid, then it
        # can only be present in the left subarray
        if arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
         
        # Else he element can only be present in the right
        return binarySearch(arr, mid+1, r, x)
         
    # We reach here if the element is not present
    return -1


def exp_search(arr,n,x):
	# if x is present at first location itself
	if arr[0] == x:
		return 0
	# find the range for binary search by repeatly doubling 

	i = 1

	while i < n and arr[i] <= x:
		i = i*2
	return binarySearch(arr,i/2,min(i,n),x)


arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
result = exp_search(arr, n, x)
if result == -1:
    print ("Element not found in thye array")
else:
    print ("Element is present at index %d" %(result))
