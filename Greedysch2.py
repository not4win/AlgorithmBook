print("enter the number of intervals:")
n=int(input())
a=[[] for i in range(n)]
for i in range(n):
	b=input()
	b=b.split(' ')
	a[i].append(int(b[0]))
	a[i].append(int(b[1]))
a = sorted(a,key = lambda x:x[0])
print(a)
interval=[[]]
for edge in a:
    if len(interval[0])==0:
        interval[0].append(edge)
    else:
        l=False
        for j in interval:
            
            for k in j:
                if(k[1]<edge[0]):
                    j.append(edge)
                    l=True
        if(l!=True):
            interval.append([[edge]])
print(interval)
