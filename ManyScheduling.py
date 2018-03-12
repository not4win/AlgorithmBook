print("enter the number of intervals:")
n=int(input())
a=[[] for i in range(n)]
for i in range(n):
	b=input()
	b=b.split(' ')
	a[i].append(int(b[0]))
	a[i].append(int(b[1]))
a = sorted(a,key = lambda x:x[1])
print(a)        	
i=0
c=[]
t=0
for i in range(n):
	if t<a[i][0]:
		c.append(a[i])
		t=a[i][1]
	else:
		pass
print(c)



