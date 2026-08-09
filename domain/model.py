import random


ROOMS_IN_WIDTH = 3
ROOMS_IN_HEIGHT = 3
NUM_ROOMS = ROOMS_IN_WIDTH * ROOMS_IN_HEIGHT
REGION_WIDTH = 28
REGION_HEIGHT = 11
MIN_ROOM_WIDTH = 6
MAX_ROOM_WIDTH = REGION_WIDTH - 3
MIN_ROOM_HEIGHT = 5
MAX_ROOM_HEIGHT = REGION_HEIGHT - 3


class GameSession():
    def __init__(self):
        self.player = Character()
        self.current_level = 0
        self.backpack = list()


class Level():
    def __init__(self):
        self.level_num = 0  # порядковый номер уровня
        self.coords = []  # геометрия (размер) уровня
        self.rooms = []  # информация о комнатах
        for ind in range(NUM_ROOMS):
            self.rooms.append(Room())
        self.corridors = []  # информация о коридорах
        self.end_of_level_x = 0 # координаты выхода из уровня
        self.end_of_level_y = 0

    def generate_next_level(self):
        self.clear_data()
        self.level_num += 1
        self.generate_rooms()
        self.generate_corridors()
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
            width_room = random.randint(MIN_ROOM_WIDTH, MAX_ROOM_WIDTH)
            height_room = random.randint(MIN_ROOM_HEIGHT, MAX_ROOM_HEIGHT)
            self.rooms[ind].width_room = width_room
            self.rooms[ind].height_room = height_room

            left_range_coord = (ind % ROOMS_IN_WIDTH) * REGION_WIDTH + 1
            right_range_coord = (ind % ROOMS_IN_WIDTH + 1) * REGION_WIDTH - width_room - 1
            up_range_coord = (ind // ROOMS_IN_HEIGHT) * REGION_HEIGHT + 1
            botton_range_coord = (ind // ROOMS_IN_HEIGHT + 1) * REGION_HEIGHT - height_room - 1
            self.rooms[ind].x_coord = random.randint(left_range_coord, right_range_coord)
            self.rooms[ind].y_coord = random.randint(up_range_coord, botton_range_coord)

    def generate_corridors(self):
        edges = self.generate_shuffled_edges_for_rooms()
        sets = [{i} for i in range(NUM_ROOMS)]
        corridors = list()
        for (i, j) in edges:
            for ind, s in enumerate(sets):
                if i in s:
                    ind_i = ind
                if j in s:
                    ind_j = ind
            if ind_i == ind_j:
                continue
            corridors.append((i, j))
            sets[ind_i].update(sets[ind_j])
            sets.pop(ind_j)

        for i, j in corridors:
            room_1 = self.rooms[i]
            room_2 = self.rooms[j]
            if (j - i) == 1:  # horizontal passage
                first_x = room_1.x_coord + room_1.width_room - 1
                first_y = random.randint(room_1.y_coord + 1, room_1.y_coord + room_1.height_room - 2)
                second_x = room_2.x_coord
                second_y = random.randint(room_2.y_coord + 1, room_2.y_coord + room_2.height_room - 2)
                if first_y == second_y:
                    self.corridors.append(Corridor(first_x, first_y, second_x, second_y))
                else:
                    vertical = random.randint(first_x + 1, second_x - 1)
                    self.corridors.append(Corridor(first_x, first_y, vertical, first_y))
                    self.corridors.append(Corridor(vertical, min(first_y, second_y), vertical, max(first_y, second_y)))
                    self.corridors.append(Corridor(vertical, second_y, second_x, second_y))
            else:
                first_x = random.randint(room_1.x_coord + 1, room_1.x_coord + room_1.width_room - 2)
                first_y = room_1.y_coord + room_1.height_room - 1
                second_x = random.randint(room_2.x_coord + 1, room_2.x_coord + room_2.width_room - 2)
                second_y = room_2.y_coord
                if first_x == second_x:
                    self.corridors.append(Corridor(first_x, first_y, second_x, second_y))
                else:
                    horizont = random.randint(first_y + 1, second_y - 1)
                    self.corridors.append(Corridor(first_x, first_y, first_x, horizont))
                    self.corridors.append(Corridor(min(first_x, second_x), horizont, max(first_x, second_x), horizont))
                    self.corridors.append(Corridor(second_x, horizont, second_x, second_y))

    def generate_shuffled_edges_for_rooms(self) -> list:
        edges = list()
        for i in range(NUM_ROOMS):
            for j in range(i + 1, NUM_ROOMS):
                row1 = i // ROOMS_IN_HEIGHT
                col1 = i % ROOMS_IN_WIDTH
                row2 = j // ROOMS_IN_HEIGHT
                col2 = j % ROOMS_IN_WIDTH
                if row1 == row2 and col2 - col1 == 1:
                    edges.append((i, j))
                if col1 == col2 and row2 - row1 == 1:
                    edges.append((i, j))
        random.shuffle(edges)
        return edges

    def generate_player(self):
        pass

    def generate_monsters(self):
        pass

    def generate_consumables(self):
        pass

    def generate_exit(self):
        exit_room = random.randint(1, len(self.rooms) - 1)
        upper_left_x = self.rooms[exit_room].x_coord + 2
        upper_left_y = self.rooms[exit_room].y_coord + 2
        bottom_right_x = upper_left_x + self.rooms[exit_room].width_room - 5
        bottom_right_y = upper_left_y + self.rooms[exit_room].height_room - 5
        print(upper_left_x, bottom_right_x, upper_left_y, bottom_right_y)
        self.end_of_level_x= random.randint(upper_left_x, bottom_right_x)
        self.end_of_level_y = random.randint(upper_left_y, bottom_right_y)


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
    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y


class Character():
    def __init__(self):
        self.max_health = 100
        self.cur_health = 100
        self.dexterity = 10
        self.strength = 100
        self.current_weapon = None
        self.pos_x = 0
        self.pos_y = 0

    def place_in_center_of_room(self, room):
        self.pos_x = room.x_coord + room.width_room // 2
        self.pos_y = room.y_coord + room.height_room // 2

    def move(self, level, step_x, step_y):
        new_pos_x = self.pos_x + step_x
        new_pos_y = self.pos_y + step_y
        outside_border = True
        for room in level.rooms:
            if new_pos_x > room.x_coord and new_pos_x < room.x_coord + room.width_room - 1 and\
            new_pos_y > room.y_coord and new_pos_y < room.y_coord + room.height_room - 1:
                outside_border = False
                break
        for corridor in level.corridors:
            if new_pos_x >= corridor.start_x and new_pos_x <= corridor.end_x and new_pos_y >= corridor.start_y and new_pos_y <= corridor.end_y:
                outside_border = False
                break

        if not outside_border:
            self.pos_x += step_x
            self.pos_y += step_y

    def check_outside_border(self, new_pos_x, new_pos_y):
        pass

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
