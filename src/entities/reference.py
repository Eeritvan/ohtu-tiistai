class Reference:
    # def __init__(self, ref_id, title, done):
    #     self.id = ref_id
    #     self.title = title
    #     self.done = done

    def __init__(self, ref_id, ref_type, author,title, year, details):
        self.id = ref_id
        self.type = ref_type
        self.author = author
        self.title = title
        self.year = year
        self.details = details

        # missing from database, but in html-form: booktitle, editor


    def __str__(self):
        #is_done = "done" if self.done else "not done"
        return f"{self.title}"
