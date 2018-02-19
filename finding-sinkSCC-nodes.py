def enter_edges(a,b):
    al[a].append(b)
    ral[b].append(a)

def DFSr(s):
    global time
    visited[s]=True
    time=time+1
    timestamp[s].append(time)
    for i in ral[s]:
        if visited[i]==False:
            DFSr(i)
    time=time+1
    timestamp[s].append(time)

def DFSrmain():
    for i in range(n):
        if(visited[i]==False):
            DFSr(i)
def DFS(s):
    visited2[s]=True
    timestamp[s].append(time)
    for i in ral[s]:
        if visited[i]==True:
            DFSr(i)
def maxtimestamp():
    maX=0
    maxnode=0
    for i in range(n):
        if(timestamp[i][1]>maX):
            maX=timestamp[i][1]
            maxnode=i
    return maxnode


n=int(input("enter the number of nodes"))
al=[[] for i in range(n)]
ral=[[] for i in range(n)]
visited=[False for i in range(n)]
visited2=[False for i in range(n)]
timestamp=[[] for i in range(n)]
time=1
option=1
while(option!=0):
    a=int(input("enter source edge"))
    b=int(input("enter target edge"))
    option=int(input("enter option"))
    enter_edges(a,b)
DFSrmain()
y=maxtimestamp()
print("one of the sink node is ",y)
print("the sink nodes are:")
DFS(y)
for i in range(n):
    if visited2[i]==True:
        print(i)


    
    
    
