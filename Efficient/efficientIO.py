def readFile(inputFile):
    inputSequences = []
    inputIndices = []

    with open(inputFile, "r") as fp:
        for line in fp:
            singleRow = line.rstrip("\n") 
            
            if singleRow.isnumeric():
                inputIndices[-1].append((int(singleRow)))
            else:
                inputSequences.append(singleRow)
                inputIndices.append([])

    return inputSequences, inputIndices


def writeFile(outputFile, cost, firstSeq, secondSeq, time, memoryUsage):
    
    with open(outputFile, "w") as fp:
        
        fp.write(str(cost) + "\n")
        fp.write(firstSeq + "\n")
        fp.write(secondSeq + "\n")
        fp.write(str(time) + "\n")
        fp.write(str(memoryUsage))
