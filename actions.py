# When there is an action use one of the Action subclass to describe it
# EscapeAction for Esc (exit)
# MovementAction for player movement

class Action:
    pass


class EscapeAction(Action):
    pass


# pass dx dy arguments to MovementAction to describe where the player is trying to move to
class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy
