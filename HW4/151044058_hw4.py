#region Global Values
ERROR = -404    # To return error
MINUS_INFINITE = -99999999  # To find maximum sum
NoBuy = 999999  # To give value of index with no cost
NoSale = -999999 # To give value of index with no price
RED = -1 # One set of Graph
BLACK = 2 # Other set of Graph
#endregion

#region Print Spectator
def printSeperator():
    print("============================================================================")
#endregion

#region Part1_b Methods
def printArray2D(array):
    for i in range(len(array)):
        print(array[i])
def findMaxErrorIndex(errorCountArray):
    maxNum = -9999
    index = 0
    for i in range(len(errorCountArray)):
        if(maxNum < errorCountArray[i]):
            maxNum = errorCountArray[i]
            index = i

    return index

def convertsIntoTheSpecialArray(array):

    isSpecialControl = True
    allErrors= isSpecialOrNot(array)
    if(len(allErrors) == 0):
        print("The array is already a Special Array")
        return ERROR, ERROR, ERROR
    else:
        errorCountArray = []
        for i in range(len(allErrors)):
            index = allErrors[i]
            errorCountArray.append(index[0])

        errorIndex = findMaxErrorIndex(errorCountArray)
        errorOf_allErrors= allErrors[errorIndex]
        while(isSpecialControl):

            i = 0
            while(i < len(errorOf_allErrors) - 1):
                tempArray = array
                x = errorOf_allErrors[i + 1][0]
                y = errorOf_allErrors[i + 1][1]
                i = i + 1

                tempArray[x][y] = tempArray[x][y] + errorOf_allErrors[0]
                returnValue = isSpecialOrNot(tempArray)
                if(len(returnValue) == 0):
                    return tempArray, x, y

                tempArray[x][y] = tempArray[x][y] - 2 * errorOf_allErrors[0]
                returnValue = isSpecialOrNot(tempArray)
                if (len(returnValue) == 0):
                    return tempArray, x, y

                tempArray[x][y] = tempArray[x][y] + errorOf_allErrors[0]    # Make it old version


def isSpecialOrNot(array):
    row = len(array[0])
    column = len(array)

    errorArray = []

    for i in range(column - 1):
        for j in range(i + 1, column):
            for k in range(row - 1):
                for l in range(k + 1, row):
                    upper_left = array[i][k]
                    upper_right = array[i][l]
                    lower_left = array[j][k]
                    lower_right = array[j][l]
                    if(upper_left + lower_right > lower_left + upper_right):
                        first = upper_left + lower_right
                        second = lower_left + upper_right
                        errorCoordinateAndDifference = [first - second, [i, k], [i, l], [j, k], [j, l]]
                        errorArray.append(errorCoordinateAndDifference)

    return errorArray
#endregion

#region Part1_c Methods
def printValueAndIndex(array):
    for i in range(len(array)):
        value , index = array[i]
        print("Value : " + str(value) + " Index : [" + str(i) + "," + str(index) + "]")

def findLeftMostMinumumElementAndIndex(array):
    row = len(array)
    returnValueArray = []
    for i in range(row):
        i_thRow = findLeftMostMinumumElementAndIndexRecursive(array[i], 0, len(array[i]) - 1)
        returnValueArray.append(i_thRow)

    printValueAndIndex(returnValueArray)

def findLeftMostMinumumElementAndIndexRecursive(array, start, end):
    if (start == end):
        return array[start], start

    middleIndex = int((start + end) / 2)

    minimumNumber1, leftMostIndex1 = findLeftMostMinumumElementAndIndexRecursive(array, start, middleIndex)
    minimumNumber2, leftMostIndex2 = findLeftMostMinumumElementAndIndexRecursive(array, middleIndex + 1, end)

    if (minimumNumber1 <= minimumNumber2):
        return minimumNumber1, leftMostIndex1
    elif (minimumNumber1 > minimumNumber2):
        return minimumNumber2, leftMostIndex2


#endregion

