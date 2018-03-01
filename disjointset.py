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
        for i in self.mem:
            if self.findset(i)==s:
                count=count+1
        return count
y=disjointop(7)
y.merge(y.mem[0],y.mem[1])
y.merge(y.mem[1],y.mem[2])
y.merge(y.mem[2],y.mem[3])
y.merge(y.mem[5],y.mem[4])

print(y.count(y.mem[6]))

