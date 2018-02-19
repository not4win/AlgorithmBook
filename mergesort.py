n=int(input("enter the elements of the array: "))
a=[]
inversions=0
print("enter elements")
for i in range(n):
    a.append(int(input()))

def merge(a,l,h):
    if(l<h):
        mid=(l+h)//2
        merge(a,l,mid)
        merge(a,mid+1,h)
        mergesort(a,l,mid,h)

def mergesort(a,l,mid,h):
    global inversions
    low=[]
    high=[]
    for i in range(l,mid+1):
        low.append(a[i])
    for i in range(mid+1,h+1):
        high.append(a[i])

    n1=mid-l
    n2=h-mid-1
    i=0
    j=0
    k=l
    while(i<=n1 and j<=n2):
        if(low[i]<=high[j]):
            a[k]=low[i]
            k=k+1
            i=i+1
        else:
            a[k]=high[j]
            k=k+1
            j=j+1
            inversions=inversions+1
    if(i<=n1):
        while(i<=n1):
            a[k]=low[i]
            k=k+1
            i=i+1
            inversions=inversions+1
    if(j<=n2):
        while(j<=n2):
            a[k]=high[j]
            k=k+1
            j=j+1

merge(a,0,len(a)-1)
print(a)
print(inversions)
            
        
