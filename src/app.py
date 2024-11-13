from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.reference_repository import get_references, create_reference, set_done
from config import app, test_env
from util import validate_reference

@app.route("/")
def index():
    references = get_references()
    references_all = len([reference for reference in references])
    return render_template("index.html", references=references, unfinished=references_all)

@app.route("/new_reference")
def new():
    return render_template("new_reference.html")

@app.route("/create_reference", methods=["POST"])
def reference_creation():
    author = request.form.get("author")
    title = request.form.get("title")
    booktitle = request.form.get("booktitle")
    year = request.form.get("year")

    editor = request.form.get("editor")
    volume = request.form.get("volume")
    number = request.form.get("number")
    series = request.form.get("series")
    pages = request.form.get("pages")
    address = request.form.get("address")
    month = request.form.get("month")
    organisation = request.form.get("organisation")
    publisher = request.form.get("publisher")

    try:
        #TODO this needs to be done better, so function does get less parameters
        validate_reference(author, title, booktitle, year, editor, volume, number, series, pages, address, month, organisation, publisher)
        create_reference(title)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_reference")

@app.route("/toggle_reference/<reference_id>", methods=["POST"])
def toggle_reference(reference_id):
    set_done(reference_id)
    return redirect("/")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
