from entities.reference import Inproceedings
from repositories.reference_repository import ReferenceRepository
from services.validate_reference import validate_reference
from services.generate_citekey import generate_citekey

class ReferenceService:
    """Class responsible of the app logic"""

    def __init__(self):
        """Class constructor
        Args:
            reference_repository: RefrenceRepository-object
                which has its methods
        """
        self._reference_repository = ReferenceRepository()

    def create_reference(self, reference: Inproceedings) -> None:
        """Creates new Reference/Inproceedings object.
        Funcions:
            validate_reference: validates input fields
            generate_citekey: generates citekey and adds it to the set
            create_reference: calls repository to make database insert
        Returns:
            Inproceedings object
        """

        try:
            validate_reference(reference)
            reference.citekey = generate_citekey(reference)
            self._reference_repository.db_create_reference(reference)
        except Exception as e:
            #TODO: change this to usererror
            raise NameError(e) from e

    def edit_reference(self, reference):
        try:
            validate_reference(reference)
            reference.citekey = generate_citekey(reference)
            self._reference_repository.db_edit_reference(reference)
        except Exception as e:
            #TODO: change this to usererror
            raise NameError(e) from e

    def get_references(self, reference_id=None) -> list:
        return self._reference_repository.db_get_references(reference_id)

    def delete_reference(self,reference_id: int) -> str:
        return self._reference_repository.db_delete_reference(reference_id)
