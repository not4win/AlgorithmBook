n=int(input("enter the elements of the array: "))
a=[]
s=""
print("enter elements")
for i in range(n):
    a.append(int(input()))

def combination(a,l,r,s):
    if(l>r):
        print(s)
        return
    combination(a,l+1,r,s+str(a[l]))
    combination(a,l+1,r,s)

combination(a,0,len(a)-1,s)
