class UserInputError(Exception):
    pass

def validate_reference(title):
    if len(title) < 5:
        raise UserInputError("Reference title length must be greater than 4")

    if len(title) > 100:
          raise UserInputError("Reference title length must be smaller than 100")
