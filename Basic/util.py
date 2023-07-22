def readInputFile(input_file):

    # Initialize input arrays
    inputIndices = []
    inputStrings = []

    # Open and Read from Input file
    with open(input_file, "r") as file:
        for line in file:
            plainLine = line.rstrip("\n")
            if plainLine.isnumeric():
                inputIndices[-1].append((int(plainLine)))
            else:
                inputStrings.append(plainLine)
                inputIndices.append([])

    return inputIndices, inputStrings


def write_output_file(output_file, cost, first_string, second_string, time, mem):

    # Open and write into the file
    with open(output_file, "w") as file:
        file.write(str(cost)+"\n")
        file.write(first_string+"\n")
        file.write(second_string+"\n")
        file.write(str(time)+"\n")
        file.write(str(mem))


def stringExpansion(indicesList, inputStr):
    for i in indicesList:
        resultStr = inputStr[: i+1] + inputStr + inputStr[i+1:]
        inputStr = resultStr

    return inputStr
