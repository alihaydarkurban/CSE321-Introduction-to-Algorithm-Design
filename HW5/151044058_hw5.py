#region Global Values
ERROR = -404
START = 0
END = 1
match_score = 2
mismatch_score = -2
gap_score = -1
MAX_SUM = 999
#endregion

#region Print Seperator
def printSeperator():
    print("=======================================================================================")
#endregion

#region Part1 Methods
def optimalPlan(NY, SF, M):
    if((len(NY) != len(SF)) or M < 0):
        return ERROR
    else:
        return optimalPlanDynamicAlgorithm(NY, SF, M, len(NY))


def optimalPlanDynamicAlgorithm(NY, SF, M, n):
    OPT_NY = [0 for i in range(n)]
    OPT_SF = [0 for i in range(n)]

    for i in range(n):
        if(i == 0):
            OPT_NY[i] = NY[i] + min(OPT_NY[i - 1], M)
            OPT_SF[i] = SF[i] + min(OPT_SF[i - 1], M)
        else:
            OPT_NY[i] = NY[i] + min(OPT_NY[i - 1], M + OPT_SF[i - 1])
            OPT_SF[i] = SF[i] + min(OPT_SF[i - 1], M + OPT_NY[i - 1])

    return min(OPT_NY[n - 1], OPT_SF[n - 1])
#endregion

#region Part2 Methods
def optimalSessions(activitiesArray):
    if(len(activitiesArray) == 0):
        return ERROR

    activitiesArray.sort(key= lambda x : x[1], reverse= False)

    returnValueArray = []
    i = 0
    if(activitiesArray[i][START] >= activitiesArray[i][END]):
        return ERROR

    returnValueArray.append(activitiesArray[i])

    for j in range(1, len(activitiesArray)):
        newActivity = activitiesArray[j]
        oldActivity = activitiesArray[i]

        if(newActivity[START] >= newActivity[END]):
            return ERROR

        if(newActivity[START] >= oldActivity[END]):
            returnValueArray.append(newActivity)
            i = j

    return returnValueArray
#endregion

#region Part3 Methods
def totalSumEqualsToZero(array):
    if(len(array) == 0):
        return ERROR

    TableOfDP = [[False for i in range(MAX_SUM)] for j in range(len(array))]
    isChecked = [[False for i in range(MAX_SUM)] for j in range(len(array))]
    sumEqualZeroArray = []
    return totalSumEqualsToZeroDP(0, 0, array, len(array), TableOfDP, isChecked, sumEqualZeroArray)

def totalSumEqualsToZeroDP(index, sum_, array, size, table_of_dp, is_checked, sum_equal_zero_array):
    if(index == size):
        if(sum_ == 0):
            if(len(sum_equal_zero_array) != 0):
                print("The subset with the total sum of elements equal to zero is")
                print(sum_equal_zero_array)
                return True
            else:
                return False
        else:
            return False

    if(is_checked[index][sum_ + size] == True):
        return table_of_dp[index][sum_ + size]

    is_checked[index][sum_ + size] = True

    sum_equal_zero_array.append(array[index])

    if(table_of_dp[index][sum_ + size] != True):
        table_of_dp[index][sum_ + size] = totalSumEqualsToZeroDP(index + 1, sum_ + array[index], array, size, table_of_dp, is_checked, sum_equal_zero_array)
    else:
        return True

    del sum_equal_zero_array[-1]

    if(table_of_dp[index][sum_ + size] != True):
        table_of_dp[index][sum_ + size] = totalSumEqualsToZeroDP(index + 1, sum_, array, size, table_of_dp, is_checked, sum_equal_zero_array)
    else:
        return True

    return table_of_dp[index][sum_ + size]

#endregion

#region Part4 Methods
def printAlignment(start, end, string):
    for i in range(start, end):
        print(string[i], end="")
    print()
