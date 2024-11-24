from datetime import datetime
import re

class UserInputError(Exception):
    pass

def validate_year(year: int):
    current_year = datetime.now().year
    if year < 0 or year > current_year:
        raise UserInputError(
            "Reference year must be a four-digit positive integer."
        )

#TODO validate month
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

def filter_title_words(title):
    stopwords = {
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
        'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was',
        'were', 'will', 'with'
    }

    words = title.split()
    lista = []
    for word in words:
        if word.lower() not in stopwords:
            lista.append(word.capitalize())
    return lista[:3]

def clean_text(text):
    return re.sub(r'[^a-zA-Z ]', '', text).strip()

def generate_citekey(i):
    cleaned_author = clean_text(i["author"])
    cleaned_title = clean_text(i["title"])
    year = i["year"]

    author_last_name = cleaned_author.split()[-1][:15].capitalize()
    filtered_title = filter_title_words(cleaned_title)
    title_part = "".join(filtered_title)[:15]

    return f"{author_last_name}{year}{title_part}"

def raise_error(message):
    raise UserInputError(message)
