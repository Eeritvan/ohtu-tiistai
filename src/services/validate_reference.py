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

def validate_reference(reference): # pylint: disable=too-many-statements
    '''#TODO: paremmat tarkistukset tänne
    if reference.ref_type == "article":
        print(reference.mandatory_fields)
        print(reference.optional_fields)
        return
    if reference.ref_type == "book":
        print(reference.mandatory_fields)
        # doesnt have any optional_fields
        return

    mandatory_fields = ['author', 'title', 'booktitle']'''

    # New field retrieval for all reference types
    mandatory_fields = reference.mandatory_fields
    optional_fields = reference.optional_fields
    print(mandatory_fields)
    for field in mandatory_fields:
        value = getattr(reference, field)
        print(field, value)
        if len(value) < 1:
            raise UserInputError(
                f"Reference {field} length must be greater than 1"
            )
        if len(value) > 255:
            raise UserInputError(
                f"Reference {field} length must be smaller than 255"
            )


    validate_year(int(reference.year))
    if 'month' in optional_fields:
        validate_month(reference.month)

    # optional_fields = ["editor",
    #                   "address",
    #                   "organisation",
    #                   "publisher",
    #                   "series"]
    if len(optional_fields) > 0:
        for field in optional_fields:
            value = getattr(reference, field)
            if value and len(value) < 1:
                raise UserInputError(
                    f"Reference {field} length must be greater than 1"
                )
            if value and len(value) > 255:
                raise UserInputError(
                    f"Reference {field} length must be smaller than 255"
                )

    if hasattr(reference, 'pages') and reference.pages and len(reference.pages) > 255:
        raise UserInputError(
            "Reference pages length must be smaller than 255"
        )

    if hasattr(reference, 'volume') and reference.volume and int(reference.volume) < 0:
        raise UserInputError(
            "Reference volume length must be positive integer"
        )

    if hasattr(reference, 'number') and reference.number and int(reference.number) < 0:
        raise UserInputError(
            "Reference number length must be positive integer"
        )
