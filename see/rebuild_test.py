list=[]
for y in range(2):
	for x in range(5):
		list.append((y,x,'test'))

check = len(list)

for i in list:
	j,k,l=list[i]
	print(j)
	print(k)

