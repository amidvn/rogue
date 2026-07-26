import curses


class ResultsScreen:
    def __init__(self, stdscr, screen_manager):
        self.stdscr = stdscr
        self.screen_manager = screen_manager
        self.data = list()

    def render(self):
        self.stdscr.addstr(0, 0, "ТАБЛИЦА РЕКОРДОВ", curses.A_BOLD)
        col1_width = 30
        col2_width = 10
        col3_width = 10
        header = f"{'Дата':<{col1_width}} {'Ур.':<{col2_width}} {'Сокровищ':<{col3_width}}"
        self.stdscr.addstr(2, 0, header, curses.A_BOLD)
        self.stdscr.addstr(3, 0, "-" * (col1_width + col2_width + col3_width + 2))

        for row_idx, row in enumerate(sorted(self.data, key=lambda x: -x['treasures']), start=4):
            line = f"{row['date']:<{col1_width}} {row['levels']:<{col2_width}} {row['treasures']:<{col3_width}}"
            self.stdscr.addstr(row_idx, 0, line)

        self.stdscr.addstr(30, 5, "------------------");
        self.stdscr.addstr(31, 5, "Esc - вернуться назад");

    def handle_input(self, key: int) -> bool:
        if key == 27 or key == ord('\x1b'):
            self.screen_manager.switch_to("main_menu", {})
        return True
