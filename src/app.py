from flask import redirect, render_template, request, jsonify, flash, Response
from db_helper import reset_db
from entities.reference import Inproceedings
from config import app, test_env
from services.reference_service import ReferenceService
from services.format_inproceedings import format_inproceedings
from entities.reference import Inproceedings

ref_repo = ReferenceService()

@app.route("/")
def index():
    references = ref_repo.get_references()
    references_all = len(references)
    return render_template("index.html", references=references,
                                         unfinished=references_all)

@app.route("/new_reference", methods=["GET", "POST"])
def new(reference=None):
    if request.method == "POST":
        reference = Inproceedings(**request.form)
        try:
            ref_repo.create_reference(reference)
            return redirect("/")
        except Exception as error:
            flash(str(error))
    return render_template("new_reference.html", reference=reference)

@app.route("/delete_reference/<reference_id>", methods=["POST"])
def del_reference(reference_id):
    try:
        deleted_title = ref_repo.delete_reference(reference_id)
        flash(f"reference: '{deleted_title}' deleted successfully")
    except Exception as error:
        flash(str(error))
    return redirect("/")

@app.route("/export_bibtex/<reference_id>", methods=["GET"])
def export_bibtex(reference_id):
    reference = ref_repo.get_references(reference_id)
    if not reference:
        flash("Reference not found")
        return redirect("/")

    bibtex_entry = format_inproceedings(reference)
    return render_template("bibtex.html", bibtex_entry=bibtex_entry,
                           reference_id=reference_id)

@app.route("/download_bibtex/<reference_id>", methods=["GET"])
def download_bibtex(reference_id):
    reference = ref_repo.get_references(reference_id)
    if not reference:
        flash("Reference not found")
        return redirect("/")

    bibtex_entry = format_inproceedings(reference)
    response = Response(bibtex_entry, mimetype='text/plain')
    response.headers.set("Content-Disposition", "attachment",
                         filename="Reference.bib")
    return response

@app.route("/edit_reference/<reference_id>", methods=["GET", "POST"])
def edit_reference(reference_id):
    if request.method == "GET":
        reference = ref_repo.get_references(reference_id)
        if not reference:
            flash("Reference not found")
            return redirect("/")
        non_empty = reference.filter_non_empty()
        return render_template("edit_reference.html", reference=non_empty)
    # POST / SUBMITTING EDITS LEADS HERE
    if request.method == "POST":
        reference = Inproceedings(db_id = reference_id,
                                  **request.form)
        if not reference:
            flash("Reference not found")
            return redirect("/")


        try:
            ref_repo.edit_reference(reference)
            flash(f"reference: '{reference.title}' edited successfully")
            return redirect("/")
        except Exception as error:
            flash(str(error))
            return render_template(
                "/edit_reference.html",
                reference = reference,
                id = reference_id
            )

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
