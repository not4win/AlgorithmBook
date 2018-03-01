class disjoint:
    def __init__(self,x):
        self.parent=x
        self.rank=0
        self.me=x
        
class disjointop:
    def __init__(self,n):
        self.mem=[None for i in range(n)]
        for i in range(n):
            self.mem[i]=disjoint(i)
        self.visited=[False for i in range(n)]
            
    def findset(self,x):
        if x.parent==x.me:
            return x

        else:
            return self.findset(x.parent)
            print('x')
            
    def merge(self,x,y):
        rx= self.findset(x)
        ry=self.findset(y)
        if rx.rank>ry.rank:
            ry.parent=rx
        elif ry.rank>rx.rank:
            rx.parent=ry
        else:
            ry.parent=rx
            rx.rank=rx.rank+1
            
    def count(self,key):
        s=self.findset(key)
        count=0
        st=""
        for i in self.mem:
            if self.findset(i)==s:
                count=count+1
                st=st+str(i.me)+" "
        return count,st

a=input()
a=a.split(' ')
y=disjointop(int(a[0]))
for i in range(int(a[1])):
    b=input()
    b=b.split(' ')
    if b[0]=='Q':
        c,d=y.count(y.mem[int(b[1])-1])
        print('the number of elements in this set',c)
        print('the elements are',d)
    if b[0]=='M':
        y.merge(y.mem[int(b[1])-1],y.mem[int(b[2])-1])

