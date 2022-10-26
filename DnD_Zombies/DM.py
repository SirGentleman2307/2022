import os
from Monster import monster

class DM:
    def __init__(self) -> None:
        self.monsters = []

    def readTheMonsterManual(self):
        '''READS THE MONSTER MANUAL !!!
        all the text files in Monsters folder'''
        arr = os.listdir("Monsters")

        for Monster in arr:
            with open("Monsters/" + Monster) as f:
                lines = f.readlines()

                # Try to get all monster from the MONSTER MANUAL !!!
                try:
                    name = lines[0].strip().split(': ')[1]
                    ac = lines[1].strip().split(': ')[1]
                    hp = lines[2].strip().split(': ')[1]
                    speed = lines[3].strip().split(': ')[1]
                    atb = lines[5].strip().split(' ,')
                    st = lines[7].strip().split(': ')[1]
                    chan = lines[12].strip().split(': ')[1]

                    newMonster = monster(name, hp, ac, speed, atb, st, chan)
                    self.monsters.append(newMonster)
                except IndentationError:
                    continue
                except IndexError:
                    continue
            f.close()


Krissi = DM()
Krissi.readTheMonsterManual()
