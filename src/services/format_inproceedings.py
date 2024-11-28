def format_inproceedings(reference):
    citekey = reference.citekey
    bibtex_entry = f"@inproceedings{{{citekey},\n"
    for key, value in reference.__dict__.items():
        if value is not None:
            bibtex_entry += f"    {key} = {{{value}}},\n"
    bibtex_entry = bibtex_entry.rstrip(",\n") + "\n}"
    return bibtex_entry
