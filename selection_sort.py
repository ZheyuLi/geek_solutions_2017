A = [64, 25, 12, 22, 11]

for i in range(len(A)):

	min_idx = i

	# for remaining list, finding the minimal and replace the current minimal

	for j in range(i+1,len(A)):
		#compare each element with current min
		if A[j] < A[min_idx]:
			min_idx = j

		A[i], A[min_idx] = A[min_idx], A[i]




print("sorted array")

for i in range(len(A)):
	print("%d"%A[i])
