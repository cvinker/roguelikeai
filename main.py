import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main() -> None:
    screen_width = 80
    screen_height = 50

    # track player position - start in center of screen
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )  # define font

    event_handler = EventHandler()  # Create instance of the EventHandler class

    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="Yet Another Roguelike Tutorial",
            vsync=True,
    ) as context:  # Create the screen
        root_console = tcod.Console(screen_width, screen_height, order="F")
        # This creates the console which is what is drawn to. Set to same dimensions,
        # as the new terminal, order argument changes access from [y, x] to [x, y]

        while True:  # Game Loop
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)  # apply update to display

            root_console.clear()  # prevent ghosting of moving player

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)  # send event to event_handler's dispatch method
                # which sends it to the proper place

                if action is None:  # no key pressed
                    continue
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()
