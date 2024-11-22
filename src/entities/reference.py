class Reference:
#   Kun kannassa on citekey, vaihda käyttöön versiot,
#   joista se on nyt kommentoitu pois!
#    def __init__(self, db_id, ref_type, citekey):
    def __init__(self, db_id, ref_type):
        self.id = db_id
        self.ref_type = ref_type
#        self.citekey = citekey

    def __str__(self):
        return (
            f"id: {self.id}\n"
            f"type: {self.ref_type}\n"
#            f"citekey: {self.citekey}\n"
        )

class Inproceedings(Reference):
#    def __init__(self, db_id, ref_type, citekey, **kwargs):
    def __init__(self, db_id, ref_type, **kwargs,):
        super().__init__(db_id, ref_type)
#        super().__init__(db_id, ref_type, citekey)
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

    def fields_not_none(self):
        field_values_filtered = {k: v for k, v in self.field_values.items()
                                 if v is not None}
        return field_values_filtered

    def __str__(self):
        return (
            f"id: {self.id}\n"
#            f"citekey: {self.citekey}\n"
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
