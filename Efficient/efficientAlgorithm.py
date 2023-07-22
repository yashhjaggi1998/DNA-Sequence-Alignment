from sys import argv
import time
import efficientConstants as eC
import efficientIO as eIO
import efficientUtils as eUtils
import efficientOpt as eOpt
import efficientCostMatrix as eCM

#helper: recursive call
def helper(inputSeq1, inputSeq2, alpha, delta):
    #initializations
    inputSeq1L = len(inputSeq1)
    inputSeq2L = len(inputSeq2)
    
    if inputSeq1L <= 2 or inputSeq2L <= 2:
        #soln from basic algo to solve divided probs
        cost = eCM.getCMxBasic(inputSeq1, inputSeq2, alpha, delta)
        return eOpt.optimalCostFinder(cost, inputSeq1, inputSeq2, alpha, delta)

    xLeft = inputSeq1[ : inputSeq1L//2]
    xRight = inputSeq1[ inputSeq1L//2 : ]

    f = eCM.getCostMatrix(xLeft, inputSeq2, alpha, delta)
    s = eCM.getCostMatrix(xRight[ : : -1], inputSeq2[ : : -1], alpha, delta)

    result = [ a+b for a,b in zip(f, s[::-1]) ]
    minIndex = result.index( min(result) )

    yLeft = inputSeq2[ : minIndex]
    yRight = inputSeq2[ minIndex : ]

    leftSubproblem = helper(xLeft, yLeft, alpha, delta)
    rightSubproblem = helper(xRight, yRight, alpha, delta)

    return leftSubproblem[0] + rightSubproblem[0], leftSubproblem[1] + rightSubproblem[1], leftSubproblem[2] + rightSubproblem[2]

#main
if __name__ == "__main__":

    if len(argv) != 3:
        print('---------------------------------------------------------------------------------------------')
        print('Invalid arguments format. Please enter $python efficientAlgorithm.py <inputFile> <outputFile>')
        print('---------------------------------------------------------------------------------------------')
        exit(0)
    
    #Read Inputs
    inputSequences, input_indices = eIO.readFile(argv[1])
    inputSeq1 = eUtils.appendString(inputSequences[0], input_indices[0])
    inputSeq2 = eUtils.appendString(inputSequences[1], input_indices[1])
    
    startTime = time.time() #startTime
    outputSeq1, outputSeq2, optimalCost = helper(inputSeq1, inputSeq2, eC.ALPHA, eC.DELTA) #runTime
    endTime = time.time() #endTime

    totalTime = (endTime - startTime)*eC.THOUSAND #endTime-startTime
    
    #write to output.txt file
    eIO.writeFile(argv[2], optimalCost, outputSeq1, outputSeq2, totalTime, eUtils.processMemory())
