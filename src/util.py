from datetime import datetime

class UserInputError(Exception):
    pass

def validate_year(year: int):
    current_year = datetime.now().year
    if year < 0 or year > current_year:
        raise UserInputError(
            "Reference year must be a four-digit positive integer."
        )

def validate_reference(validate_set):
    for key, content in validate_set.items():
        if key in ["author", "title", "booktitle"]:
            if len(content) < 3:
                raise UserInputError(
                    f"Reference {key} length must be greater than 3"
                )

            if len(content) > 255:
                raise UserInputError(
                    f"Reference {key} length must be smaller than 255"
                )

        elif key == "year":
            validate_year(int(content))

        elif key in ["editor", "address", "organisation", "publisher"]:
            if content and len(content) < 3:
                raise UserInputError(
                    f"Reference {key} length must be greater than 3"
                )
            if len(content) > 255:
                raise UserInputError(
                    f"Reference {key} length must be smaller than 255"
                )

        else: # volume, number, series, pages
            if content and len(content) > 255:
                raise UserInputError(
                    f"Reference {key} length must be smaller than 255"
                )

def raise_error(message):
    raise UserInputError(message)
