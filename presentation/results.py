import curses


class ResultsScreen:
    def __init__(self, stdscr, screen_manager):
        self.stdscr = stdscr
        self.screen_manager = screen_manager
        self.data = list()

    def render(self):
        self.stdscr.addstr(0, 0, "ТАБЛИЦА РЕКОРДОВ", curses.A_BOLD)
        col1_width = 20
        col2_width = 10
        col3_width = 12
        header = f"{'Date':<{col1_width}} {'Treasure':<{col2_width}} {'Level':<{col2_width}} {'Enemies':<{col2_width}} {'Food':<{col2_width}} {'Elixirs':<{col2_width}} {'Scrolls':<{col2_width}} {'Attacks/hits':<{col3_width}} {'Tiles':<{col2_width}}"
        self.stdscr.addstr(2, 0, header, curses.A_BOLD)
        self.stdscr.addstr(3, 0, "-" * len(header))

        for row_idx, row in enumerate(sorted(self.data, key=lambda x: -x['treasures']), start=4):
            attacks_hits = f"{row['attacks']}/{row['hits']}"
            line = f"{row['date']:<{col1_width}} {row['treasures']:<{col2_width}} {row['levels']:<{col2_width}} {row['enemies']:<{col2_width}} {row['food']:<{col2_width}} {row['elixirs']:<{col2_width}} {row['scrolls']:<{col2_width}} {attacks_hits:<{col3_width}} {row['tiles']:<{col2_width}}"
            self.stdscr.addstr(row_idx, 0, line)
            if row_idx > 28:
                self.stdscr.addstr(row_idx + 1, 0, "...")
                break

        self.stdscr.addstr(30, 5, "------------------");
        self.stdscr.addstr(31, 5, "Esc - вернуться назад");

    def handle_input(self, key: int) -> bool:
        if key == 27 or key == ord('\x1b'):
            self.screen_manager.switch_to("main_menu", {})
        return True
