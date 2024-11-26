from sqlalchemy import text
from config import db
from util import UserInputError
from entities.reference import Inproceedings

def inproceedings_helper(row):
    return Inproceedings(
        db_id=row[0],
        citekey=row[1],
        ref_type=row[2],
        author=row[3],
        title=row[4],
        year=row[5],
        booktitle=row[6],
        editor=row[7],
        volume=row[8],
        number=row[9],
        series=row[10],
        pages=row[11],
        address=row[12],
        month=row[13],
        organisation=row[14],
        publisher=row[15]
    )

def get_references(reference_id=None):
    query = '''
                SELECT
                id,
                citekey,
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
        '''
    if reference_id:
        query += ' WHERE id = :id'
        result = db.session.execute(text(query), {'id': reference_id})
        row = result.fetchone()
        if row:
            return inproceedings_helper(row)
        return None

    result = db.session.execute(text(query))
    rows = result.fetchall()
    return [inproceedings_helper(row) for row in rows]

def create_reference(references: dict):
    ref_type = "inproceedings"
    fields = {"type": ref_type}

    for key, content in references.items():
        if content:
            fields[key] = content

    try:
        columns = ', '.join(fields)
        placeholders = ', '.join(f":{key}" for key in fields)

        sql = text(f'''
                    INSERT INTO sources (
                    {columns}
                    )

                    VALUES (
                    {placeholders}
                   )
                    ''')
        db.session.execute(sql, fields)
        db.session.commit()
    except:
        return False
    return True

def delete_reference(reference_id: int):
    try:
        sql = text("DELETE FROM sources WHERE id = :id RETURNING title")
        result = db.session.execute(sql, {'id': reference_id})
        db.session.commit()
        return result.fetchone()[0]
    except Exception as e:
        raise UserInputError("deletion failed") from e


# def edit_reference_data(ref):


#     ref_type = "inproceedings"
#     print(ref)


#     sql = text('''

#                 UPDATE sources SET (citekey, type, author, title,
#                 year, booktitle, editor, volume, number,
#                 series, pages, address, month, organisation,
#                 publisher)
#                    = (
#                 :citekey, :type, :author, :title, :year, :booktitle,
#                 :editor, :volume, :number, :series, :pages, :address,
#                 :month, :organisation, :publisher)

#                 where id = :ref_id
#             ''')
#     db.session.execute(sql, {

#                 'citekey':ref.citekey,
#                 'type':ref_type,
#                 'author':ref.author,
#                 'title' :ref.title,
#                 'year' :ref.year,
#                 'booktitle' :ref.booktitle,
#                 'editor' :ref.editor,
#                 'volume' :ref.volume,
#                 'number' :ref.number,
#                 'series' :ref.series,
#                 'pages' :ref.pages,
#                 'address' :ref.address,
#                 'month' :ref.month,
#                 'organisation' :ref.organisation,
#                 'publisher' :ref.publisher,
#                 'ref_id':ref.id
#         })
#     db.session.commit()




