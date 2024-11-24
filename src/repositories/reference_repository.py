from sqlalchemy import text
from config import db
from util import UserInputError
from entities.reference import Inproceedings

def get_references():
    result = db.session.execute(text(
        '''
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

        '''))
    references = result.fetchall()
    return [Inproceedings(
        db_id=ref[0],
        citekey=ref[1],
        ref_type=ref[2],
        author=ref[3],
        title=ref[4],
        year=ref[5],
        booktitle=ref[6],
        editor=ref[7],
        volume=ref[8],
        number=ref[9],
        series=ref[10],
        pages=ref[11],
        address=ref[12],
        month=ref[13],
        organisation=ref[14],
        publisher=ref[15]
        ) for ref in references]

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
