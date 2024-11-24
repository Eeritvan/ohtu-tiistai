from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.reference_repository import (
    get_references,
    create_reference,
    delete_reference,
    get_reference_by_id
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
        if not create_reference(validate_set):
            raise_error("The title already exists.")
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/new_reference")

@app.route("/delete_reference/<reference_id>", methods=["POST"])
def del_reference(reference_id):
    try:
        deleted_title = delete_reference(reference_id)
        flash(f"reference: '{deleted_title}' deleted successfully")
    except Exception as error:
        flash(str(error))
    return redirect("/")

@app.route("/export_bibtex/<reference_id>", methods=["GET"])
def export_bibtex(reference_id):
    reference = get_reference_by_id(reference_id)
    if not reference:
        flash("Reference not found")
        return redirect("/")

    bibtex_entry = f"@inproceedings{{{reference.id},\n"
    for key, value in reference.field_values.items():
        if value is not None:
            bibtex_entry += f"    {key} = {{{value}}},\n"
    bibtex_entry = bibtex_entry.rstrip(",\n") + "\n}"

    return render_template("bibtex.html", bibtex_entry=bibtex_entry)

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
