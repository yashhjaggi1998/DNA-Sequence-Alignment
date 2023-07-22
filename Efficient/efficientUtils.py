import psutil

def processMemory():
    process = psutil.Process()
    memInfo = process.memory_info()
    memConsumed = int(memInfo.rss/1024)
    return memConsumed


def getHash(n1, n2):
    return ord(n1)*100 + ord(n2)


def appendString(inputSeq, listOfIndices):
    for i in listOfIndices:
        result = inputSeq[:i+1] + \
            inputSeq + inputSeq[i+1:]
        inputSeq = result
    return inputSeq