#region Part2 Methods
def find_kthElemet(array1, array2, k):
    return find_kthElementRecursive(array1, array2, len(array1), len(array2), k)

def find_kthElementRecursive(array1, array2, len_array1, len_array2, k):
    if((len_array1 + len_array2) < k or k < 1):
        return ERROR

    if(len_array1 == 0):
        return array2[k - 1]

    if (len_array2 == 0):
        return array1[k - 1]

    if(k == 1):
        minElement = min(array1[0], array2[0])
        return minElement

    new_k = int(k / 2)
    tempList = []
    index1 = min(len_array1, new_k)
    index2 = min(len_array2, new_k)

    if(array1[index1 - 1] > array2[index2 - 1]):
        new_k = k - index2
        temp_len_array2 = len_array2 - index2
        tempList = array2[index2:len_array2]
        return find_kthElementRecursive(array1, tempList, len_array1, temp_len_array2, new_k)

    tempList.clear()
    new_k = k - index1
    temp_len_array1 = len_array1 - index1
    tempList = array1[index1:len_array1]

    return find_kthElementRecursive(tempList, array2, temp_len_array1, len_array2, new_k)


#endregion

#region Part3 Methods
def findContiguousSubsetWithLargestSum(array):
    maxSum, startIndex, endIndex = findContiguousSubsetWithLargestSumRecursive(array, 0, len(array) - 1)
    returningArray = array[startIndex:endIndex + 1]
    return returningArray, maxSum

def findContiguousSubsetWithLargestSumRecursive(array, start, end):

    if(start == end):
        return array[start], start, end

    middleIndex = int((start + end) / 2)

    maxSumLeftSubArray, leftStart, leftEnd = findContiguousSubsetWithLargestSumRecursive(array, start, middleIndex)
    maxSumRightSubArray , rightStart, rightEnd = findContiguousSubsetWithLargestSumRecursive(array, middleIndex + 1, end)
    maxSumCroos, crossStart, crossEnd = findMaxCrossingSubArraySum(array, start, end, middleIndex)

    if(max(maxSumLeftSubArray, maxSumRightSubArray, maxSumCroos) == maxSumLeftSubArray):
        return maxSumLeftSubArray, leftStart, leftEnd
    elif(max(maxSumLeftSubArray, maxSumRightSubArray, maxSumCroos) == maxSumRightSubArray):
        return maxSumRightSubArray, rightStart, rightEnd
    else:
        return maxSumCroos, crossStart, crossEnd


def findMaxCrossingSubArraySum(array, start, end, middle):

    sum = 0
    startIndex = 0
    endIndex = 0
    leftSum = MINUS_INFINITE
    rightSum = MINUS_INFINITE

    for i in range(middle, start - 1, -1):
        sum = sum + array[i]
        if(sum > leftSum):
            leftSum = sum
            startIndex = i

    sum = 0
    for i in range(middle + 1, end + 1):
        sum = sum + array[i]
        if(sum > rightSum):
            rightSum = sum
            endIndex = i

    return (leftSum + rightSum), startIndex, endIndex

#endregion

#region Part4 Class Methods
class Graph():
    def __init__(self,V):
        self.V = V
        self.graph = [[0 for i in range(V)] for j in range(V)]  #initialization of graph
        self.colorArray = [RED for i in range(V)]    #initialize of collorArray

    def size(self):
        return self.V
    def printGraph(self):
        for i in range(self.V):
            print(str(i) + " -> ", end="")
            for j in range(len(self.graph[i])):
                if(self.graph[i][j] == 1):
                    print(str(j) + " ", end="")
            print()

def printGraphWithMatrixRepresentation(G):
    for i in range(G.size()):
        print(G.graph[i])

def isBipartiteGraph(G):
    for i in range(G.size()):
        if (G.colorArray[i] == -1):
            returnValue = isBipartiteGraphBFS(G, i)
            if(returnValue == False):
                return False
    return True

