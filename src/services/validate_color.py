class UserInputError(Exception):
    pass

def validate_color(color: str) -> None:
    if len(color) < 2:
        raise UserInputError("Tag must be at least 2 characters long")
    if len(color) > 20:
        raise UserInputError("Tag must be less than 20 characters long")
