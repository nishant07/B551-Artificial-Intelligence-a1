def solution(arr,goal):
        fringe = []
        visited = []
        stepArr = ["L","L","L","L","R","R","R","R","U","U","U","U","D","D","D","D"]
        obj1 = Object(-1, None)
        obj1.setMatrix(arr, "N", 0)
        fringe.append(obj1)
        while fringe:
            if isEqualArr(visited, fringe[0].matrix):
                fringe.pop(0)
            else:
                tempArr = fringe[0].matrix
                depth = fringe[0].gVal
                pathStep = fringe[0].steps
                if isEqual(tempArr, goal):
                    print fringe[0].steps
                    return tempArr
                else:
                    visitedObj = Object()
                    visitedObj.setMatrix(tempArr, "N", 0)
                    visitedObj.gVal = fringe[0].gVal
                    visitedObj.hVal = fringe[0].hVal
                    visitedObj.val = fringe[0].val
                    visited.append(visitedObj)
                    fringe.pop(0)
                for cnt in range (0,16):
                    obj = Object(depth,pathStep)
                    obj.setMatrix(tempArr, stepArr[cnt], cnt%4)
                    obj.sethVal()
                    fringe.append(obj)
                fringe.sort(key = lambda x:x.val, reverse = True)
        return tempArr     

def getArrayVal(num):
        arrVal = ["","00","01","02","03","10","11","12","13","20","21","22","23","30","31","32","33"];
        return arrVal[num]

def calDiff(val, row, col):
        val1 = getArrayValues(val)
        diff1 = row - val1[0:1]
        diff2 = col - val1[1:]
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
        if arr == goalArr:
            return True
        else:
            return False

def isEqualArr(visited, matrix):
        for i in visited:
            equal = isEqual(visited[i], matrix)
            if equal:
                return equal

class Object:
    def __init__(self, depth, path):
            self.gVal = depth + 1
            self.steps = path
            self.hVal = 0
            self.val = self.gVal + self.hVal
            matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    def setHVal(self):
            self.hVal = heuristic(self.matrix)
            self.val = self.hVal + self.gVal

    def setMatrix(self, matrix, step, num):
            tempMatrix = []
#            steps
            for i in range(0,4):
                for j in range(0,4):
                    tempMatrix.append(matrix[i][j])
            self.matrix = move(tempMatrix, step, num)
 #           steps = steps + " " + step + num

def printArr(arr):
        for i in range(0,4):
            print arr[i][0] +" "+ arr[i][1] +" "+ arr[i][2] +" "+ arr[i][3]

arr = [[5,7,8,1],[10,2,4,3],[6,9,11,12],[15,13,14,16]]
goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
tempArr = solution(arr,goal)
printArr(tempArr)