def findAlignment(string1, string2):
    len_string1 = len(string1)
    len_string2 = len(string2)
    temp_length1 = 0
    temp_length2 = 0
    N = 0 # Represents the match count
    M = 0 # Represents the mismatch count
    K = 0 # Represents the gap count

    TableOfDP = [[0 for i in range(len_string1 + len_string2 + 1)] for j in range(len_string1 + len_string2 + 1)]

    for i in range(len_string1 + len_string2 + 1):
        TableOfDP[i][0] = i * gap_score
        TableOfDP[0][i] = i * gap_score

    for i in range(1, len_string1 + 1):
        for j in range(1, len_string2 + 1):
            if(string1[i - 1] == string2[j - 1]):
                TableOfDP[i][j] = TableOfDP[i - 1][j - 1]
            else:
                max1 = max((TableOfDP[i - 1][j - 1] + mismatch_score),(TableOfDP[i - 1][j] + gap_score))
                max2 = max(max1, (TableOfDP[i][j - 1] + gap_score))

                TableOfDP[i][j] = max(max1, max2)

    totalLength = len_string1 + len_string2

    i = len_string1
    j = len_string2

    string1Result = [0 for x in range(totalLength + 1)]
    string2Result = [0 for x in range(totalLength + 1)]

    string1Index = totalLength
    string2Index = totalLength

    loopEndControl = True
    while(loopEndControl):
        if(string1[i - 1] == string2[j - 1]):
            string1Result[string1Index] = string1[i - 1]
            string2Result[string2Index] = string2[j - 1]

            string1Index = string1Index - 1
            string2Index = string2Index - 1

            temp_length1 = temp_length1 + 1
            temp_length2 = temp_length2 + 1

            i = i - 1
            j = j - 1
            N = N + 1

        elif(TableOfDP[i - 1][j - 1] + mismatch_score == TableOfDP[i][j]):
            string1Result[string1Index] = string1[i - 1]
            string2Result[string2Index] = string2[j - 1]

            string1Index = string1Index - 1
            string2Index = string2Index - 1

            temp_length1 = temp_length1 + 1
            temp_length2 = temp_length2 + 1

            i = i - 1
            j = j - 1
            M = M + 1

        elif(TableOfDP[i][j - 1] + gap_score == TableOfDP[i][j]):
            string1Result[string1Index] = '_'
            string2Result[string2Index] = string2[j - 1]

            string1Index = string1Index - 1
            string2Index = string2Index - 1

            j = j - 1

            temp_length2 = temp_length2 + 1

            if(i < len_string1):
                temp_length1 = temp_length1 + 1
                K = K + 1

        elif(TableOfDP[i - 1][j] + gap_score == TableOfDP[i][j]):
            string1Result[string1Index] = string1[i - 1]
            string2Result[string2Index] = '_'

            string1Index = string1Index - 1
            string2Index = string2Index - 1

            i = i - 1

            temp_length1 = temp_length1 + 1

            if(j < len_string2):
                temp_length2 = temp_length2 + 1
                K = K + 1

        if(i == 0 or j == 0):
            loopEndControl = False

    # These loop are filled string1Result and string2Result
    # if above while loop terminated before the end string1 or string2
    while(string1Index > 0):
        if(i > 0):
            i = i - 1
            string1Result[string1Index] = string1[i]
            string1Index = string1Index - 1
            temp_length1 = temp_length1 + 1
            temp_length2 = temp_length2 + 1
            K = K + 1
        else:
            string1Result[string1Index] = '_'
            string1Index = string1Index - 1

    while(string2Index > 0):
        if(j > 0):
            j = j - 1
            string2Result[string2Index] = string2[j]
            string2Index = string2Index - 1
            temp_length1 = temp_length1 + 1
            temp_length2 = temp_length2 + 1
            K = K + 1
        else:
            string2Result[string2Index] = '_'
            string2Index = string2Index - 1

    print("-------------------")
    print("PRINT THE ALIGNMENT")
    print("-------------------")
    indexOfStart = 0 ###
    controlToExit = False
    for i in range(totalLength, 2, -1):
        if(string2Result[i] == '_' and string1Result[i] == '_' and controlToExit == False):
            indexOfStart = i + 1
            controlToExit = True

    printAlignment(indexOfStart, indexOfStart + temp_length1, string1Result)
    printAlignment(indexOfStart, indexOfStart + temp_length2, string2Result)

    print("Match Score :", N)
    print("Mismatch Score :", M)
    print("Gap Score :", K)

    return (N * match_score) + (M * mismatch_score) + (K * gap_score)
#endregion

#region Part5 Methods
def makeAllPositive(array):
    # True means that positive, False means that negative
    numAndId = []
    for i in range(len(array)):
        if(array[i] < 0):
            numAndId.append([-1 * array[i],False])
        else:
            numAndId.append([array[i],True])

    return numAndId

def findMinimumNumberOfOperations(array):
    if(len(array) < 2):
        return ERROR, ERROR

    mappedArray = makeAllPositive(array)
    mappedArray.sort() #It sorts the mappedArray based first index.
    #  print(mappedArray)
    operationCountArray = []
    sumOfArray = 0
    tempOperation = 0
    for i in range(0, len(mappedArray)):

        if(i == 1 or i == 0):
            if(i == 1):
                temp = mappedArray[i - 1][0] + mappedArray[i][0]
                tempOperation = temp
        else:
            if(sumOfArray < 0):
                temp = (-1)*sumOfArray + mappedArray[i][0]
            else:
                temp = sumOfArray + mappedArray[i][0]

            tempOperation = temp

        if (mappedArray[i][1] == False):
            sumOfArray = sumOfArray + ((-1) * mappedArray[i][0])
        else:
            sumOfArray = sumOfArray + mappedArray[i][0]

        if (i != 0):
            operationCountArray.append(tempOperation)
            # print("sum", sumOfArray, end="")
            # print(" op", tempOperation)

    minOperationCount = sum(operationCountArray)
    return sumOfArray, minOperationCount
#endregion

