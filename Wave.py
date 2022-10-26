

from itertools import count
import re
from socket import SCM_J1939_DEST_NAME
from sys import stdout
from turtle import st
from winreg import HKEY_LOCAL_MACHINE


class Wave:

    def __init__(self, monsters = []):
        '''Gets feed monsters and will keep track of monsters hp and the status of the wave, how many monster are alive. '''
        self.monsters = monsters
        self.xp = self.calXp()
        self.status = self.checkStatus()


    def calXp(self):
        '''Calculates the Xp totla of the monsters in the wave'''
        stdout = 0
        if (self.monsters):
            for monster in self.monsters:
                stdout = stdout + monster.xp
        return stdout

    def checkStatus(self):
        '''Checks the status of the wave, are all monsters dead'''
        dead = 0
        if (self.monsters):
            for monster in self.monsters:
                if (monster.hp <= 0):
                    dead = dead + 1
        return len(self.monsters) != dead

    def addMonster(self, monster):
        if (monster):
            self.monsters.append(monster)
            return 1
        return -1

    def getMonsterIds(self):
        '''Gets all ids of a monsters'''
        stdout = -1
        if (self.monsters):
            stdout = []
            for monster in self.monsters:
                stdout.append(monster.id)
        return stdout

    def findMonsterById(self, id):
        if(self.monsters):
            for monster in self.monsters:
                if (monster.id == id):
                    return monster
        return -1

    def DpToMonster(self, id, Dp):
        '''Deal damage point to monster with id'''
        if (Dp > 0):
            monster = self.findMonsterById(id)
            monster.dealDp(Dp) #could change ----
            return 1
        return -1


