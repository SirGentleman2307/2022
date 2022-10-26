

from pickle import TRUE


class monster:
    def __init__(self, name = "", ac = "", hp = "", speed = "", atb = [], saveThrow = "", actions = []) -> None:
        self.name = name
        self.ac = ac
        self.hp = hp
        self.speed = speed
        self.atb = atb
        self.saveThrow = saveThrow
        self.actions = actions

    def __str__(self) -> str:
        return str(self.name + self.ac + self.hp)

    def takeDamage(self, damage):
        self.hp = self.hp - damage
        # If monster dies return false, NOT ALIVE
        if self.hp < 0:
            return False
        return True