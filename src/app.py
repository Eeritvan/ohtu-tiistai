from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.reference_repository import ReferenceRepository
from config import app, test_env
from services.reference_service import ReferenceService


@app.route("/")
def index():
    #PAJA: miten saisi defaultina, ettei tarvi toistaa
    ref = ReferenceRepository()
    references = ref.get_references()
    references_all = len(references)
    return render_template("index.html", references=references,
                                         unfinished=references_all)

@app.route("/new_reference")
def new():
    return render_template("new_reference.html")

@app.route("/create_reference", methods=["POST"])
def reference_creation():
    validate_set = dict(request.form.items())

    try:
        #PAJA: miten saisi defaultina, ettei tarvi toistaa
        refserv = ReferenceService()
        if not refserv.create_reference(validate_set):
            #TODO puuttuu
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
    reference = get_references(reference_id)
    if not reference:
        flash("Reference not found")
        return redirect("/")

    bibtex_entry = format_inproceedings(reference)
    return render_template("bibtex.html", bibtex_entry=bibtex_entry)

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
