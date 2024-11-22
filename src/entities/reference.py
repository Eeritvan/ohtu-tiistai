class Reference:
    def __init__(self, db_id, ref_type, author, title, year):
        self.id = db_id
        self.type = ref_type
        self.author = author
        self.title = title
        self.year = year

    def __str__(self):
        return (
            f"id: {self.id}\n"
            f"type: {self.type}\n"
            f"author: {self.author}\n"
            f"title: {self.title}\n"
            f"year: {self.year}"
        )

class Inproceedings(Reference):
    def __init__(self, db_id, ref_type, author, title, year, **kwargs):
        super().__init__(db_id, ref_type, author, title, year)
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

    def __str__(self):
        return (
            f"id: {self.id}\n"
            f"type: {self.type}\n"
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
