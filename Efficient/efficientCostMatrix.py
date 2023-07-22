import efficientUtils as eUtils

def getCMxBasic(inputSeq1, inputSeq2, alpha, delta):
    #initializations
    costMatrix = []
    inputSeq1L = len(inputSeq1)
    inputSeq2L = len(inputSeq2)
    
    #main logic
    for i in range(inputSeq1L+1):
        costMatrix.append([])
        for j in range(inputSeq2L+1):
            costMatrix[-1].append(0)

    for i in range(inputSeq1L+1):
        costMatrix[i][0] = i * delta

    for i in range(inputSeq2L+1):
        costMatrix[0][i] = i * delta

    for i in range(1, inputSeq1L+1):
        for j in range(1, inputSeq2L+1):
            costMatrix[i][j] = min( alpha[eUtils.getHash(inputSeq1[i-1], inputSeq2[j-1])] + costMatrix[i-1][j-1], delta + min(costMatrix[i-1][j], costMatrix[i][j-1]) )

    return costMatrix

def getCostMatrix(inputSeq1, inputSeq2, alpha, delta):
    #initializations
    costMatrix = []
    inputSeq1L = len(inputSeq1)
    inputSeq2L = len(inputSeq2)
    
    #main logic
    for i in range(2):
        costMatrix.append([])
        for j in range(inputSeq2L+1):
            costMatrix[-1].append(0)

    for i in range(inputSeq2L+1):
        costMatrix[0][i] = i * delta

    for i in range(1, inputSeq1L+1):
        costMatrix[1][0] = i * delta
        for j in range(1, inputSeq2L+1):
            costMatrix[1][j] = min( alpha[eUtils.getHash(inputSeq1[i-1], inputSeq2[j-1])] + costMatrix[0][j-1], delta + min(costMatrix[0][j], costMatrix[1][j-1]) )

        for k in range(inputSeq2L+1):
            costMatrix[0][k] = costMatrix[1][k]

    return costMatrix[1]