import curses
from .menu import MenuScreen
from .level import LevelScreen
from .results import ResultsScreen


class ScreenManager:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.menu_manager = None
        self.data = {}
        self.screens = {
            "main_menu": MenuScreen(self.stdscr, self),
            "level": LevelScreen(self.stdscr, self),
            "results": ResultsScreen(self.stdscr, self)
        }
        self.current_screen = "main_menu"

        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    def render(self):
        if not self.current_screen:
            return

        screen = self.screens.get(self.current_screen)
        if screen:
            self.stdscr.clear()
            screen.render()
            self.stdscr.refresh()

    def switch_to(self, name, data):
        self.current_screen = name

    def handle_input(self, key) -> bool:
        screen = self.screens.get(self.current_screen)
        if screen:
            return screen.handle_input(key)

        return True
