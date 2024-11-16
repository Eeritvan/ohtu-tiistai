from sqlalchemy import text
from config import db

from entities.reference import Reference

def get_references():
    result = db.session.execute(text("SELECT id, type, author, title, year, details FROM sources"))
    references = result.fetchall()


    return [
        Reference(reference[0], reference[1], reference[2], reference[3],
                  reference[4], reference[5])
        for reference in references
    ]

# def set_done(reference_id):
#     sql = text("UPDATE todos SET done = TRUE WHERE id = :id")
#     db.session.execute(sql, { "id": reference_id })
#     db.session.commit()

def create_reference(author,title, year):
    joku = "inproceedings"
    sql = text("INSERT INTO sources (type, author, title, year) VALUES (:type, :author, :title, :year)")
    db.session.execute(sql, { "type":joku, "author": author, "title": title, "year":year })
    db.session.commit()
