class ds:
	def __init__(self,x):
		self.parent=x
		self.rank=0
		self.me=x
class edges:
	def __init__(self,a,b,weight):
		self.a=a
		self.b=b
		self.weight=weight
class dsx:
	def __init__(self,n):
		self.mem=[None for i in range(n)]
		for i in range(n):
			self.mem[i]=ds(i)
		self.ew=[[None for i in range(n) ] for i in range(n)]
		self.W=[]
		self.T=[]
	def findset(self,x):
		if x.parent==x.me:
			return x

		else:
			return self.findset(x.parent)
			print('x')
	def union(self,x,y):
		rx= self.findset(x)
		ry=self.findset(y)
		if rx.rank>ry.rank:
			ry.parent=rx
		elif ry.rank>rx.rank:
			rx.parent=ry
		else:
			ry.parent=rx
			rx.rank=rx.rank+1

	def edgesx(self,a,b,size):
		self.ew[a][b]=size
		self.W.append(edges(a,b,size))

		return

	def sort_edges(self):
		for i in range(len(self.W)-1,-0,-1):
			for j in range(i):
				if self.W[j].weight>self.W[j+1].weight:
					temp=self.W[j]
					self.W[j]=self.W[j+1]
					self.W[j+1]=temp
	def kruskal(self):
		for ed in self.W:
			if self.findset(self.mem[ed.a])!=self.findset(self.mem[ed.b]):
				print(ed.a,ed.b)
				self.T.append([ed.weight])
				self.union(self.mem[ed.a],self.mem[ed.b])
y=dsx(6)
y.edgesx(0,1,3)
y.edgesx(0,3,2)
y.edgesx(0,4,2)
y.edgesx(1,4,1)
y.edgesx(1,5,3)
y.edgesx(1,2,1)
y.edgesx(3,4,1)
y.edgesx(4,5,2)
y.edgesx(5,2,2)
y.edgesx(4,2,4)
y.sort_edges()
y.kruskal()
print(y.T)




