from sqlalchemy import text
from config import db
from entities.reference import Inproceedings, Book, Article

class UserInputError(Exception):
    pass

class ReferenceRepository:
    """Class responsible of database operations."""

    def __init__(self):
        """Class constructor"""

    def _helper(self, row):
        match (row[2]):
            case 'article':
                return Article(
                    db_id=row[0],
                    citekey=row[1],
                    ref_type=row[2],
                    author=row[3],
                    title=row[4],
                    year=row[5],
                    volume=row[8],
                    number=row[9],
                    pages=row[11],
                    month=row[13],
                    journal=row[16],
                    note=row[17]
                )
            case 'book':
                return Book(
                    db_id=row[0],
                    citekey=row[1],
                    ref_type=row[2],
                    author=row[3],
                    title=row[4],
                    year=row[5],
                    address=row[12],
                    publisher=row[15]
                )
            case _:
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
                    publisher,
                    journal,
                    note
                    FROM sources
            '''
        if reference_id:
            query += ' WHERE id = :id'
            result = db.session.execute(text(query), {'id': reference_id})
            row = result.fetchone()
            if row:
                return self._helper(row)
            return None

        result = db.session.execute(text(query))
        rows = result.fetchall()
        return [self._helper(row) for row in rows]

    def db_create_reference(self, reference):
        """Inserts reference and tags to the database and
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
            
            result = db.session.execute(sql, fields)
            source_id = result.fetchone()[0]
            db.session.commit()

            for tag_id in reference.tags:
                self.db_add_tag(source_id, tag_id)

        except Exception as e:
            db.session.rollback()
            raise UserInputError(
                f"Title '{reference.title}' already exists"
            ) from e

    def db_edit_reference(self, reference):
        old_fields = reference.__dict__
        excluded_keys = ['mandatory_fields', 'optional_fields', 'tags']
        fields = {
            key: (value if value != '' else None)
            for key, value in old_fields.items()
            if key not in excluded_keys
        }

        placeholders = ', '.join(f"{key} = :{key}" for key in fields)

        try:
            sql = text(f'''
                        UPDATE sources
                        SET {placeholders}
                        WHERE id =:id''')

            db.session.execute(sql, fields)
            db.session.commit()

            source_id = reference.id
            self.db_delete_refe_tags(source_id)
            for tag_id in reference.tags:
                self.db_add_tag(source_id, tag_id)

        except Exception as e:
            db.session.rollback()
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
            db.session.rollback()
            raise UserInputError("deletion failed") from e

    def db_get_ref_tags(self, reference_id):
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

    def db_get_ref_tag_ids(self, reference_id):
        """Get all tags related to specific reference. """

        sql = text(
            '''
            SELECT DISTINCT tag_id
            FROM sources_tags
            WHERE source_id = :source_id
            '''
        )
        result = db.session.execute(sql, {"source_id":reference_id})
        rows = result.fetchall()
        tag_ids = [row[0] for row in rows]
        return tag_ids

    def db_add_tag(self, reference_id : int, tag_id : int):
        """Add tag to a specific reference. Uses tag_id"""

        sql = text('''INSERT INTO sources_tags(source_id, tag_id)
                    VALUES (:source_id, :tag_id)
                    ''')
        db.session.execute(sql,{"source_id":reference_id, "tag_id":tag_id})
        db.session.commit()

    def db_add_tagname(self, reference_id : int, tagname : str):
        """Add tag for specific reference. Uses tagname instead of id """

        tag_id = self.get_tag_id(tagname)
        sql = text('''INSERT INTO sources_tags(source_id, tag_id)
                    VALUES (:source_id, :tag_id)
                    ''')
        db.session.execute(sql,{"source_id":reference_id, "tag_id":tag_id})
        db.session.commit()

    def db_delete_refe_tags(self, reference_id : int):
        """Deletes tags linked to reference. """
        try:
            sql = text("DELETE FROM sources_tags WHERE source_id = :id")
            db.session.execute(sql, {'id': reference_id})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise UserInputError("deletion of tags in reference failed") from e
