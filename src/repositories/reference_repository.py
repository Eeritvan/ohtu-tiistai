from sqlalchemy import text
from config import db
from entities.reference import Inproceedings

# Tarkista mikä on tälle oikeampi paikka
class UserInputError(Exception):
    pass

class ReferenceRepository:
    """Class responsible of database operations."""

    def __init__(self):
        """Class constructor"""

    #TODO: Jotenkin ettei tarvitse luetella kaikkia kenttiä
    def inproceedings_helper(self, row):
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

    #TODO: Muuta toimimaan ilman helpperiä?
    def get_references(self, reference_id=None):
        """Selects one or all references from the database.
        Returns:
            list"""
        query = '''
                    SELECT
                    id,
                    citekey,
                    ref_type,
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
                return self.inproceedings_helper(row)
            return None

        result = db.session.execute(text(query))
        rows = result.fetchall()
        return [self.inproceedings_helper(row) for row in rows]

    def create_reference(self, reference: Inproceedings):
        """Inserts reference to the database and 
            updates database id to the object.
            Returns:
                Reference object with db_id
        """
        fields = reference.filter_non_empty()

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
                        RETURNING id''')
            db.session.execute(sql, fields)
            db.session.commit()
        except Exception as e:
            raise UserInputError(f"Title '{reference.title}' already exists") from e

    def delete_reference(self,reference_id: int):
        """Deletes reference from database. 
        Returns:
          title of deleted content."""
        try:
            sql = text("DELETE FROM sources WHERE id = :id RETURNING title")
            result = db.session.execute(sql, {'id': reference_id})
            db.session.commit()
            return result.fetchone()[0]
        except Exception as e:
            raise UserInputError("deletion failed") from e