#region Test Part1
def testPart1():
    printSeperator()
    print("Algorithm HW5 Part1")
    NY = [1, 3, 20, 30]
    SF = [50, 20, 2, 4]
    M = 10
    cost = optimalPlan(NY, SF, M)
    if(cost == ERROR):
        print("You are making a mistake in creating values!")
    else:
        print("NY :",NY)
        print("SF :",SF)
        print("Cost of the optimal plan :", cost)

    print()

    NY = [5, 30, 4, 30, 25]
    SF = [10, 2, 40, 6, 10]
    M = 10
    cost = optimalPlan(NY, SF, M)
    if(cost == ERROR):
        print("You are making a mistake in creating values!")
    else:
        print("NY :",NY)
        print("SF :",SF)
        print("Cost of the optimal plan :", cost)
    printSeperator()
#endregion

#region Test Part2
def testPart2():
    printSeperator()
    print("Algorithm HW5 Part2")
    # Activities array has activity arrays.
    # First index represents the start time of it.
    # Second index represents the finish time of it.
    allActivities = [
        [4, 8],
        [2, 3],
        [4, 5],
        [1, 5],
        [6, 8],
        [8, 9],
        [1, 4]
    ]
    copyActivities = allActivities.copy()
    activities = optimalSessions(allActivities)

    if(activities == ERROR):
        print("You are making a mistake in creating value!")

    else:
        print("Activities :", copyActivities)
        print("You can join " + str(len(activities)) + " sessions.\n"
        "These sessions are :", activities)

    print()


    # Activities array has activity arrays.
    # First index represents the start time of it.
    # Second index represents the finish time of it.
    allActivities = [
        [2, 4],
        [1, 5],
        [2, 3],
        [5, 7],
        [3, 10],
        [6, 9],
        [4, 6],
        [5, 6]

    ]
    copyActivities = allActivities.copy()
    activities = optimalSessions(allActivities)

    if(activities == ERROR):
        print("You are making a mistake in creating value!")

    else:
        print("Activities :", copyActivities)
        print("You can join " + str(len(activities)) + " sessions.\n"
        "These sessions are :", activities)


    printSeperator()
#endregion

#region Test Part3
def testPart3():
    printSeperator()
    print("Algorithm HW5 Part3")
    S = [-1, 6, 4, 2, 3, -7, -5]
    if(len(S) != 0):
        print("Your set of integers is :", S)
    isThereAnyZeroSum = totalSumEqualsToZero(S)
    if(isThereAnyZeroSum == ERROR):
        print("You are making a mistake in creating value!")
    elif(isThereAnyZeroSum == False):
        print("There is no subset that sum of the elements equal to zero!")

    print()


    S = [2, -4, -2, 3, 5, -1 ]
    if(len(S) != 0):
        print("Your set of integers is :", S)
    isThereAnyZeroSum = totalSumEqualsToZero(S)
    if(isThereAnyZeroSum == ERROR):
        print("You are making a mistake in creating value!")
    elif(isThereAnyZeroSum == False):
        print("There is no subset that sum of the elements equal to zero!")

    printSeperator()
#endregion

#region Test Part4
def testPart4():
    printSeperator()
    print("Algorithm HW5 Part4")


    sequence_A = "ALIGNMENT"
    sequence_B = "XLGNMYENT"

    if(len(sequence_A) == 0 or len(sequence_B) == 0):
        print("You are making a mistake in creating value")
    else:
        print("Your sequence_A is :", sequence_A)
        print("Your sequence_B is :", sequence_B)
        minCost = findAlignment(sequence_A, sequence_B)
        print("Minimum Cost :", minCost)

    print()

    sequence_A = "SEQUENCE"
    sequence_B = "ESUENKCE"

    if(len(sequence_A) == 0 or len(sequence_B) == 0):
        print("You are making a mistake in creating value")
    else:
        print("Your sequence_A is :", sequence_A)
        print("Your sequence_B is :", sequence_B)
        minCost = findAlignment(sequence_A, sequence_B)
        print("Minimum Cost :", minCost)
    printSeperator()
#endregion

#region Test Part5
def testPart5():
    printSeperator()
    print("Algorithm HW5 Part5")

    arrayOfIntegers = [1, 4, 2, 3]
    sumOfArray, minOperationCount = findMinimumNumberOfOperations(arrayOfIntegers)

    if(sumOfArray == ERROR or minOperationCount == ERROR):
        print("You are making a mistake in creating values!")
    else:
        print("Your integer array is :", arrayOfIntegers)
        print("Sum of it :", sumOfArray)
        print("Minimum number of operation :", minOperationCount)

    print()

    arrayOfIntegers = [1,-6, 4,-11, 8]
    sumOfArray, minOperationCount = findMinimumNumberOfOperations(arrayOfIntegers)

    if(sumOfArray == ERROR or minOperationCount == ERROR):
        print("You are making a mistake in creating values!")
    else:
        print("Your integer array is :", arrayOfIntegers)
        print("Sum of it :", sumOfArray)
        print("Minimum number of operation :", minOperationCount)

    printSeperator()
#endregion

if __name__ == '__main__':
    testPart1()
    testPart2()
    testPart3()
    testPart4()
    testPart5()
    printSeperator()
    print("151044058 ALİ HAYDAR KURBAN")
    printSeperator()