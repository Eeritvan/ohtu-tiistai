class Tag: # pylint: disable=redefined-builtin
    def __init__(self, name, id = None, color=None):
        self.id = id
        self.name = name
        self.color = color

    def __str__(self):
        return (
            f"id: {self.id}\n"
            f"name: {self.name}\n"
            f"color: {self.color}\n"
        )
