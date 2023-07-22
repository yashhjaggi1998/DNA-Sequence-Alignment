from sys import argv
import costsMapping
import psutil
import util
import time


# Process memory checker
def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed

# Hash calculator
def get_hash(a, b):
    return ord(a)*100 + ord(b)


UNDERSCORE='_'
SINGLE_VALUE = 1
# Get optimal solution - basic version
def optimalCostFinder(cost, strFirst, strSecond, keyValPair, fixedCost):
    strFir = ""
    strSec = ""
    firstInd = len(strFirst)
    secondInd = len(strSecond)

    # while ko for me krdo !!!!!!!!!!!!!!!!!!!!
    while firstInd >=SINGLE_VALUE and secondInd >=SINGLE_VALUE:
        # isko switch statement me krdo !!!!!!!!!!!!
        if cost[firstInd][secondInd] == cost[firstInd - SINGLE_VALUE][secondInd - SINGLE_VALUE] + keyValPair[get_hash(strFirst[firstInd - SINGLE_VALUE], strSecond[secondInd - SINGLE_VALUE])]:
            firstInd = firstInd - SINGLE_VALUE
            secondInd = secondInd - SINGLE_VALUE
            strFir = strFirst[firstInd-SINGLE_VALUE] + strFir
            strSec = strSecond[secondInd-SINGLE_VALUE] + strSec
        elif cost[firstInd][secondInd] == cost[firstInd][secondInd-SINGLE_VALUE] + fixedCost:
            secondInd = secondInd - SINGLE_VALUE
            strFir = UNDERSCORE + strFir
            strSec = strSecond[secondInd-SINGLE_VALUE] + strSec
        else:
            strFir = strFirst[firstInd-SINGLE_VALUE] + strFir
            strSec = UNDERSCORE + strSec
            firstInd = firstInd -  SINGLE_VALUE
            # for me krdo!!!!!!!!!!
    while firstInd >=SINGLE_VALUE:
        strFir = strFirst[firstInd-SINGLE_VALUE] + strFir
        strSec = UNDERSCORE + strSec
        firstInd = firstInd - SINGLE_VALUE
        # for me krdo!!!!!!!!!!
    while secondInd >=SINGLE_VALUE:
        strFir = UNDERSCORE + strFir
        strSec = strSecond[secondInd-SINGLE_VALUE] + strSec
        secondInd = secondInd - SINGLE_VALUE

    # ye change krdo, kuch or krke return kro, not same to same!!!!!!!!!!
    return strFir[::-1], strSec[::-1], cost[len(strFirst)][len(strSecond)]


SING_VAL = 1
#get_cost_matrix equivalent in reference code
def basicCostFinder(keyVal, fixCost, firstStr, secStr):
    firstLen = len(firstStr)
    secondLen = len(secStr)
    cost_matrix = []
    for _ in range(firstLen+SING_VAL):
        cost_matrix.append([])
        for __ in range(secondLen+SING_VAL):
            cost_matrix[-SING_VAL].append(0)

    ## change to while!!!!!
    for zz in range(firstLen+SING_VAL):
        cost_matrix[zz][0] = zz * fixCost

## change to while!!!!!
    for op in range(secondLen+SING_VAL):
        cost_matrix[0][op] = op * fixCost

## change to while!!!!!
    for rw in range(SING_VAL, firstLen+SING_VAL):
        for np in range(SING_VAL, secondLen+1):
            cost_matrix[rw][np] = min(
                keyVal[get_hash(firstStr[rw - SING_VAL], secStr[np - SING_VAL])
                      ] + cost_matrix[rw - SING_VAL][np - SING_VAL],
                fixCost + min(cost_matrix[rw - SING_VAL][np], cost_matrix[rw][np - SING_VAL]))

    return cost_matrix



VALID_FORMAT = 'Valid format : python basic_3.py <inputFile> <outputPath>'
INVALID_ARGUMENT = 'Invalid number of Arguments'
# Argument validater
def validateArguments(totalArguments):
    if (len(totalArguments) != 3):
        print(INVALID_ARGUMENT+" | "+VALID_FORMAT)
        exit(0)


if __name__ == "__main__":

    # initialize
    VALMUL = 1000

    # Check for valid number of arguments
    validateArguments(argv)

    # Read the Input file
    inputIndices, inputStrings = util.readInputFile(argv[1])

    # Expanding the Strings
    inputStr1 = util.stringExpansion(inputIndices[0], inputStrings[0])
    inputStr2 = util.stringExpansion(inputIndices[1], inputStrings[1])

    # Assign Delta and Alpha costs respectively
    deltaCost = costsMapping.deltaCost
    alphaCost = costsMapping.alphaCost

    timerStart = time.time()
    totCost = basicCostFinder(alphaCost, deltaCost, inputStr1, inputStr2)
    timerEnd = time.time()

    ## ISKO CHANGE KRDO !!!!!!
    time_taken = VALMUL * (timerEnd - timerStart)
    strOutputFirst, stringOutputSecond, optimalCosting = optimalCostFinder(
        totCost, inputStr1, inputStr2, alphaCost, deltaCost)
    util.write_output_file(argv[2], optimalCosting,
                           strOutputFirst, stringOutputSecond, time_taken, process_memory())
