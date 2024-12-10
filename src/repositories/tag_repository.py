from sqlalchemy import text
from config import db
from entities.tag import Tag

class UserInputError(Exception):
    pass

class TagRepository:
    def db_get_latest_tag(self):
        sql = text('SELECT id FROM tags ORDER BY id DESC LIMIT 1')
        result = db.session.execute(sql).fetchone()
        if result == None:
            return 0
        return result[0]

    def db_create_tag(self, tag):
        """Creates a new tag."""
        try:
            sql = text('''INSERT INTO tags(tagname, color)
                    VALUES (:tagname, :color)
                    ''')
            db.session.execute(sql,{"tagname":tag.name, "color":tag.color})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise UserInputError(f"Tagname '{tag.name}' already exists") from e

    def db_get_tags(self):
        """Get all tags in database.
        Returns: result-object"""
        try:
            sql = text('''Select id, tagname, color
                    FROM tags
                    ''')
            result = db.session.execute(sql)
            rows = result.fetchall()
            tag_names = [Tag(row[1], row[0], row[2]) for row in rows]
            return tag_names
        except Exception as e:
            raise UserInputError("Fetching tag name failed") from e

    def db_get_tag_id(self, tagname: str):
        """Get id for tag by name"""
        sql = text(
            '''
            SELECT id
            FROM tags
            WHERE tagname = :tagname
            '''
        )
        result = db.session.execute(sql, {"tagname": tagname})
        tag = result.fetchone()
        return tag.id

    def db_delete_tag(self, tagname : str):
        """Deletes existing tags from every table. """
        tag_id = self.db_get_tag_id(tagname)
        try:
            sql = text("DELETE FROM tags WHERE id = :id RETURNING tagname")
            result = db.session.execute(sql, {'id': tag_id})
            db.session.commit()
            return result.fetchone()[0]
        except Exception as e:
            raise UserInputError("deletion failed") from e
