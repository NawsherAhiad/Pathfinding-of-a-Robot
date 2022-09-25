inputFile = open("Input File(S).txt", "r")
Xp = float(inputFile.readline())
x = float(inputFile.readline())
es = float(inputFile.readline())
maxItr = int(inputFile.readline())
n = int(inputFile.readline())

coefficients = []
for i in range(0, n+1):
    coefficients.append(float(inputFile.readline()))

inputFile.close()


def func(z):
    sum = 0
    for i in range(0, n+1):
        sum = sum + coefficients[i]*pow(z, i)

    return sum


def secant(x, Xp):
    ea = 9999
    currentItr = 1
    outputFile = open("Output File(S).txt", "w")

    while ea >= es and currentItr <= maxItr:
        Xcurrent = float(x - ((func(x)*(Xp - x)) / ( func(Xp) - func(x))))
        ea = float(abs((Xcurrent - x) / Xcurrent))
        print("iteration no: ", round(currentItr, 4), "Xi-1 :", round(Xp, 4), "Xi: ", round(x, 4), "Xi+1: ", round(Xcurrent, 4), "Epsilon a:", round(ea, 4))
        outputFile.write("iteration no: ")
        outputFile.write(str(round(currentItr, 4)))
        outputFile.write(" Xi-1: ")
        outputFile.write(str(round(Xp, 4)))
        outputFile.write(" Xi: ")
        outputFile.write(str(round(x, 4)))
        outputFile.write(" Xi+1: ")
        outputFile.write(str(round(Xcurrent, 4)))
        outputFile.write(" Epsilon a: ")
        outputFile.write(str(round(ea, 4)))
        outputFile.write("\n")
        Xp = x
        x = Xcurrent
        currentItr = currentItr + 1

    outputFile.write("estimated root: ")
    outputFile.write(str(round(Xcurrent, 4)))
    outputFile.close()

    return Xcurrent


ans = secant(x,Xp)
print("estimated root: ", round(ans, 4))