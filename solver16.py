# Here the search problem includes seraching of goal state which is canonical configuration of the given board.
# To reach till the goal
#
#
#
#
#
import sys

arr = []
f = open(sys.argv[1], 'r')
for i in f:
    arr.append(map(int,(i.split())))
goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def solution(arr,goal):
    fringe = []
    visited = []
    stepArr = ["L","L","L","L","R","R","R","R","U","U","U","U","D","D","D","D"]
    obj1 = Object(-1, '')
    obj1.setMatrix(arr, "N", 0)
    fringe.append(obj1)
    pcount = 0
    while len(fringe) != 0:
        pcount = pcount + 1
        if isEqualArr(visited, fringe[0].matrix):
            fringe.pop(0)
        else:
            tempArr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            for i in range(0,4):
                for j in range(0,4):
                    tempArr[i][j] = fringe[0].matrix[i][j]
            depth = fringe[0].gVal
            pathStep = fringe[0].steps
            printArr(tempArr)

            if isEqual(tempArr, goal):
                print "Output: "
                printArr(tempArr)
                return fringe[0].steps[4:]
            else:
                visitedObj = Object(-1,'')
                visitedObj.setMatrix(tempArr, "N", 0)
                visitedObj.gVal = fringe[0].gVal
                visitedObj.hVal = fringe[0].hVal
                visitedObj.val = fringe[0].val
                visited.append(visitedObj)
                fringe.pop(0)
            for cnt in range (0,16):
                obj = Object(depth,pathStep)
                obj.setMatrix(tempArr,stepArr[cnt], cnt%4)
                obj.setHVal()
                fringe.append(obj)
            fringe.sort(key = lambda x:x.val)
            visited.sort(key = lambda x:x.val)
    return tempArr

def getArrayValues(num):
    arrVal = ["","00","01","02","03","10","11","12","13","20","21","22","23","30","31","32","33"];
    return arrVal[num]

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

def heuristic(arr):
    sum = 0;
    for i in range(0,4):
        for j in range(0,4):
            sum = sum + calDiff(arr[i][j], i, j)
    return sum;

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

def isEqual(arr, goalArr):
    return arr == goalArr

def isEqualArr(visited, matrix):
    for i in visited:
        equal = isEqual(i.matrix, matrix)
        if equal:
            return equal

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

def printArr(arr):
    print arr

output = solution(arr,goal)
print output
f.close()



