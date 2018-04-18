'''


'''

def insertion_sort(arr):

	for i in range(1,len(arr)):

		cur = arr[i]

		# compare the current elemnet with the jth element in arr[0,i-1]
		# if arr[j] greater than arr[i] then keep looking j-1 th position
		# else arr[j] less than arr[i] then insert the key one ahead of the current position
		j = i-1
		while j>=0 and cur <arr[j]:
			# move one position back so that leave one empty position for insertion
			arr[j+1] =arr[j] 
			j  -=1

		#insert one ahead of position j

		arr[j+1] = cur

# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])
 