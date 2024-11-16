import re

class UserInputError(Exception):
    pass

def validate_reference(validate_set):

    for key, content in validate_set.items():

        if key == "author" and "title" and "booktitle":
        # Mandatory: author, title, booktitle, year
            if len(content) < 3:
                raise UserInputError(
                    f"Reference {key} length must be greater than 3"
                )

            if len(content) > 255:
                raise UserInputError(
                    f"Reference {key} length must be smaller than 255"
                )
        elif(key == "editor" or "address" or "organisation" or "publisher"):
        # Optional: editor, address, organisation, publisher
        # More checking needed?
            if len(content)>0:
                print(">0")
                if len(content) < 3:
                    print("<3")
                    raise UserInputError(
                        f"Reference {key} length must be greater than 3"
                    )
            if len(content) > 255:
                raise UserInputError(
                    f"Reference {key} length must be smaller than 255"
                )
        else:
        # Optional: volume, number, series, pages
        # More checking needed
            if len(content) > 255:
                raise UserInputError(
                    f"Reference {key} length must be smaller than 255"
                )

        # Mandatory: year
        if key == "year":
            if re.search(
                r'\b(?:14\d{2}|15\d{2}|16\d{2}|17\d{2}|18\d{2}|19\d{2}|20\d{2})\b', content) is None:
                raise UserInputError("Reference year must be a four-digit number.")

