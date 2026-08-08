import curses


class LevelScreen:
    def __init__(self, stdscr, screen_manager):
        self.stdscr = stdscr
        self.screen_manager = screen_manager
        self.game_session = None
        self.level = None

    def render(self):
        for room in self.level.rooms:
            x_coord = room.x_coord
            width_room = room.width_room
            y_coord = room.y_coord
            height_room = room.height_room
            for x in range(x_coord, x_coord + width_room):
                for y in range(y_coord, y_coord + height_room):
                    symb = "."
                    if x == x_coord or x == (x_coord + width_room - 1) or y == y_coord or y == (y_coord + height_room - 1):
                        symb = "#"
                    self.stdscr.addstr(y, x, symb, curses.color_pair(1))

        for corridor in self.level.corridors:
            start_x = corridor.start_x
            start_y = corridor.start_y
            end_x = corridor.end_x
            end_y = corridor.end_y
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    self.stdscr.addstr(y, x, ".", curses.color_pair(1))

        player_pos_x = self.game_session.player.pos_x
        player_pos_y = self.game_session.player.pos_y
        self.stdscr.addstr(player_pos_y, player_pos_x, "@", curses.color_pair(1))

    def handle_input(self, key: int) -> bool:
        if key == ord('q') or key == ord('Q'):
            return False
        elif key == ord('w') or key == ord('W'):
            self.game_session.player.move(self.level, 0, -1)
        elif key == ord('s') or key == ord('S'):
            self.game_session.player.move(self.level, 0, 1)
        elif key == ord('a') or key == ord('A'):
            self.game_session.player.move(self.level, -1, 0)
        elif key == ord('d') or key == ord('D'):
            self.game_session.player.move(self.level, 1, 0)
        return True
