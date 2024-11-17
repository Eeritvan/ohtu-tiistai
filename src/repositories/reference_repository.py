from sqlalchemy import text
from config import db

from entities.reference import Reference


def get_references():
    result = db.session.execute(text(
        '''
                SELECT
                id,
                type,
                author,
                title,
                year,
                booktitle,
                editor,
                volume,
                number,
                series,
                pages,
                address,
                month,
                organisation,
                publisher

                FROM sources

        '''))
    references = result.fetchall()

    return references

# def set_done(reference_id):
#     sql = text("UPDATE todos SET done = TRUE WHERE id = :id")
#     db.session.execute(sql, { "id": reference_id })
#     db.session.commit()

def create_reference(references: dict):
    ref_type = "inproceedings"

    try:
        sql = text('''
                    INSERT INTO sources (
                    type,
                    author,
                    title,
                    year,
                    booktitle,
                    editor,
                    volume,
                    number,
                    series,
                    pages,
                    address,
                    month,
                    organisation,
                    publisher)

                    VALUES (
                    :type,
                    :author,
                    :title,
                    :year,
                    :booktitle,
                    :editor,
                    :volume,
                    :number,
                    :series,
                    :pages,
                    :address,
                    :month,
                    :organisation,
                    :publisher)

                    ''')
        db.session.execute(sql, {
                "type" : ref_type,
                "author" : references['author'],
                "title" : references['title'],
                "year" : references['year'],
                "booktitle" : references['booktitle'],
                "editor" : references['editor'],
                "volume" : references['volume'],
                "number" : references['number'],
                "series" : references['series'],
                "pages" : references['pages'],
                "address" : references['address'],
                "month" : references['month'],
                "organisation" : references['organisation'],
                "publisher": references['publisher']
                })
        db.session.commit()
    except:
        return False
    return True


