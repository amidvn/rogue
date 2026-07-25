class GameSession():
    pass


class Level():
    pass


class Room():
    pass


class Corridor():
    pass


class Character():
    def __init__(self):
        self.max_health = 100
        self.cur_health = 100
        self.dexterity = 10
        self.strength = 100
        self.cur_weapon = None


class Backpack():
    pass


class Enemy():
    def __init__(self):
        self.type = None
        self.cur_health = 100
        self.dexterity = 10
        self.strength = 100
        self.hostility = 100


class Item():
    def __init__(self):
        self.type = None
        self.subtype = None
        self.health = 0
        self.max_health = 0
        self.dexterity = 0
        self.strength = 0
        self.value = 0
