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

    def _inproceedings_helper(self, row):
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

    def db_get_references(self, reference_id=None):
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
                return self._inproceedings_helper(row)
            return None

        result = db.session.execute(text(query))
        rows = result.fetchall()
        return [self._inproceedings_helper(row) for row in rows]

    def db_create_reference(self, reference: Inproceedings):
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
            raise UserInputError(
                f"Title '{reference.title}' already exists"
            ) from e

    def db_edit_reference(self, reference):
        fields = reference.__dict__
        for key, value in fields.items():
            if value == '':
                fields[key] = None
        placeholders = ', '.join(f"{key} = :{key}" for key in fields)

        try:
            sql = text(f'''
                        UPDATE sources
                        SET {placeholders}
                        WHERE id =:id''')

            db.session.execute(sql, fields)
            db.session.commit()
        except Exception as e:
            raise UserInputError(
                f"Title '{reference.title}' already exists"
            ) from e

    def db_delete_reference(self,reference_id: int):
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

    def create_tag(self, color: str , tagname: str):
        """Creates a new tag."""
        try:
            sql = text('''INSERT INTO tags(tagname, color)
                    VALUES (:tagname, :color)
                    ''')
            db.session.execute(sql,{"tagname":tagname, "color":color})
            db.session.commit()
        except Exception as e:
            raise UserInputError(
                f"Tagname '{tagname}' already exists"
            ) from e

    def get_tags(self):
        """Get all tags in database.
        Returns: result-object"""

        sql = text('''Select id, tagname, color
                   FROM tags
                   ''')
        result = db.session.execute(sql)
        rows = result.fetchall()
        return rows

    def add_tag(self, reference_id : int, tag_id : int):
        """Add tag to a specific reference. Uses tag_id"""

        sql = text('''INSERT INTO sources_tags(source_id, tag_id)
                    VALUES (:source_id, :tag_id)
                    ''')
        db.session.execute(sql,{"source_id":reference_id, "tag_id":tag_id})
        db.session.commit()


    def get_ref_tags(self, reference_id):
        """Get all tags related to specific reference. """

        sql = text(
            '''
            SELECT DISTINCT tagname, color

            FROM sources_tags AS st
                LEFT JOIN tags
                ON st.tag_id = tags.id

            WHERE st.source_id = :source_id
            '''
        )
        result = db.session.execute(sql, {"source_id":reference_id})
        rows = result.fetchall()

        return rows

    def get_tag_id(self, tagname):
        """Get id for tag by name"""
        sql = text(
            '''
            SELECT id
            FROM tags
            WHERE tagname = :tagname
            '''
        )
        result = db.session.execute(sql, {"tagname":tagname})
        tag = result.fetchone()
        return tag.id

    def add_tagname(self, reference_id : int, tagname : str):
        """Add tag for specific reference. Uses tagname instead of id """

        tag_id = self.get_tag_id(tagname)
        sql = text('''INSERT INTO sources_tags(source_id, tag_id)
                    VALUES (:source_id, :tag_id)
                    ''')
        db.session.execute(sql,{"source_id":reference_id, "tag_id":tag_id})
        db.session.commit()

    def delete_tag(self, tagname : str):
        """Deletes existing tags from every table. """
        tag_id = self.get_tag_id(tagname)
        try:
            sql = text("DELETE FROM tags WHERE id = :id RETURNING tagname")
            result = db.session.execute(sql, {'id': tag_id})
            db.session.commit()
            return result.fetchone()[0]
        except Exception as e:
            raise UserInputError("deletion failed") from e







