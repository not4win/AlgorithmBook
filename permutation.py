n=int(input("enter the elements of the array: "))
a=[]
print("enter elements")
for i in range(n):
    a.append(int(input()))
def permute(a,l,r):
    if(l==r):
        print(a)
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            permute(a,l+1,r)
            a[l],a[i]=a[i],a[l]

permute(a,0,len(a)-1)
            
    
