class UserInputError(Exception):
    pass

def validate_tag(tag) -> None:
    if len(tag.name) < 2:
        raise UserInputError("Tag must be at least 2 characters long")
    if len(tag.name) > 20:
        raise UserInputError("Tag must be less than 20 characters long")
