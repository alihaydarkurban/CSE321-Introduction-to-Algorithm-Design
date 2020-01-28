from random import randint  # This is for random index to create fake coin

fakeWeight = 404  # This is weight for fake coin


######################################-----PART1 METHODS-----######################################
class Boxes:
    boxList = []

    def __init__(self, size):
        self.size = 2 * size
        self.start = 0
        self.end = self.size - 1
        self.boxList.clear()

        for i in range(size):
            self.boxList.append('B')

        for i in range(size):
            self.boxList.append('W')

    def makePattern(self):
        self.makePatternRecursive(self.start, self.end)

    def makePatternRecursive(self, start, end):
        if (start >= int(self.size / 2)):
            return
        else:
            if (start % 2 != 0 and end % 2 == 0):
                self.boxList[start], self.boxList[end] = self.boxList[end], self.boxList[start]

            start = start + 1
            end = end - 1
            self.makePatternRecursive(start, end)

    def printBoxList(self):
        print(self.boxList)


###################################################################################################

######################################-----PART2 METHODS-----######################################
class Coin:
    weight = 10

    def __init__(self, name):
        self.name = name

    def printCoin(self):
        print("Name :", self.name, "Weight :", self.weight)


def createCoins(coinsList, num):
    coinsList.clear()
    for i in range(num):
        name = "Coin_" + str(i)
        coin = Coin(name)
        coinsList.append(coin)

    fakeCoinIndex = randint(0, num - 1)

    coinsList[fakeCoinIndex].weight = fakeWeight;


def printCoinsList(coinsList):
    for i in range(len(coinsList)):
        coinsList[i].printCoin()


def findFakeCoin(coinsList):
    return findFakeCoinRecursive(0, len(coinsList) - 1, coinsList)


def findFakeCoinRecursive(start, end, coinsList):
    if (start >= end):
        return

    if (len(coinsList) == 1 or len(coinsList) == 2):
        print("We can not understand which is the fake coin")
        return

    else:
        if (coinsList[start].weight == coinsList[start + 1].weight):
            notFakeWeight = coinsList[start].weight
            return helperRecursive(coinsList, notFakeWeight, 2)
        else:
            tempWeight = coinsList[start + 2].weight
            if (tempWeight == coinsList[start].weight):
                return coinsList[start + 1]
            else:
                return coinsList[start]


def helperRecursive(coinsList, notFakeWeight, index):
    if (index >= len(coinsList)):
        return
    else:
        if (coinsList[index].weight == notFakeWeight):
            index = index + 1
            return helperRecursive(coinsList, notFakeWeight, index)
        else:
            return coinsList[index]


###################################################################################################

######################################-----PART3 METHODS-----######################################
def insertionSort(array):
    countOfSwap = 0
    for index in range(1, len(array)):
        currentItem = array[index]

        sortedIndex = index - 1
        while (sortedIndex >= 0 and currentItem < array[sortedIndex]):
            array[sortedIndex + 1] = array[sortedIndex]
            sortedIndex = sortedIndex - 1
            countOfSwap = countOfSwap + 1

        array[sortedIndex + 1] = currentItem

    return array, countOfSwap


def partition(array, start, end, countOfSwap):
    index = (start - 1)
    pivotItem = array[end]

    for pivotIndex in range(start, end):
        if (array[pivotIndex] < pivotItem):
            index = index + 1
            array[index], array[pivotIndex] = array[pivotIndex], array[index]
            countOfSwap = countOfSwap + 1

    array[index + 1], array[end] = array[end], array[index + 1]
    countOfSwap = countOfSwap + 1
    return countOfSwap, (index + 1)


def quickSortRecursive(array, start, end, countOfSwap):
    if (start < end):
        countOfSwap, pivot = partition(array, start, end, countOfSwap)

        array, countOfSwap = quickSortRecursive(array, start, pivot - 1, countOfSwap)
        array, countOfSwap = quickSortRecursive(array, pivot + 1, end, countOfSwap)

    return array,countOfSwap


def quickSort(array):
    return quickSortRecursive(array, 0, len(array) - 1, 0)


###################################################################################################

######################################-----PART4 METHODS-----######################################

def findPivotIndex(unSortedArray, start, end):
    pivot = unSortedArray[end]
    currentPivotIndex = start

    for i in range(start, end):
        if (unSortedArray[i] < pivot):
            unSortedArray[i], unSortedArray[currentPivotIndex] = unSortedArray[currentPivotIndex], unSortedArray[i]
            currentPivotIndex = currentPivotIndex + 1

    unSortedArray[end], unSortedArray[currentPivotIndex] = unSortedArray[currentPivotIndex], unSortedArray[end]

    return currentPivotIndex


