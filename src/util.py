import re

class UserInputError(Exception):
    pass

#TODO this needs to be fixed, so input is less params and more flexible for other reference types
def validate_reference(author, title, booktitle, year, editor):
    #volume, number, series, pages, address, month, organisation, publisher

    fields_validation_length = {"author": author, "title": title, "book title": booktitle}

    if len(editor)>0:
        fields_validation_length["editor"] = editor

    # if len(volume)>0:
    #     fields_validation_length["volume"] = volume
    # if len(number)>0:
    #     fields_validation_length["number"] = number
    # if len(series)>0:
    #     fields_validation_length["series"] = series
    # if len(pages)>0:
    #     fields_validation_length["pages"] = pages
    # if len(address)>0:
    #     fields_validation_length["address"] = address
    # if len(month)>0:
    #     fields_validation_length["month"] =  month
    # if len(organisation)>0:
    #     fields_validation_length["organisation"] =  organisation
    # if len(publisher)>0:
    #     fields_validation_length["publisher"] =  publisher

    for key, content in fields_validation_length.items():

        if len(content) < 5:
            raise UserInputError(f"Reference {key} length must be greater than 4")

        if len(content) > 100:
            raise UserInputError(f"Reference {key} length must be smaller than 100")

    if re.search(r'\b(?:14\d{2}|15\d{2}|16\d{2}|17\d{2}|18\d{2}|19\d{2}|20\d{2})\b', year) is None:
          raise UserInputError("Reference year must be a four-digit number.")

