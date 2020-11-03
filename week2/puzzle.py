"""Program to show steps to solve a * puzzle problem
This program provides optimal steps to arrive at goal state given an start state
Here strt state and goal state are specified in the code itself"""
#state=[(1,0,0),(2,0,1),(4,0,2),(7,1,0),(8,1,1),(3,1,2),(5,2,0),(6,2,1),('',2,2)]
#state=[1,2,3,4,5,6,7,0,8]
#goalstate=[1,2,3,4,5,6,7,8,0]
#goalstate=[(1,0,0),(2,0,1),(3,0,2),(4,1,0),(5,1,1),(6,1,2),(7,2,0),(8,2,1),('',2,2)]

def manhattan(state):
    
    a=[0,0,0,1,1,1,2,2,2]
    b=[0,1,2,0,1,2,0,1,2]
    m=list(zip(state,a,b))
    n=list(zip(goalstate,a,b))
    sum=0
    for k,l,q in m:
        for x,y,z in n:
            if (k==x):
                sum+=abs(y-l)+abs(z-q)
    return sum
def nextstate(state):
    a=[0,0,0,1,1,1,2,2,2]
    b=[0,1,2,0,1,2,0,1,2]
    m=list(zip(state,a,b))
  
    

    for val, i, j  in m:
        if (int(val)==0):
            list_nextstate=[]
            if ((i,j)==(0,0)):
                for _ in [1,3]:
                    copy=state[:]
                    copy[_],copy[0]=copy[0],copy[_]
                    list_nextstate.append(copy)
            
            elif ((i,j)==(0,1)):
                for _ in [0,2,4]:
                    copy=state[:]
                    copy[_],copy[1]=copy[1],copy[_]
                    list_nextstate.append(copy)

            elif ((i,j)==(0,2)):
                for _ in [1,5]:
                    copy=state[:]
                    copy[_],copy[2]=copy[2],copy[_]
                    list_nextstate.append(copy)
            elif ((i,j)==(1,0)):
                for _ in [0,4,7]:
                    copy=state[:]
                    copy[_],copy[3]=copy[3],copy[_]
                    list_nextstate.append(copy)
            elif ((i,j)==(1,1)):
                for _ in [1,3,5,7]:
                    copy=state[:]
                    copy[_],copy[4]=copy[4],copy[_]
                    list_nextstate.append(copy)
            elif ((i,j)==(1,2)):
                for _ in [2,4,8]:
                    copy=state[:]
                    copy[_],copy[5]=copy[5],copy[_]
                    list_nextstate.append(copy)
            elif ((i,j)==(2,0)):
                for _ in [3,7]:
                    copy=state[:]
                    copy[_],copy[6]=copy[6],copy[_]
                    list_nextstate.append(copy)
            elif ((i,j)==(2,1)):
                for _ in [4,6,8]:
                    copy=state[:]
                    copy[_],copy[7]=copy[7],copy[_]
                    list_nextstate.append(copy)
            elif ((i,j)==(2,2)):
                for _ in [5,7]:
                    copy=state[:]
                    copy[_],copy[8]=copy[8],copy[_]
                    list_nextstate.append(copy)    
          
            return sorted(list_nextstate,key=manhattan)[0]
#driver code
goalstate=[1,2,3,8,0,4,7,6,5]
state=[2,0,3,1,8,4,7,6,5]
while(goalstate!=state):
    x=nextstate(state)
    print(x)
    state=x
"""output:
python puzzle8.py
[0, 2, 3, 1, 8, 4, 7, 6, 5]
[1, 2, 3, 0, 8, 4, 7, 6, 5]
[1, 2, 3, 8, 0, 4, 7, 6, 5]
"""