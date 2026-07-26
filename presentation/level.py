import curses


class LevelScreen:
    def __init__(self, stdscr, screen_manager):
        self.stdscr = stdscr
        self.screen_manager = screen_manager
        self.game_session = None

    def render(self):
        self.stdscr.addstr("\n    LEVEL SCREEN" + "\n\n", curses.color_pair(1) | curses.A_BOLD)

    def handle_input(self, key: int) -> bool:
        if key == ord('q') or key == ord('Q'):
            return False
        return True
