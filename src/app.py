from flask import redirect, render_template, request, jsonify, flash, Response
from db_helper import reset_db
from config import app, test_env
from services.reference_service import ReferenceService, get_all_tag_names
from services.validate_tag import validate_tag

ref_repo = ReferenceService()

@app.route("/")
def index():
    references = ref_repo.get_references()
    references_all = len(references)
    return render_template("index.html", references=references,
                                         unfinished=references_all)

@app.route("/new_reference", methods=["GET", "POST"])
def new():
    selected_type = None
    ref_types = [
        {"value": "inproceedings", "text": "Inproceeding"},
        {"value": "book", "text": "Book"},
        {"value": "article", "text": "Article"}
        ]
    tags = get_all_tag_names()

    if request.method == "POST":
        if 'select_type_submit' in request.form:
            # Handle when type is selected and submitted
            selected_type = request.form["select_type"]

        elif 'create_reference_submit' in request.form:
            selected_type = request.form["ref_type"]
            # Handle when reference data is submitted
            reference = ref_repo.create_ref_type_object(request.form)
            reference.add_tags(request.form.getlist("tags"))
            try:
                ref_repo.create_reference(reference)
                return redirect("/")

            except Exception as error:
                flash(str(error))
                return render_template("new_reference.html",
                            reference=reference, ref_types= ref_types,
                            ref_type=selected_type, tags=tags)
        else:
            print("Unknown form submission")

    return render_template("new_reference.html",
                            reference=None, ref_types= ref_types,
                            ref_type=selected_type, tags=tags)


## TEMPORARY DICTIONARY for testing and displaying different colors
TAGS = {'Red': "255, 0, 0",
        'Green': "0, 128, 0",
        'lue': '0, 0, 255',
        'Cyan': '0, 255, 255',
        'Magenta': '255, 0, 255',
        'Yellow': '255, 255, 0',
        'Orange': '255, 165, 0',
        'Purple': '128, 0, 128',
        'Lime': '0, 255, 0',
        'Teal': '0, 128, 128',
        'Navy': '0, 0, 128',
        'Maroon': '128, 0, 0',
        'Olive': '128, 128, 0',
        'Gray': '128, 128, 128',
        'Pink': '255, 192, 203',
        'Brown': '165, 42, 42',
        'Salmon': '250, 128, 114',
        'DarkGoldenRod': '184, 134, 11',
        'SlateBlue': '106, 90, 205',
        'DarkGreen': '0, 100, 0',
        }

@app.route("/manage_tags", methods=["GET", "POST"])
def manage_tags():
    if request.method == "POST":
        try:
            new_tag = request.form["name"]
            validate_tag(new_tag)
            # create a new tag here
            TAGS[new_tag] = '106, 90, 205' # here to test addition to the list
        except Exception as error:
            flash(str(error))

    # 'tags' is expecting a dictionary e.g. {'name': 'color', ...}
    return render_template("manage_tags.html", tags=TAGS) # tags=TAGS for colors

@app.route("/delete_tag", methods=["POST"])
def delete_tag():
    try:
        tag_name = request.form["tag_name"]
        ref_repo.delete_tag(tag_name)
        flash(f"Tag '{tag_name}' deleted successfully")
    except Exception as error:
        flash(str(error))
    return redirect("/manage_tags")

@app.route("/search_reference")
def search_reference():
    references = ref_repo.get_references()
    references_all = len(references)
    filters = {
        "author": request.args.get("author", ''),
        "title": request.args.get("title", ''),
        "type": request.args.get("ref_type", ''),
        "year": request.args.get("year", '')
    }

    if any(filters.values()):
        references = [
            ref for ref in references
            if filters["author"] in ref.author
            and filters["title"] in ref.title
            and filters["type"] in ref.ref_type
            and (filters["year"] == '' or str(filters["year"]) == str(ref.year))
        ]

    return render_template("filter_reference.html", references=references,
                                                    filters=filters,
                                                    total=references_all)

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
    if reference_id == "all":
        bibtex_entry = ref_repo.get_bibtex_entries_for_all()
    elif reference_id == "filtered":
        ids = request.args.get('reference_ids')
        reference_id=f"filtered:{ids}"
        bibtex_entry = ref_repo.get_bibtex_entries_for_filtered(ids)
    else:
        reference = ref_repo.get_references(reference_id)
        if not reference:
            flash("Reference not found")
            return redirect("/")
        bibtex_entry = ref_repo.get_reference_bibtex(reference)
    return render_template("bibtex.html", bibtex_entry=bibtex_entry,
                           reference_id=reference_id)

@app.route("/download_bibtex/<reference_id>", methods=["GET"])
def download_bibtex(reference_id):
    if reference_id == "all":
        bibtex_entry = ref_repo.get_bibtex_entries_for_all()
    elif "filtered" in reference_id:
        bibtex_entry = ref_repo.get_bibtex_entries_for_filtered(reference_id)
    else:
        reference = ref_repo.get_references(reference_id)
        if not reference:
            flash("Reference not found")
            return redirect("/")
        bibtex_entry = ref_repo.get_reference_bibtex(reference)

    response = Response(bibtex_entry, mimetype='text/plain')
    response.headers.set("Content-Disposition", "attachment",
                         filename="Reference.bib")
    return response

@app.route("/edit_reference/<reference_id>", methods=["GET", "POST"])
def edit_reference(reference_id):
    tags = get_all_tag_names()
    if request.method == "GET":
        reference = ref_repo.get_references(reference_id)
        if not reference:
            flash("Reference not found")
            return redirect("/")
        non_empty = reference.filter_non_empty()
        ref_tags = ref_repo.get_ref_tag_ids(reference_id)
        return render_template("edit_reference.html",
                            reference=non_empty, tags=tags, ref_tags=ref_tags)
    if request.method == "POST":
        reference = ref_repo.create_ref_type_object(request.form, reference_id)
        reference.delete_tags()
        reference.add_tags(request.form.getlist("tags"))
        if not reference:
            flash("Reference not found")
            return redirect("/")

        try:
            ref_repo.edit_reference(reference)
            flash(f"reference: '{reference.title}' edited successfully")
        except Exception as error:
            flash(str(error))
            return render_template(
                "/edit_reference.html",
                reference = reference,
                id = reference_id, tags=tags
            )
    return redirect("/")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
