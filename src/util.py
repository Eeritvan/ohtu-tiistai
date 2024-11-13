import re

class UserInputError(Exception):
    pass

def validate_reference(author, title, booktitle, year):
    if len(author) < 5:
        raise UserInputError("Reference author length must be greater than 4")

    if len(author) > 100:
          raise UserInputError("Reference author length must be smaller than 100")

    if len(title) < 5:
        raise UserInputError("Reference title length must be greater than 4")

    if len(title) > 100:
          raise UserInputError("Reference title length must be smaller than 100")

    if len(booktitle) < 5:
        raise UserInputError("Reference booktitle length must be greater than 4")

    if len(booktitle) > 100:
          raise UserInputError("Reference booktitle length must be smaller than 100")

    if re.search(r'\b(?:14\d{2}|15\d{2}|16\d{2}|17\d{2}|18\d{2}|19\d{2}|20\d{2})\b', year) == None:
          raise UserInputError("Reference year must be a four-digit number.")