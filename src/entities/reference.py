class Reference:
    def __init__(self, id, title, done):
        self.id = id
        self.title = title
        self.done = done

    def __str__(self):
        #is_done = "done" if self.done else "not done"
        return f"{self.title}"