def isBipartiteGraphBFS(G, index):

    visited = []
    visited.append(index)

    while(len(visited) != 0):
        U = visited.pop()

        if(G.graph[U][U] == 1):
            return False

        for V in range(G.size()):
            if(G.graph[U][V] == 1 and G.colorArray[V] == RED):
                if(G.colorArray[U] == RED):
                    G.colorArray[V] = BLACK
                else:
                    G.colorArray[V] = RED

                visited.append(V)

            elif(G.graph[U][V] == 1 and G.colorArray[U] == G.colorArray[V]):
                return False

    return True

#endregion

#region Part5 Methods
def printCostOrPrice(array):
    if(len(array) == 0):
        print("Error, Invalid Array!")
        return
    print("[",end="")
    for i in range(len(array)):

        if(array[i] == NoBuy):
            print("No Buy", end="")
        elif(array[i] == NoSale):
            print("No Sale, ", end="")
        else:
            if(i == len(array) - 1):
                print(str(array[i]) + "" , end="")
            else:
                print(str(array[i]) + ", " , end="")
    print("]")

def findBestDayToBuyGood(Cost, Price):

    if(len(Cost) != len(Price)):
        print("You are making a mistake! (Size of arrays must be the same)")
        return ERROR, ERROR
    else:
        return findBestDayToBuyGoodRecursive(Cost, Price, 0, len(Cost) - 2)

def findBestDayToBuyGoodRecursive(Cost, Price, start, end):
    if(start == end):
        return start + 1, Price[start + 1] - Cost[start]

    middleIndex = int((start + end) / 2)

    maxIndex1, maxGain1 = findBestDayToBuyGoodRecursive(Cost, Price, start, middleIndex)

    maxIndex2, maxGain2 = findBestDayToBuyGoodRecursive(Cost, Price, middleIndex + 1, end)

    if(maxGain1 >= maxGain2 and maxGain1 > 0):
        return maxIndex1, maxGain1
    elif(maxGain1 < maxGain2 and maxGain2 > 0):
        return maxIndex2, maxGain2
    else:
        return ERROR, ERROR

#endregion

#region Test Part1_b
# To test it create a 2D array and call convertsIntoTheSpecialArray method with it.
# This method returns 3 thing
# 1. Special Array (Converting from 2D array)
# 2. row (the row index of changing item)
# 3. column (the column index of changing item)
# if it returns ERROR, the 2D array is already a Special Array
def testPart1_b():
    printSeperator()
    print("Algorithm HW4 Part1_b")
    print("Your 2D Array is")
    NotSpecialArray = [
        [10, 17, 13, 28, 23],
        [17, 22, 16, 29, 23],
        [24, 28, 22, 34, 24],
        [11, 13, 66, 17, 7],
        [45, 44, 32, 37, 23],
        [36, 33, 19, 21, 6],
        [75, 66, 51, 53, 34]
    ]
    printArray2D(NotSpecialArray)
    SpecialArray, row, column = convertsIntoTheSpecialArray(NotSpecialArray)

    if (SpecialArray != ERROR):
        print("After chancing one single element")
        print("Changing Row : " + str(row) + " Changing Column : " + str(column))
        printArray2D(SpecialArray)
    printSeperator()


#endregion

#region Test Part1_c
# To test it create a 2D array and call findLeftMostMinumumElementAndIndex method with it.
# findLeftMostMinumumElementAndIndex method prints minimum item and its indexes
def testPart1_c():
    printSeperator()
    print("Algorithm HW4 Part1_c")
    print("Your 2D Array is")
    SpecialArray = [
        [10, 17, 13, 28, 23],
        [17, 22, 16, 29, 23],
        [24, 28, 22, 34, 24],
        [11, 13, 6, 17, 7],
        [45, 44, 32, 37, 23],
        [36, 33, 19, 21, 6],
        [75, 66, 51, 53, 34]
    ]
    printArray2D(SpecialArray)
    print("After Finding Leftmost Minimum Element and Its Index in Each Row")
    findLeftMostMinumumElementAndIndex(SpecialArray)
    printSeperator()

