import curses


class LevelScreen:
    def __init__(self, stdscr, screen_manager):
        self.stdscr = stdscr
        self.screen_manager = screen_manager
        self.game_session = None
        self.level = None

    def render(self):
        for room in self.level.rooms:
            for x in range(room.x_coord, room.x_coord + room.width_room):
                for y in range(room.y_coord, room.y_coord + room.height_room):
                    symb = "."
                    if x == room.x_coord or x == room.x_coord + room.width_room - 1 or y == room.y_coord or y == room.y_coord + room.height_room - 1:
                        symb = "#"
                    self.stdscr.addstr(y, x, symb, curses.color_pair(1))

    def handle_input(self, key: int) -> bool:
        if key == ord('q') or key == ord('Q'):
            return False
        return True
