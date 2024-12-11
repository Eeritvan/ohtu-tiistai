from repositories.tag_repository import TagRepository
from services.validate_tag import validate_tag
from services.generate_color import generate_color

class UserInputError(Exception):
    pass

class TagService():
    def __init__(self):
        self._tag_repository = TagRepository()

    def get_all_tag_names(self):
        return self._tag_repository.db_get_tags()

    def create_new_tag(self, tag):
        try:
            validate_tag(tag)
            latest_id = self._tag_repository.db_get_latest_tag()
            tag.color = generate_color(latest_id)
            self._tag_repository.db_create_tag(tag)
        except Exception as e:
            raise UserInputError(e) from e

    def delete_tag(self, tag_name):
        try:
            self._tag_repository.db_delete_tag(tag_name)
        except Exception as e:
            raise UserInputError(e) from e
