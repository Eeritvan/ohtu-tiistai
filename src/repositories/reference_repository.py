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
    return False
