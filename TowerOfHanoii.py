n=int(input("enter the number of pegs: "))

def SolveHanoi(n,s,i,t):
    if(n>=1):
        SolveHanoi(n-1,s,t,i)
        print("move disc ",n," from ",s," to", t)
        SolveHanoi(n-1,i,s,t)
SolveHanoi(n,'S','I','T')
