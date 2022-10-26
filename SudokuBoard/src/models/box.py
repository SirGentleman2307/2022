#******************************************************************************
#  This is a model for the sodoku.py
#  Text explain model
#
#
#
# Change 1,2,3,4,5,6,7,8,9 too 123,456,789
#
#******************************************************************************

class box: 
    def __init__(self, numbers = list()) -> None:
        self.valid = False
        self.numbers = numbers

    def editNumbers(self, newNumbers):
        self.numbers = newNumbers
        self.numberCountValidor()

    def numberCountValidor(self):
        self.valid = False

        test = list()
        for number in self.numbers:
            if number == 0:
                self.valid = False
                return
            test[number -1] = number

        if test == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.valid = True
        return

    def __str__(self) -> str:
        return "".join(self.numbers)