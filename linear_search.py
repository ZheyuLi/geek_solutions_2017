'''
Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].


Examples :

Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
          x = 110;
Output : 6
Element x is present at index 6

Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
           x = 175;
Output : -1
Element x is not present in arr[].
'''



def solve(x,arr):
	for i,val in enumerate(arr):
		if x == val:
			return i 
	return -1 

arr =[ 0, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 110

print(solve(x,arr))