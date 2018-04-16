'''

Binary Search

Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

A simple approach is to do linear search.The time complexity of above algorithm is O(n). Another approach to perform the same task is using Binary Search.

Binary Search: 
Search a sorted array by repeatedly dividing the search interval in half. 
Begin with an interval covering the whole array. 
If the value of the search key is less than the item in the middle of the interval, 
narrow the interval to the lower half. Otherwise narrow it to the upper half. 
Repeatedly check until the value is found or the interval is empty.

'''



# recursive version for binary search 




def rec_bs(arr,l,r,x):
	if r >= l:
		mid = int(l + (r-l)/2)
		if arr[mid] == x :
			return mid 
		elif arr[mid] > x :
			return rec_bs(arr,l,mid-1,x)
		else:
			return rec_bs(arr,mid+1,r,x)
	else:
		return -1 


# def itr_bs(arr,l,r,x):
	while l<= r:
		mid = int(l + (r-l)/2)
		if arr[mid] == x :
			return mid 
		elif arr[mid] < x:
			l = mid +1
		else:
			r = mid -1
	return -1




# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = rec_bs(arr, 0, len(arr)-1, x)
result = itr_bs(arr,0,len(arr)-1,x)
if result != -1:
    print ("Element is present at index %d" % result)
else:
    print ("Element is not present in array")




