# Unbeatable
from math import inf
from os import system
def printBoard(state):
    for i in range(len(state)):
        if state[i]!='X' and state[i]!='O':
            print("_",end=" ")
        else:
            print(state[i],end=" ")
        if (i+1)%m==0:
            print()

def createBoard(m):
    state=[]
    for i in range(m*m):
        state.append(i)
    return state

def result(state,pos,turn):
    state[pos]=turn
    return state

def getActions(state):
    a=[]
    for i in range(len(state)):
        if state[i]!='X' and state[i]!='O':
            a.append(i)
    return a

def isBoardFull(state):
    for i in state:
        if i!='X' and i!='O':
            return False
    return True
def getHorizontalIndexes():
    indexes=[]
    a=[]
    for i in range(m*m):
        a.append(i)
        if (i+1)%m==0:
            indexes.append(a)
            a=[]
    return indexes

    
def getVerticalIndexes():
    indexes=[]
    for j in range(m):
        a=[]
        for i in range(j,m*m,m):
            a.append(i)
        indexes.append(a)
    return indexes

def getDiagonalIndexes():
    indexes=[]
    a=[]
    for i in range(0,m*m,m+1):
        a.append(i)
    indexes.append(a)
    a=[]
    for i in range(m-1,(m*m-m)+1,m-1):
        a.append(i)
    indexes.append(a)
    return indexes
def isTerminal(state):
    for l in ver_indexes:
        a=state[l[0]]
        equal=True
        for i in range(1,len(l)):
            if state[l[i]]!=a:
                equal=False
                break
        if equal:
            if a=='X':
                winner='X'
            else:
                winner='O'
            return True
    for l in hor_indexes:
        a=state[l[0]]
        equal=True
        for i in range(1,len(l)):
            if state[l[i]]!=a:
                equal=False
                break
        if equal:
            if a=='X':
                winner='X'
            else:
                winner='O'
            return True
    for l in dia_indexes:
        a=state[l[0]]
        equal=True
        for i in range(1,len(l)):
            if state[l[i]]!=a:
                equal=False
                break
        if equal:
            if a=='X':
                winner='X'
            else:
                winner='O'
            return True
    if isBoardFull(state):
        return True
    return False
def Utility(state):
    for l in ver_indexes:
        a=state[l[0]]
        equal=True
        for i in range(1,len(l)):
            if state[l[i]]!=a:
                equal=False
                break
        if equal:
            if a=='X':
                return 1
            return -1
    for l in hor_indexes:
        a=state[l[0]]
        equal=True
        for i in range(1,len(l)):
            if state[l[i]]!=a:
                equal=False
                break
        if equal:
            if a=='X':
                return 1
            return -1
    for l in dia_indexes:
        a=state[l[0]]
        equal=True
        for i in range(1,len(l)):
            if state[l[i]]!=a:
                equal=False
                break
        if equal:
            if a=='X':
                return 1
            return -1
    return 0

def minimax(state,depth,max_turn,alpha,beta):
    global count
    max_score=-inf
    min_score=inf
    count+=1
    if isTerminal(state):
        u=Utility(state)
        if u==1:
            return 10-depth
        else:
            return u

    else:
        if max_turn:
            for i in getActions(state):
                score=minimax(result(state,i,'X'),depth+1,False,alpha,beta)
                if score>max_score:
                    max_score=score
                if score>alpha:
                    alpha=score
                state[i]=i
                if alpha>=beta:
                    break
            return max_score

        else:
            for i in getActions(state):
                score=minimax(result(state,i,'O'),depth+1,True,alpha,beta)
                if score<min_score:
                    min_score=score
                if  score<beta:
                    beta=score
                state[i]=i
                if alpha>=beta:
                    break
            return min_score



def getMaxPos(board):
    global count
    act=getActions(board)
    max_pos=act[0]
    max_score=-inf
    for i in act:
        score=minimax(result(board,i,'X'),0,False,-inf,inf)
        count+=1
        if score>max_score:
            max_score=score
            max_pos=i
        board[i]=i
    # print("Utility :",max_score)
    return max_pos

count=0
m=3
board=createBoard(m)
ai_turn=True
ver_indexes=getVerticalIndexes()
hor_indexes=getHorizontalIndexes()
dia_indexes=getDiagonalIndexes()
while not isTerminal(board):
    if ai_turn:
        a=getMaxPos(board)
        print(count)
        result(board,a,'X')
        printBoard(board)
        if isTerminal(board):
            break
        ai_turn=False
        count=0
    else:
        a=int(input("Enter the Pos :"))
        result(board,a,'O')
        printBoard(board)
        if isTerminal(board):
            break
        ai_turn=True