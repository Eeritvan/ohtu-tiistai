from datetime import datetime

class UserInputError(Exception):
    pass

def validate_year(year: int):
    current_year = datetime.now().year
    if year < 0 or year > current_year:
        raise UserInputError(
            "Reference year must be a four-digit positive integer."
        )

def validate_month(month):
    if month and (int(month) < 1 or int(month) > 12):
        raise UserInputError(
            "Reference month must be a number between 1 and 12"
        )

# TODO: volume
# TODO: number
# TODO: pages
def validate_reference(reference):
    mandatory_fields = ['author', 'title', 'booktitle']
    for field in mandatory_fields:
        value = getattr(reference, field)
        if len(value) < 3:
            raise UserInputError(
                f"Reference {field} length must be greater than 3"
            )
        if len(value) > 255:
            raise UserInputError(
                f"Reference {field} length must be smaller than 255"
            )

    validate_year(int(reference.year))
    validate_month(reference.month)

    optional_fields = ["editor", "address", "organisation", "publisher", "series"]
    for field in optional_fields:
        value = getattr(reference, field)
        if value and len(value) < 3:
            raise UserInputError(
                f"Reference {field} length must be greater than 3"
            )
        if value and len(value) > 255:
            raise UserInputError(
                f"Reference {field} length must be smaller than 255"
            )
