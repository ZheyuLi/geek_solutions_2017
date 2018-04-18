import sys 

loop = 2
arr = []
for i in range(loop):
	line = input()
	arr.append(line)

width = int(arr[0])
if width <2:
	exit()
text = arr[1]

text = text.split()
count =0 
prev = 0 
i = 0
print(text)
while i< len(text)and i +1< len(text):
# for i,token in enumerate(text):
	token= text[i]
	next = text[i+1]
	print(token)

	# print(len(text[i+1])+1+len(token))
	if len(token)<=width and len(next)+1+len(token)>width:
		count +=1 
		i+=1

	elif len(token) +1 <= width and len(next)+1+len(token)<=width :
		count +=1 
		i+=2
	elif len(token) >width and len(text[i+1]) +1 +(len(token)-width)<=width:
		
		count +=1
		i +=2
	elif len(token) > width :
		count +=2
		i+=1


print(i)
print("count",count)





string = "there is 4 errors in this sentence whose longest wrod have length of 9"