def find_kthSmallestItem(unSortedArray, start, end, k):
    pivotIndex = findPivotIndex(unSortedArray, start, end)

    if (pivotIndex == k):
        return unSortedArray[pivotIndex]
    elif (pivotIndex > k):
        return find_kthSmallestItem(unSortedArray, start, pivotIndex - 1, k)
    else:
        return find_kthSmallestItem(unSortedArray, pivotIndex + 1, end, k)


def findMedian(unSortedArray):
    sizeOfArray = len(unSortedArray)
    if (sizeOfArray % 2 == 1):
        middleIndex = int(sizeOfArray / 2)
        median = find_kthSmallestItem(unSortedArray, 0, sizeOfArray - 1, middleIndex)
    else:
        middleIndex_1 = int(sizeOfArray / 2)
        middleIndex_2 = middleIndex_1 - 1

        number_1 = find_kthSmallestItem(unSortedArray, 0, sizeOfArray - 1, middleIndex_1)
        number_2 = find_kthSmallestItem(unSortedArray, 0, sizeOfArray - 1, middleIndex_2)

        median = (number_1 + number_2) / 2

    return median


###################################################################################################

######################################-----PART5 METHODS-----######################################

# This methos uses find_kthSmallestItem method which is implemented in Part4.
def finMaxAndMinItem(array):
    minItem = find_kthSmallestItem(array, 0, len(array) - 1, 0)
    maxItem = find_kthSmallestItem(array, 0, len(array) - 1, len(array) - 1)

    return maxItem, minItem


def findSUM_B(num1, num2, n):
    return ((num1 + num2) * n) / 4


def isGreaterThanOrEqualSumB(array, sumB):
    sum = 0
    returnValue = False
    for i in range(len(array)):
        sum = sum + array[i]

    if (sum >= sumB):
        returnValue = True

    return returnValue


def findSubsets(arrray):
    size = len(arrray)
    SubArrays = []

    maxOfArray, minOfArray = finMaxAndMinItem(arrray)
    sumB = findSUM_B(maxOfArray, minOfArray, size)

    for i in range(0, (2 ** size)):
        subArray = []
        for j in range(0, size):
            if (i & ((2 ** j)) > 0):
                subArray.append(arrray[j])

        controlForSubArray = isGreaterThanOrEqualSumB(subArray, sumB)
        if (controlForSubArray):
            SubArrays.append(subArray)

    return SubArrays


def multiplicationOfArray(array):
    result = 1
    for i in range(len(array)):
        result = result * array[i]
    return result


def findMinimumNumberOfMultiplicationSubset(array):
    subSets = findSubsets(array)
    insideMinSubSet = subSets[0]
    return findRecursive(subSets, 0, insideMinSubSet)


def findRecursive(array, index, minArray):
    if (index >= len(array)):
        return minArray

    else:
        minMultiplication = multiplicationOfArray(minArray)
        localMin = multiplicationOfArray(array[index])
        if (localMin < minMultiplication):
            minArray = array[index]

        return findRecursive(array, index + 1, minArray)


def printSubsets(array):
    for i in range(len(array)):
        print(array[i])


###################################################################################################

# Common used method
def printSeperator():
    print("============================================================================")


# It is for testing Part1.
# To test this part cretae a Boxes object with size n.
# When a Box object created it has "B" and "W" elements.
# First n elements are "B", others are "W".
# Call makePattern method with this object.
# Call printBoxList to show output.
def testPart1():
    printSeperator()
    print("Algorithm HW3 Part1")
    print("Your Box Object : ")
    boxes = Boxes(3)
    boxes.printBoxList()
    print("After Pattern : ")
    boxes.makePattern()
    boxes.printBoxList()
    print()
    print("Your Box Object : ")
    boxes2 = Boxes(6)
    boxes2.printBoxList()
    print("After Pattern : ")
    boxes2.makePattern()
    boxes2.printBoxList()
    printSeperator()


