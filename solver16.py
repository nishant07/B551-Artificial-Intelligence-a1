# Here the search problem includes seraching of goal state which is canonical configuration of the given board.
# To reach till the goal state we decide to consider a state as an object with a matrix containing the current state
# after applying some left/right/up/down on some rows/columns, its heuristic value, cost of reaching till the state and
# path followed to reached till that particular state.

#We have consider weight of any edge as 1, and choose next state having least value of heuristic value plus the value of
#reaching till the node.
#Heuristic function = sum of steps required to move each element from its current position to the goal state.
#Here one step = L/R/U/D of any one row or column

#Following programs considers given state as start state. If start state is not goal then expand that node. Each node
# will have 16 child states which are achived after performing L/R/U/D on each Rows/Columns. Now add all these children
# states in a fringe and sort the fringe. The parent node will be put in visited list. Popup the first node from fringe
# and perform the above procedure.

#The basic challenge faced is regarding running time of the program and number of nodes to be visited to reach till the
#final goal.
import sys

arr = []
#Open file as mentioned in the command line arguament
f = open(sys.argv[1], 'r')
#Fill Start state values from the given input
for i in f:
    arr.append(map(int,(i.split())))
goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def solution(arr,goal):
    fringe = []
    visited = []
    stepArr = ["L","L","L","L","R","R","R","R","U","U","U","U","D","D","D","D"]
    obj1 = Object(-1, '')
    obj1.setMatrix(arr, "N", 0)
    #add start state in fringe
    fringe.append(obj1)
    pcount = 0
    #continue till fringe is not empty
    while len(fringe) != 0:
        pcount = pcount + 1
        #if state already visited neglect
        if isEqualArr(visited, fringe[0].matrix):
            fringe.pop(0)
        else:
            tempArr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            #get first state from fringe
            for i in range(0,4):
                for j in range(0,4):
                    tempArr[i][j] = fringe[0].matrix[i][j]
            depth = fringe[0].gVal
            pathStep = fringe[0].steps
            printArr(tempArr)
            #if current state is goal state return path
            if isEqual(tempArr, goal):
                print "Output: "
                printArr(tempArr)
                return fringe[0].steps[4:]
            else:
                #add current state in visited list
                visitedObj = Object(-1,'')
                visitedObj.setMatrix(tempArr, "N", 0)
                visitedObj.gVal = fringe[0].gVal
                visitedObj.hVal = fringe[0].hVal
                visitedObj.val = fringe[0].val
                visited.append(visitedObj)
                fringe.pop(0)
            #generate child nodes of current state and add to fringe
            for cnt in range (0,16):
                obj = Object(depth,pathStep)
                obj.setMatrix(tempArr,stepArr[cnt], cnt%4)
                obj.setHVal()
                fringe.append(obj)
            #sort both fringe and visited list according to its cost(g(n)+h(n))
            fringe.sort(key = lambda x:x.val)
            visited.sort(key = lambda x:x.val)
    return tempArr

#return required row + column position of input number
def getArrayValues(num):
    arrVal = ["","00","01","02","03","10","11","12","13","20","21","22","23","30","31","32","33"];
    return arrVal[num]

#calculate the required steps to reach till goal position for the input number
def calDiff(val, row, col):
    val1 = getArrayValues(val)
    diff1 = row - int(val1[0:1])
    diff2 = col - int(val1[1:])
    if diff1<0:
        diff1=diff1*-1
    if diff2<0:
        diff2=diff2*-1;
    if diff1==3:
        diff1=1
    if diff2==3:
        diff2=1
    return diff1+diff2

#returns the sum of all steps required to place all numbers at their goal place
def heuristic(arr):
    sum = 0;
    for i in range(0,4):
        for j in range(0,4):
            sum = sum + calDiff(arr[i][j], i, j)
    return sum;

#change position of numbers according to required action
def move(arr, step, i):
    tempArr = arr
    if step == "L":
        temp = tempArr[i][0]
        tempArr[i][0] = tempArr[i][1]
        tempArr[i][1] = tempArr[i][2]
        tempArr[i][2] = tempArr[i][3]
        tempArr[i][3] = temp
    elif step == "R":
        temp = tempArr[i][3]
        tempArr[i][3] = tempArr[i][2]
        tempArr[i][2] = tempArr[i][1]
        tempArr[i][1] = tempArr[i][0]
        tempArr[i][0] = temp
    elif step == "U":
        temp = tempArr[0][i]
        tempArr[0][i] = tempArr[1][i]
        tempArr[1][i] = tempArr[2][i]
        tempArr[2][i] = tempArr[3][i]
        tempArr[3][i] = temp
    elif step == "D":
        temp = tempArr[3][i]
        tempArr[3][i] = tempArr[2][i]
        tempArr[2][i] = tempArr[1][i]
        tempArr[1][i] = tempArr[0][i]
        tempArr[0][i] = temp
    return tempArr

#check if two arrays are equal
def isEqual(arr, goalArr):
    return arr == goalArr

#check if a state is already visited
def isEqualArr(visited, matrix):
    for i in visited:
        equal = isEqual(i.matrix, matrix)
        if equal:
            return equal

#state is represented as an object of following class
class Object:
    def __init__(self, depth, path):
        self.gVal = depth + 1
        self.steps = path
        self.hVal = 0
        self.val = self.gVal + self.hVal
        self.matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    def setHVal(self):
        self.hVal = heuristic(self.matrix)
        self.val = self.hVal + self.gVal

    #set the values of state as per input step
    def setMatrix(self, matrix, step, num):
        tempMatrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for i in range(0,4):
            for j in range(0,4):
                tempMatrix[i][j] = matrix[i][j]
        tempMatrix = move(tempMatrix, step, num)
        for i in range(0,4):
            for j in range(0,4):
                self.matrix[i][j] = tempMatrix[i][j]
        self.steps = self.steps + " " + step + str(num+1)

#print given array
def printArr(arr):
    print arr

#print the required steps to achieve goal state from given state
output = solution(arr,goal)
print output
f.close()



