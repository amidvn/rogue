import curses


class MenuScreen:
    def __init__(self, stdscr, screen_manager):
        self.stdscr = stdscr
        self.screen_manager = screen_manager
        self.header = "ROGUE"
        self.bottom = "Made by @amidvn"
        self.menu_options = [
            ("Новая игра", self.action_new_game),
            ("Загрузить игру", self.action_load_game),
            ("Таблица результатов", self.action_results),
            ("Выход", self.action_exit)
        ]
        self.current_row = 0

    def render(self):
        self.stdscr.addstr("\n    " + self.header + "\n\n", curses.color_pair(1) | curses.A_BOLD)

        for idx, (label, _) in enumerate(self.menu_options):
            x = 2
            y = idx + 3
            if idx == self.current_row:
                self.stdscr.addstr(y, x, f"> {label}", curses.color_pair(2))
            else:
                self.stdscr.addstr(y, x, f"  {label}", curses.color_pair(1))

        self.stdscr.addstr("\n\n\n    " + self.bottom + "\n\n", curses.color_pair(1) | curses.A_BOLD)

    def handle_input(self, key: int) -> bool:
        if key == curses.KEY_UP:
            self.current_row = max(0, self.current_row - 1)
        elif key == curses.KEY_DOWN:
            self.current_row = min(len(self.menu_options) - 1, self.current_row + 1)
        elif key == ord("\n"):
            should_exit = self.menu_options[self.current_row][1]()
            if should_exit:
                return False
        return True

    def action_new_game(self):
        self.screen_manager.switch_to("level", {})
        return False

    def action_load_game(self):
        self.screen_manager.switch_to("load_game", {})
        return False

    def action_results(self):
        self.screen_manager.switch_to("results", {})
        return False

    def action_exit(self):
        return True