#endregion

#region Test Part2
# To test it create 2 sorted array.
# Call find_kthElemet with 2 array and k value
# It returns the kth element.
# If it returns ERROR you are giving wrong k value
def testPart2():
    printSeperator()
    print("Algorithm HW4 Part2")
    sortedArray1 = [5, 10, 15, 20, 25]
    sortedArray2 = [3, 6, 9, 12]
    k = 4
    print("Your Sorted Array 1 :", sortedArray1)
    print("Your Sorted Array 2 :", sortedArray2)
    kthElement = find_kthElemet(sortedArray1, sortedArray2, k)
    if(kthElement == ERROR):
        print("Invalid k to Find Element! k :", k)
    else:
        print(str(k) + "th Element : " + str(kthElement))
    printSeperator()

#endregion

#region Test Part3
# To test it create a array and call findContiguousSubsetWithLargestSum method with it.
# This method returns 2 thing
# 1. maxSumSubArray (contiguous array of max sum given array)
# 2. maxSum (sum value)
def testPart3():
    printSeperator()
    print("Algorithm HW4 Part3")
    array = [5, -6, 6, 7, -6, 7, -4, 3]
    maxSumSubArray, maxSum = findContiguousSubsetWithLargestSum(array)

    print("Your Array :", array)
    print("Contiguous Subset With Largest Sum :", maxSumSubArray)
    print("Sum :", maxSum)
    printSeperator()
#endregion

#region Test Part4
# To test it create an object of Graph with Vertex ///myGraph = Graph(4)////
# Then initialize the 2D array which is represents the Graph
# Then call isBipartiteGraph method with Graph object.
# It return True if it is bipartite graph
def testPart4():
    printSeperator()
    print("Algorithm HW4 Part4")
    print("Your Adjacency Matrix Graph is")
    myGraph = Graph(4) # This is number of vertex.
    myGraph.graph = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]

    ]
    printGraphWithMatrixRepresentation(myGraph)
    myGraph.printGraph()

    isBipartite = isBipartiteGraph(myGraph)
    if (isBipartite == True):
        print("The Graph is Bipartite")
    else:
        print("The Graph is not Bipartite")

    print("Your Adjacency Matrix Graph is")
    myGraph = Graph(4)  # This is number of vertex.
    myGraph.graph = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 1]
    ]
    printGraphWithMatrixRepresentation(myGraph)
    myGraph.printGraph()

    isBipartite = isBipartiteGraph(myGraph)
    if (isBipartite == True):
        print("The Graph is Bipartite")
    else:
        print("The Graph is not Bipartite")

    printSeperator()

#endregion

#region Test Part5
# To test it create 2 array.
# Last index of Cost array must be NoBuy
# First index of Price array must be NoSale
# Call findBestDayToBuyGood method with arrays
# It returns best day and gain value to buy good
# If it returns ERROR there is no day to make money.
def testPart5():
    printSeperator()
    print("Algorithm HW4 Part5")
    Cost = [5, 11, 2, 21, 5, 7, 8, 12, 13, NoBuy]
    Price = [NoSale, 7, 9, 5, 21, 7, 13, 10, 14, 20]
    print("Your Cost is")
    printCostOrPrice(Cost)
    print("Your Price is")
    printCostOrPrice(Price)

    Day, GainAmounth = findBestDayToBuyGood(Cost, Price)

    if(Day != ERROR and GainAmounth != ERROR):
        print("The best day to buy goods is the " + str(Day) + "th day")
        print("The gain is", GainAmounth)

    else:
        print("There is no day to make money")

    printSeperator()


#endregion

if __name__ == '__main__':
    testPart1_b()
    testPart1_c()
    testPart2()
    testPart3()
    testPart4()
    testPart5()
    printSeperator()
    print("151044058 ALİ HAYDAR KURBAN")
    printSeperator()