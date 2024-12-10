class Reference:
    """Parent class for all reference types.
    Stores basic values which are common to all types.
        """

    def __init__(self, ref_type, db_id=None, citekey=None):
        """Constructor which creates new Reference object"""
        self.id = db_id
        self.ref_type = ref_type
        self.citekey = citekey
        self.tags = []

    def add_tags(self, tags):
        self.tags = tags

    def delete_tags(self):
        self.tags.clear()

    def __str__(self):
        """Creates a string which contains attribute values."""
        return (
            f"id: {self.id}\n"
            f"type: {self.ref_type}\n"
            f"citekey: {self.citekey}\n"
        )

class Inproceedings(Reference):
    def __init__(self, **kwargs): # pylint: disable=too-many-statements
        super().__init__(
            kwargs.get('ref_type'),
            kwargs.get('db_id', None),
            kwargs.get('citekey', None)
            )
        self.author = kwargs.get('author', None)
        self.title = kwargs.get('title', None)
        self.year = kwargs.get('year', None)
        self.booktitle = kwargs.get('booktitle', None)
        self.editor = kwargs.get('editor', None)
        self.volume = kwargs.get('volume', None)
        self.number = kwargs.get('number', None)
        self.series = kwargs.get('series', None)
        self.pages = kwargs.get('pages', None)
        self.address = kwargs.get('address', None)
        self.month = kwargs.get('month', None)
        self.organisation = kwargs.get('organisation', None)
        self.publisher = kwargs.get('publisher', None)
        self.mandatory_fields = ["author", "title", "booktitle", "year"]
        self.optional_fields = ["editor",
                                "volume",
                                "number",
                                "series",
                                "pages",
                                "address",
                                "month",
                                "organisation",
                                "publisher"]

    def filter_non_empty(self) -> dict:
        reference_dict = self.__dict__
        filtered_reference = {}

        for key, value in reference_dict.items():
            excluded_keys = ['mandatory_fields',
                          'optional_fields', 'tags']
            if key not in excluded_keys:
                if value not in ("", None):
                    filtered_reference[key] = value

        return filtered_reference

    def filter_bibtex_fields(self) -> dict:
        reference_dict = self.__dict__
        filtered_reference = {}

        for key, value in reference_dict.items():
            excluded_keys = ['ref_type',
                          'id',
                          'citekey',
                          'mandatory_fields',
                          'optional_fields', 'tags']
            if key not in excluded_keys:
                if value not in ("", None):
                    filtered_reference[key] = value

        return filtered_reference

    def __str__(self):
        return (
            f"id: {self.id}\n"
            f"citekey: {self.citekey}\n"
            f"type: {self.ref_type}\n"
            f"author: {self.author}\n"
            f"title: {self.title}\n"
            f"year: {self.year}\n"
            f"booktitle: {self.booktitle}\n"
            f"editor: {self.editor}\n"
            f"volume: {self.volume}\n"
            f"number: {self.number}\n"
            f"series: {self.series}\n"
            f"pages: {self.pages}\n"
            f"address: {self.address}\n"
            f"month: {self.month}\n"
            f"organisation: {self.organisation}\n"
            f"publisher: {self.publisher}"
            )

class Article(Reference):
    def __init__(self, **kwargs):
        super().__init__(
            kwargs.get('ref_type'),
            kwargs.get('db_id', None),
            kwargs.get('citekey', None)
            )
        self.author = kwargs.get('author', None)
        self.title = kwargs.get('title', None)
        self.year = kwargs.get('year', None)
        self.journal = kwargs.get('journal', None)
        self.volume = kwargs.get('volume', None)
        self.number = kwargs.get('number', None)
        self.pages = kwargs.get('pages', None)
        self.month = kwargs.get('month', None)
        self.note = kwargs.get('note', None)
        self.mandatory_fields = ["author", "title", "journal", "year"]
        self.optional_fields = ["volume", "number", "pages", "month", "note"]

    def filter_non_empty(self) -> dict:
        reference_dict = self.__dict__
        filtered_reference = {}

        for key, value in reference_dict.items():
            excluded_keys = ['mandatory_fields',
              'optional_fields', 'tags']
            if key not in excluded_keys:
                if value not in ("", None):
                    filtered_reference[key] = value

        return filtered_reference

    def filter_bibtex_fields(self) -> dict:
        reference_dict = self.__dict__
        filtered_reference = {}

        for key, value in reference_dict.items():
            excluded_keys = ['ref_type',
                          'id',
                          'citekey',
                          'mandatory_fields',
                          'optional_fields', 'tags']
            if key not in excluded_keys:
                if value not in ("", None):
                    filtered_reference[key] = value

        return filtered_reference

    def __str__(self):
        return (
            f"id: {self.id}\n"
            f"citekey: {self.citekey}\n"
            f"type: {self.ref_type}\n"
            f"author: {self.author}\n"
            f"title: {self.title}\n"
            f"year: {self.year}\n"
            f"journal: {self.journal}\n"
            f"volume: {self.volume}\n"
            f"number: {self.number}\n"
            f"pages: {self.pages}\n"
            f"month: {self.month}\n"
            f"note: {self.note}"
            )



class Book(Reference):
    def __init__(self, **kwargs):
        super().__init__(
            kwargs.get('ref_type'),
            kwargs.get('db_id', None),
            kwargs.get('citekey', None)
            )
        self.author = kwargs.get('author', None)
        self.title = kwargs.get('title', None)
        self.year = kwargs.get('year', None)
        self.publisher = kwargs.get('publisher', None)
        self.address = kwargs.get('address', None)
        self.mandatory_fields = ["author","year","title","publisher","address"]
        self.optional_fields = []

    def filter_non_empty(self) -> dict:
        reference_dict = self.__dict__
        filtered_reference = {}

        for key, value in reference_dict.items():
            excluded_keys = ['mandatory_fields', 'optional_fields', 'tags']
            if key not in excluded_keys:
                if value not in ("", None):
                    filtered_reference[key] = value

        return filtered_reference

    def filter_bibtex_fields(self) -> dict:
        reference_dict = self.__dict__
        filtered_reference = {}

        for key, value in reference_dict.items():
            excluded_keys = ['ref_type',
                          'id',
                          'citekey',
                          'mandatory_fields',
                          'optional_fields', 'tags']
            if key not in excluded_keys:
                if value not in ("", None):
                    filtered_reference[key] = value

        return filtered_reference

    def __str__(self):
        return (
            f"id: {self.id}\n"
            f"citekey: {self.citekey}\n"
            f"type: {self.ref_type}\n"
            f"author: {self.author}\n"
            f"title: {self.title}\n"
            f"year: {self.year}\n"
            f"publisher: {self.publisher}\n"
            f"address: {self.address}"
            )
