def format_inproceedings(reference):
    citekey = reference.citekey if reference.citekey else "None"
    bibtex_entry = f"@inproceedings{{{citekey},\n"
    for key, value in reference.field_values.items():
        if value is not None:
            bibtex_entry += f"    {key} = {{{value}}},\n"
    bibtex_entry = bibtex_entry.rstrip(",\n") + "\n}"
    return bibtex_entry