# It is for testing Part2.
# To test this part determine a number which represents the number of coins.
# Create an empty list and call createCoins method with the list and the number.
# createCoins method creates coins and append the list.
# Index of fake coin created by randomly.
# Create a variable and call findFakeCoin with the list.
# findFakeCoin finds the fake coin and returns it.
# printCoinsList prints all coins.
# printCoin print one coin.
def testPart2():
    printSeperator()
    print("Algorithm HW3 Part2")
    numberOfCoins = 5
    coinsList = []
    createCoins(coinsList, numberOfCoins)
    print("Your Coins : ")
    printCoinsList(coinsList)
    FakeCoin = findFakeCoin(coinsList)
    print("Fake Coin is : ")
    FakeCoin.printCoin()
    print()
    numberOfCoins = 8
    coinsList = []
    createCoins(coinsList, numberOfCoins)
    print("Your Coins : ")
    printCoinsList(coinsList)
    FakeCoin = findFakeCoin(coinsList)
    print("Fake Coin is : ")
    FakeCoin.printCoin()
    printSeperator()


# It is for testing Part3.
# To test this part create a list of integers.
# Create a integer num which represents the amount of swap during sorting.
# For insertion sort, call insertionSort with the list.
# This method returns sorted list and amount of swap.
# For quick sort, call quickSort with the list.
# This method returns sorted list and amount of swap.
def testPart3():
    printSeperator()
    print("Algorithm HW3 Part3")
    list_1 = [1, 2, 3, 4, 5]
    print("List :", list_1)
    sortedList_1, countOfSwap1 = insertionSort(list_1)
    print("Sorted List (Insertion):", sortedList_1)
    print("countOfSwap :", countOfSwap1)
    print()
    list_2 = [1, 2, 3, 4, 5]
    print("List :", list_2)
    sortedList_2, countOfSwap2 = quickSort(list_2)
    print("Sorted List (Quick):", sortedList_2)
    print("countOfSwap :", countOfSwap2)
    print()
    list_3 = [6, 7, 9, 8, 10]
    print("List :", list_3)
    sortedList_1, countOfSwap1 = insertionSort(list_3)
    print("Sorted List (Insertion):", sortedList_1)
    print("countOfSwap :", countOfSwap1)
    print()
    list_4 = [6, 7, 9, 8, 10]
    print("List :", list_4)
    sortedList_2,countOfSwap2 = quickSort(list_4)
    print("Sorted List (Quick):", sortedList_2)
    print("countOfSwap :", countOfSwap2)
    print()
    list_5 = [10, 7, 8, 9, 1, 5]
    print("List :", list_5)
    sortedList_1, countOfSwap1 = insertionSort(list_5)
    print("Sorted List (Insertion):", sortedList_1)
    print("countOfSwap :", countOfSwap1)
    print()
    list_6 = [10, 7, 8, 9, 1, 5]
    print("List :", list_6)
    sortedList_2,countOfSwap2 = quickSort(list_6)
    print("Sorted List (Quick):", sortedList_2)
    print("countOfSwap :", countOfSwap2)
    printSeperator()


# It is for testing Part4.
# To test this part create a list of integer item.
# Call findMedian method with the list.
# findMedian retunrs the median of the list.
def testPart4():
    printSeperator()
    print("Algorithm HW3 Part4")
    unSortedArray_1 = [14, 55, 27, 11, 20, 19, 49, 47, 88]
    unSortedArray_2 = [48, 24, 30, 8, 11, 29, 1, 4]

    print("Your Unsorted Array is :")
    print(unSortedArray_1)
    median = findMedian(unSortedArray_1)
    print("Median is :", median)
    print()
    print("Your Unsorted Array is :")
    print(unSortedArray_2)
    median = findMedian(unSortedArray_2)
    print("Median is :", median)
    printSeperator()


# It is for testing Part5.
# To test this part create a list of integer item.
# Call findMinimumNumberOfMultiplicationSubset with the list.
# findMinimumNumberOfMultiplicationSubset returns a list of subset of A.
def testPart5():
    printSeperator()
    print("Algorithm HW3 Part5")
    A = [2, 4, 7, 5, 22, 11]

    # allSubsetsOfGivenCondition = findSubsets(A)    #These lines print all subsets which are >= SUM_B.
    # printSubsets(allSubsetsOfGivenCondition)

    optimalSubSet = findMinimumNumberOfMultiplicationSubset(A)
    print("The optimal sub-set is", optimalSubSet)
    printSeperator()


if __name__ == '__main__':
    ###############----PART1 TEST---###################
    testPart1()
    ###################################################

    ###############----PART2 TEST---###################
    testPart2()
    ###################################################

    ###############----PART3 TEST---###################
    testPart3()
    ###################################################

    ###############----PART4 TEST---###################
    testPart4()
    ###################################################

    ###############----PART5 TEST---###################
    testPart5()
    ###################################################