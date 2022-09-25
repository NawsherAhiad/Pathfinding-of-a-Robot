inputFile = open("Input File(NR).txt", "r")

x = float(inputFile.readline())
es = float(inputFile.readline())
maxItr = int(inputFile.readline())
n = int(inputFile.readline())


coefficients = []
for i in range(0, n+1):
    coefficients.append(float(inputFile.readline()))

inputFile.close()


def func(x):
    sum = 0
    for i in range(0, n+1):
        sum = sum + coefficients[i]*pow(x, i)

    return sum


def func2(x):
    sum = 0

    for i in range(1, n + 1):
        sum = sum + i*coefficients[i] * pow(x, i - 1)
    return sum


def nr(x):
    ea = 9999
    currentItr = 1

    outputFile = open("Output File(NR).txt", "w")

    while ea >= es and currentItr <= maxItr:
        xcurrent = float((x -(func(x) / func2(x))))
        ea = float(abs((xcurrent - x) / xcurrent))
        print("iteration no: ", currentItr, "Xi: ", round(x, 4), " Xi+1: ", round(xcurrent, 4), " epsilon a: ", round(ea, 4))
        outputFile.write("iteration no: ")
        outputFile.write(str(round(currentItr, 4)))
        outputFile.write(" Xi: ")
        outputFile.write(str(round(x, 4)))
        outputFile.write(" Xi+1: ")
        outputFile.write(str(round(xcurrent, 4)))
        outputFile.write(" epsilon a: ")
        outputFile.write(str(round(ea, 4)))
        outputFile.write("\n")
        x = xcurrent
        currentItr = currentItr + 1

    outputFile.write("estimated root: ")
    outputFile.write(str(round(xcurrent, 4)))
    outputFile.close()

    return xcurrent


ans = nr(x)
print("estimated root: ", round(ans, 4))