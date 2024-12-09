class UserInputError(Exception):
    pass

def validate_tag(tag: str) -> None:
    if len(tag) < 2:
        raise UserInputError("Tag must be at least 2 characters long")
    if len(tag) > 20:
        raise UserInputError("Tag must be less than 20 characters long")
