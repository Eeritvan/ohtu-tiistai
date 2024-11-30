def format_inproceedings(reference):
    citekey = reference.citekey
    bibtex_entry = f"@inproceedings{{{citekey},\n"
    for key, value in reference.filter_bibtex_fields().items():
        if value is not None:
            bibtex_entry += f"    {key} = {{{value}}},\n"
    bibtex_entry = bibtex_entry.rstrip(",\n") + "\n}"
    return bibtex_entry
