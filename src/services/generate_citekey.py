import re

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

def generate_citekey(reference):

    cleaned_author = clean_text(reference.author)
    cleaned_title = clean_text(reference.title)
    year = reference.year

    author_last_name = cleaned_author.split()[-1][:15].capitalize()
    filtered_title = filter_title_words(cleaned_title)
    title_part = "".join(filtered_title)[:15]

    return f"{author_last_name}{year}{title_part}"
