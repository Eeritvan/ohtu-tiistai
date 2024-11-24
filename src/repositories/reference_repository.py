from sqlalchemy import text
from config import db
from util import UserInputError
from entities.reference import Inproceedings

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
    return [Inproceedings(
        db_id=ref[0],
        ref_type=ref[1],
        author=ref[2],
        title=ref[3],
        year=ref[4],
        booktitle=ref[5],
        editor=ref[6],
        volume=ref[7],
        number=ref[8],
        series=ref[9],
        pages=ref[10],
        address=ref[11],
        month=ref[12],
        organisation=ref[13],
        publisher=ref[14]
        ) for ref in references]

def get_reference_by_id(reference_id):
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
                WHERE id = :id
        '''), {'id': reference_id})
    ref = result.fetchone()
    if ref:
        return Inproceedings(
            db_id=ref[0],
            ref_type=ref[1],
            author=ref[2],
            title=ref[3],
            year=ref[4],
            booktitle=ref[5],
            editor=ref[6],
            volume=ref[7],
            number=ref[8],
            series=ref[9],
            pages=ref[10],
            address=ref[11],
            month=ref[12],
            organisation=ref[13],
            publisher=ref[14]
        )
    return None

# def set_done(reference_id):
#     sql = text("UPDATE todos SET done = TRUE WHERE id = :id")
#     db.session.execute(sql, { "id": reference_id })
#     db.session.commit()

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
