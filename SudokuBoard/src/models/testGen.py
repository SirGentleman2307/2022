#******************************************************************************
#  This makes test.txt for the sudoku
#  Text explain
#
#
#
#
#
#******************************************************************************

import os
#Global values
testPath = "\\".join(os.path.dirname(__file__).split("\\")[0:-1]) + "\\tests\\"

def makeFile(fileName,sudokuString):
    # test = "100000000020000000003000000000400000000050000000006000000000700000000080000000009"
    # test = "111222333111222333111222333444555666444555666444555666777888999777888999777888999"
    filePath = testPath + fileName + ".txt"
    with open(filePath,"w",encoding='utf8') as f:
        # Start by spliting the long string into rows with 9 ints
        bigSplit = [sudokuString[index : index + 9] for index in range(0, len(sudokuString), 9)]
        count = 0
        for bigPiece in bigSplit:
            count += 1
            # Split the row into 3 ints
            smallSplit = [bigPiece[index : index + 3] for index in range(0, len(bigPiece), 3)]
            f.write("│".join(smallSplit) + "\n")
            # When 3 rows are printed add the sepirator
            if count == 3 or count == 6:
                f.write("───┼───┼───\n")

def genTest():
    return

if __name__ == '__main__':
    if input() == "1":
        fileName = input("Enter in file name: ")
        filePath = testPath + fileName + ".txt"
        try:
            with open(filePath,"r",encoding='utf8') as f:
                print(f.read())
        except:
            print("No file found named %s" % fileName)
    else:
        makeFile("NewSS","111222333111222333111222333444555666444555666444555666777888999777888999777888999")
    #print("\\".join(os.path.dirname(__file__).split("\\")[0:-1])+"\\tests")
    print("Done")