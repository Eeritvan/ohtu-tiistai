from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.reference_repository import (
    get_references,
    create_reference
)
from config import app, test_env
from util import validate_reference, raise_error

@app.route("/")
def index():
    references = get_references()
    references_all = len(references)
    return render_template("index.html", references=references,
                                         unfinished=references_all)

@app.route("/new_reference")
def new():
    return render_template("new_reference.html")

@app.route("/create_reference", methods=["POST"])
def reference_creation():
    fields = [
        "author", "title", "booktitle", "year", "editor",
        "volume", "number", "series", "pages", "address",
        "month", "organisation", "publisher"
    ]
    validate_set = {field: request.form.get(field) for field in fields}

    try:
        validate_reference(validate_set)
        if create_reference(validate_set):
            raise_error("The title already exists.")
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/new_reference")

# @app.route("/toggle_reference/<reference_id>", methods=["POST"])
# def toggle_reference(reference_id):
#     set_done(reference_id)
#     return redirect("/")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
