from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.reference_repository import (
    get_references,
    create_reference
 #   set_done
)
from config import app, test_env
from util import validate_reference

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
    # This variable list is uneccessary if create_reference() is changed
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

    #Adding all input in a dict for sending it to validation
    validate_set = {}
    validate_set["author"] = request.form.get("author")
    validate_set["title"] = request.form.get("title")
    validate_set["booktitle"] = request.form.get("booktitle")
    validate_set["year"] = request.form.get("year")
    validate_set["editor"] = request.form.get("editor")
    validate_set["volume"] = request.form.get("volume")
    validate_set["number"] = request.form.get("number")
    validate_set["series"] = request.form.get("series")
    validate_set["pages"] = request.form.get("pages")
    validate_set["address"] = request.form.get("address")
    validate_set["month"] = request.form.get("month")
    validate_set["organisation"] = request.form.get("organisation")
    validate_set["publisher"] = request.form.get("publisher")

    try:
        validate_reference(validate_set)
    #Change this also to validate_set and remove variable list above?
        create_reference(author,title, year)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_reference")

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
