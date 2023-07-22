import efficientUtils as eUtils

'''def getOptSolnBasic(cost, inputSeq1, inputSeq2, alpha, delta):
    #initializations
    p1 = len(inputSeq1)
    p2 = len(inputSeq2)
    outputSeq1 = ""
    outputSeq2 = ""
    
    #main logic
    while p1 > 0 and p2 > 0:
        if cost[p1][p2] == alpha[eUtils.getHash(inputSeq1[p1 - 1], inputSeq2[p2 - 1])] + cost[p1 - 1][p2 - 1]:
            outputSeq1 += inputSeq1[p1-1]
            outputSeq2 += inputSeq2[p2-1]
            p1 -= 1
            p2 -= 1
        elif cost[p1][p2] == delta + cost[p1][p2-1]:
            outputSeq1 += '_'
            outputSeq2 += inputSeq2[p2-1]
            p2 -= 1
        else:
            outputSeq1 += inputSeq1[p1-1]
            outputSeq2 += '_'
            p1 -= 1
    
    while p1 > 0:
        outputSeq1 += inputSeq1[p1-1]
        outputSeq2 += '_'
        p1 -= 1
    while p2 > 0:
        outputSeq1 += '_'
        outputSeq2 += inputSeq2[p2-1]
        p2 -= 1

    return outputSeq1[::-1], outputSeq2[::-1], cost[len(inputSeq1)][len(inputSeq2)]
'''
UNDERSCORE='_'
SINGLE_VALUE = 1
# Get optimal solution - basic version
def optimalCostFinder(cost, strFirst, strSecond, keyValPair, fixedCost):
    strFir = ""
    strSec = ""
    firstInd = len(strFirst)
    secondInd = len(strSecond)

    # while ko for me krdo !!!!!!!!!!!!!!!!!!!!
    while firstInd > 0 and secondInd > 0:
        # isko switch statement me krdo !!!!!!!!!!!!
        if cost[firstInd][secondInd] == cost[firstInd - SINGLE_VALUE][secondInd - SINGLE_VALUE] + keyValPair[eUtils.getHash(strFirst[firstInd - SINGLE_VALUE], strSecond[secondInd - SINGLE_VALUE])]:
            firstInd = firstInd - SINGLE_VALUE
            secondInd = secondInd - SINGLE_VALUE
            strFir = strFir + strFirst[firstInd] 
            strSec = strSec + strSecond[secondInd] 
        elif cost[firstInd][secondInd] == cost[firstInd][secondInd-SINGLE_VALUE] + fixedCost:
            secondInd = secondInd - SINGLE_VALUE
            strFir = strFir + UNDERSCORE
            strSec = strSec + strSecond[secondInd]
        else:
            strFir = strFir + strFirst[firstInd-SINGLE_VALUE]
            strSec = strSec + UNDERSCORE
            firstInd = firstInd -  SINGLE_VALUE
            # for me krdo!!!!!!!!!!
    while firstInd > 0:
        strFir = strFir + strFirst[firstInd-SINGLE_VALUE]
        strSec = strSec + UNDERSCORE
        firstInd = firstInd - SINGLE_VALUE
        # for me krdo!!!!!!!!!!
    while secondInd > 0:
        strFir = strFir + UNDERSCORE
        strSec = strSec + strSecond[secondInd-SINGLE_VALUE]
        secondInd = secondInd - SINGLE_VALUE

    # ye change krdo, kuch or krke return kro, not same to same!!!!!!!!!!
    return strFir[::-1], strSec[::-1], cost[len(strFirst)][len(strSecond)]