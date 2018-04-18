'''

MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)


'''
def merge(arr,l,m,r):

	n1 = m-l+1
	n2 = r-m

	L = [0]*n1
	R = [0]*n2

	for i in range(0,n1):
		L[i] = arr[l+i]

	for i in range(0,n2):
		R[i] = arr[m+1+i]
	i = 0
	j =0
	k =l

	while i<n1 and j<n2:
		if L[i]<= R[j]:

			arr[k] = L[i]
			i +=1
		else:
			arr[k] =R[j]
			j+=1
	while i <n1:
		arr[k] = L[i]
		i+=1
		k+=1
	while j <n2:
		arr[k] = R[j]
		j+=1
		k+=1








def merge_sort(arr,l,r):
	if l<r:
		m = int((l+(r-1))/2)

		merge_sort(arr,l,m)

		merge_sort(arr,m+1,r)
		merge(arr,l,m,r)


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print ("Given array is")
for i in range(n):
    print ("%d" %arr[i]),
 
merge_sort(arr,0,n-1)
print ("\n\nSorted array is")
for i in range(n):
    print ("%d" %arr[i]),
 






