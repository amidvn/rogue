import curses

from domain import GameSession
from presentation import ScreenManager


def main(stdscr):
    height, width = stdscr.getmaxyx()
    if height < 31 or width < 150:
        stdscr.addstr(0, 0, "Недостаточно размера на терминале\nНажмите любую клавишу для выхода")
        key = stdscr.getch()
        return

    screen_manager = ScreenManager(stdscr)

    current_screen = ""

    while True:
        if screen_manager.current_screen != current_screen:
            if screen_manager.current_screen == "level":
                screen_manager.screens["level"].game_session = GameSession()
            elif screen_manager.current_screen == "load_game":  # TODO - load game from json
                screen_manager.screens["level"].game_session = GameSession()
                screen_manager.current_screen = "level"
            elif screen_manager.current_screen == "results":
                screen_manager.screens["results"].data = [
                    {'date': '2026-07-26 15:40', 'levels': 5, 'treasures': 12, 'enemies': 26, 'food': 19, 'elixirs': 7, 'scrolls': 6, 'attacks': 52, 'hits': 36, 'tiles': 47},
                    {'date': '2026-07-26 14:00', 'levels': 6, 'treasures': 14, 'enemies': 26, 'food': 19, 'elixirs': 7, 'scrolls': 6, 'attacks': 52, 'hits': 36, 'tiles': 47},
                    {'date': '2026-07-26 12:00', 'levels': 3, 'treasures': 7, 'enemies': 26, 'food': 19, 'elixirs': 7, 'scrolls': 6, 'attacks': 52, 'hits': 36, 'tiles': 47}
                ]

            screen_manager.switch_to(screen_manager.current_screen, {})

            current_screen = screen_manager.current_screen

        screen_manager.render()
        key = stdscr.getch()
        should_continue = screen_manager.handle_input(key)
        if not should_continue:
            break


if __name__ == "__main__":
    curses.wrapper(main)
