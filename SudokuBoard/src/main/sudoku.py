#******************************************************************************
#  This is the main program that runs the sudoku game
#  Text explain
#
#
#
#
#
#******************************************************************************
import os
testPath = "\\".join(os.path.dirname(__file__).split("\\")[0:-1]) + "\\tests\\"

class sudokuGame:
    def __init__(self, filePath) -> None:
        self.boardString = self.loadBoard(filePath)

    def run(self):
        pass

    def loadBoard(self, filePath):
        try:
            with open(filePath,"r",encoding="utf8") as f:
                rawString = ""
                for line in f:
                    rawLine = line.strip().split("│")
                    if len(rawLine) == 3:
                        rawString += rawLine + ","
        except:
            print("No file found named %s" % filePath)

        completeList = ["" for n in range(0,27,1)]
        i = -1
        for line in rawString.split(",")[0:-1]:
            i +=1
            tempList = [line[index : index + 3] for index in range(0, len(line), 3)]
            completeList[i] += tempList[i]
            completeList[i+3] += tempList[i]
            completeList[i+6] += tempList[i]
            if  i == 2:
                i = 9
            if i == 11:
                i = 18
        completeString = ",".join(completeList)
        self.boardString = completeString

    def __str__(self) -> str:
        return self.boardString


if __name__ == '__main__':
    if input() == "1":
        fileName = input("Enter in file name: ")
        filePath = testPath + fileName + ".txt"
        Game = sudokuGame(filePath)
        print(Game)
    print("Done")

