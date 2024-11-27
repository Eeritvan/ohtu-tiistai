from entities.reference import Inproceedings
from repositories.reference_repository import ReferenceRepository

# Siirretty util.pystä
from services.validate_reference import validate_reference
from services.generate_citekey import generate_citekey


class UsernameExistsError(Exception):
    pass

class ReferenceService:
    """Class responsible of the app logic"""

    def __init__(self):
        """Class constructor
        Args:
            reference_repository: RefrenceRepository-object
                which has its methods
        """
        self._reference_repository = ReferenceRepository()

    #PAJA: onko dict oikea tapa tuoda tänne tiedot?
    def create_reference(self, validate_set:dict):
        """Creates new Reference/Inproceedings object.
        Funcions:
            validate_reference: validates input fields
            generate_citekey: generates citekey and adds it to the set
            create_reference: calls repository to make database insert
        Returns:
            Inproceedings object
        """

        #TODO Lisättävä tähän raise error?
        validate_reference(validate_set)
        validate_set["citekey"] = generate_citekey(validate_set)

        result = self._reference_repository.create_reference(
            Inproceedings(**validate_set))

        return result

    #TODO
    def get_references(self, reference_id=None):
        """Pyytää tekemään selectin tietokantaan"""
        # return list of Inproceedings?

    #TODO
    def delete_reference(self,reference_id: int):
        """Pyytää poiston tietokannasta ja saa titlen palautuksena"""
