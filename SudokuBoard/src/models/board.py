#******************************************************************************
#  This is a model for the sodoku.py board state
#  Text explain model
#
#
#
#
#
#******************************************************************************
import box

class board:
    def __init__(self) -> None:
        self.boxList = list()
        self.solved = False

    def addByString(self, sudokuString):
        # sudokuList = sudokuString.split()
        sudokuList = [num for num in sudokuString]
        self.boxList.append(box(sudokuList))

    def addByBox(self, aBox):
        self.boxList.append(aBox)

    def __str__(self) -> str:
        completeList = list()
        i = -1
        for box in self.boxList:
            i +=1
            tempStr = str(box)
            tempList = [tempStr[index : index + 3] for index in range(0, len(tempStr), 3)]

            completeList[i] = tempList[0]
            completeList[i+3] = tempList[1]
            completeList[i+6] = tempList[2]

            if  i == 2:
                i = 9
            if i == 11:
                i = 18
            return "".join(completeList)