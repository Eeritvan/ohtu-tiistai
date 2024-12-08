from sqlalchemy import text
from config import db, app

TABLE_NAMES = ["sources", "tags", "sources_tags"]

def table_exists(name):
    sql_table_existence = text(
        "SELECT EXISTS ("
        "  SELECT 1"
        "  FROM information_schema.tables"
        f" WHERE table_name = '{name}'"
        ")"
    )

    print(f"Checking if table {name} exists")
    print(sql_table_existence)

    result = db.session.execute(sql_table_existence)
    return result.fetchall()[0][0]

def reset_db():
    for TABLE_NAME in TABLE_NAMES:
        print(f"Clearing contents from table {TABLE_NAME}")
        sql = text(f"DELETE FROM {TABLE_NAME}")
        db.session.execute(sql)
        db.session.commit()

def setup_db():
    for TABLE_NAME in TABLE_NAMES:
        if table_exists(TABLE_NAME):
            print(f"Table {TABLE_NAME} exists, dropping")
            sql = text(f"DROP TABLE {TABLE_NAME} CASCADE")
            db.session.execute(sql)
            db.session.commit()

    print(f"Creating table {TABLE_NAMES[0]}")
    sql = text(
        f"CREATE TABLE {TABLE_NAMES[0]} ("
        "  id SERIAL PRIMARY KEY, "
        "  citekey VARCHAR(50) UNIQUE NOT NULL, "
        "  ref_type VARCHAR(50) NOT NULL, "
        "  author VARCHAR(255) NOT NULL, "
        "  title VARCHAR(255) UNIQUE NOT NULL, "
        "  year INT NOT NULL, "
        "  booktitle TEXT,"
        "  editor TEXT,"
        "  volume INTEGER,"
        "  number INTEGER,"
        "  series TEXT,"
        "  pages TEXT,"
        "  address TEXT,"
        "  month INTEGER,"
        "  organisation TEXT,"
        "  publisher TEXT,"
        "  journal TEXT,"
        "  note TEXT"
        ")"
    )

    db.session.execute(sql)
    db.session.commit()


    print(f"Creating table {TABLE_NAMES[1]}")
    sql = text(
        f"CREATE TABLE {TABLE_NAMES[1]} ("
        " id SERIAL PRIMARY KEY, "
        " tagname VARCHAR(20) UNIQUE, "
        " color VARCHAR(20)"
        ")"
    )
    db.session.execute(sql)
    db.session.commit()

    print(f"Creating table {TABLE_NAMES[2]}")
    sql = text(
        f"CREATE TABLE {TABLE_NAMES[2]} ("
        " id SERIAL PRIMARY KEY, "
        " source_id INTEGER REFERENCES sources ON DELETE CASCADE, "
        " tag_id INTEGER REFERENCES tags ON DELETE CASCADE"
        " )"
    )
    db.session.execute(sql)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
