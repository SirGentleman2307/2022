from re import S


class Game:

    def __init__(self, players = 0):
        self.players = players
        self.monsterInfo = self.readMM()
        self.waves = self.makeWaves()
        self.status = self.checkStatus()
        self.currentWaveId = 1

    def readMM(self):
        pass

    def makeWaves(self):
        pass

    def checkStatus(self):
        pass

    def dealDpToMonster(self, Dp, Id):
        if (Dp > 0):
            self.waves[self.currentWaveId - 1].dealDpToMonster(Dp, Id)
            return 1
        return -1

