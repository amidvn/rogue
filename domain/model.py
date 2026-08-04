from random import randint


class GameSession():
    pass


ROOMS_IN_WIDTH = 3
ROOMS_IN_HEIGHT = 3
NUM_ROOMS = ROOMS_IN_WIDTH * ROOMS_IN_HEIGHT
REGION_WIDTH = 27
REGION_HEIGHT = 10
MIN_ROOM_WIDTH = 6
MAX_ROOM_WIDTH = REGION_WIDTH - 2
MIN_ROOM_HEIGHT = 5
MAX_ROOM_HEIGHT = REGION_HEIGHT - 2

class Level():
    def __init__(self):
        self.level_num = 0  # порядковый номер уровня
        self.coords = []  # геометрия (размер) уровня
        self.rooms = []  # информация о комнатах
        for ind in range(NUM_ROOMS):
            self.rooms.append(Room())
        self.passages = {}  # информация о коридорах
        self.end_of_level = []  # координаты выхода из уровня

    def generate_next_level(self):
        self.clear_data()
        self.level_num += 1
        self.generate_rooms()
        self.generate_passages()
        player_room = self.generate_player()
        self.generate_monsters()
        self.generate_consumables()
        self.generate_exit()

    def clear_data(self):
        for ind in range(NUM_ROOMS):
            self.rooms[ind].monster_num = 0
            self.rooms[ind].food_num = 0
            self.rooms[ind].weapon_num = 0
            self.rooms[ind].elixir_num = 0
            self.rooms[ind].scroll_num = 0

    def generate_rooms(self):
        for ind in range(NUM_ROOMS):
            width_room = randint(MIN_ROOM_WIDTH, MAX_ROOM_WIDTH)
            height_room = randint(MIN_ROOM_HEIGHT, MAX_ROOM_HEIGHT)
            left_range_coord = (ind % ROOMS_IN_WIDTH) * REGION_WIDTH + 1
            right_range_coord = (ind % ROOMS_IN_WIDTH + 1) * REGION_WIDTH - width_room + 1
            self.rooms[ind].x_coord = randint(left_range_coord, right_range_coord)
            up_range_coord = (ind // ROOMS_IN_HEIGHT) * REGION_HEIGHT + 1
            botton_range_coord = (ind // ROOMS_IN_HEIGHT + 1) * REGION_HEIGHT - height_room + 1
            self.rooms[ind].width_room = width_room
            self.rooms[ind].height_room = height_room
            self.rooms[ind].x_coord = randint(left_range_coord, right_range_coord)
            self.rooms[ind].y_coord = randint(up_range_coord, botton_range_coord)

    def generate_passages(self):
        pass

    def generate_player(self):
        pass

    def generate_monsters(self):
        pass

    def generate_consumables(self):
        pass

    def generate_exit(self):
        pass



class Room():
    def __init__(self):
        self.width_room = 0
        self.height_room = 0
        self.x_coord = 0
        self.y_coord = 0
        self.monster_num = 0
        self.food_num = 0
        self.weapon_num = 0
        self.elixir_num = 0
        self.scroll_num = 0
        self.monsters = []
        self.coords = []
        self.consumables = []


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
