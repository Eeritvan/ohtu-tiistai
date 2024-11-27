class Reference:
    """Parent class for all reference types. 
    Stores basic values which are common to all types. 
        """

    def __init__(self, ref_type, db_id=None, citekey=None):
        """Constructor which creates new Reference object"""
        self.id = db_id
        self.ref_type = ref_type
        self.citekey = citekey

    def update_id(self, db_id):
        """Updates the value of database id"""
        self.id = db_id

    def __str__(self):
        """Creates a string which contains attribute values."""
        return (
            f"id: {self.id}\n"
            f"type: {self.ref_type}\n"
            f"citekey: {self.citekey}\n"
        )


class Inproceedings(Reference):
    """Class for Inproceedings reference type"""

    def __init__(self, **kwargs):
        """Constructor"""
        super().__init__(kwargs.get('ref_type', None),
            kwargs.get('db_id', None), kwargs.get('citekey', None))

        self.field_values = {
            "author": kwargs.get('author', None),
            "title": kwargs.get('title', None),
            "year": kwargs.get('year', None),
            "booktitle": kwargs.get('booktitle', None),
            "editor": kwargs.get('editor', None),
            "volume": kwargs.get('volume', None),
            "number": kwargs.get('number', None),
            "series": kwargs.get('series', None),
            "pages": kwargs.get('pages', None),
            "address": kwargs.get('address', None),
            "month": kwargs.get('month', None),
            "organisation": kwargs.get('organisation', None),
            "publisher": kwargs.get('publisher', None)
        }
        self.mandatory_fields = ["author", "title", "booktitle", "year"]

    def __str__(self):
        return (
            f"id: {self.id}\n"
            f"citekey: {self.citekey}\n"
            f"type: {self.ref_type}\n"
            f"author: {self.field_values['author']}\n"
            f"title: {self.field_values['title']}\n"
            f"year: {self.field_values['year']}\n"
            f"booktitle: {self.field_values['booktitle']}\n"
            f"editor: {self.field_values['editor']}\n"
            f"volume: {self.field_values['volume']}\n"
            f"number: {self.field_values['number']}\n"
            f"series: {self.field_values['series']}\n"
            f"pages: {self.field_values['pages']}\n"
            f"address: {self.field_values['address']}\n"
            f"month: {self.field_values['month']}\n"
            f"organisation: {self.field_values['organisation']}\n"
            f"publisher: {self.field_values['publisher']}"
            )

    def __getattr__(self, field):
        return self.field_values[field]
