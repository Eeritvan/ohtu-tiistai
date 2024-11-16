import unittest
from util import validate_reference, UserInputError

class TestReferenceValidation(unittest.TestCase):
    # MISSING all form fields
    def setUp(self):
        pass

    def test_valid_length_does_not_raise_error(self):
        """All validated fields are filled and passed"""

        # Mandatory
        validate_set1 = {"author": "author",
                         "title":"juokse",
                         "booktitle": "juokse",
                         "year":"2020"}
        validate_reference(validate_set1)

        testfield = "a" * 100
        validate_set2 = {"author": testfield,
                         "title": testfield,
                         "booktitle": testfield,
                        "year":"2021"}
        validate_reference(validate_set2)

    def test_too_short_or_long_raises_error(self):
        """All validated fields are filled with too short or long strings"""
        with self.assertRaises(UserInputError):
            testfield3 = "ole"
            validate_set3 = {"author": testfield3,
                         "title": testfield3,
                         "booktitle": testfield3,
                        "year":"1991"}
            validate_reference(validate_set3)

        with self.assertRaises(UserInputError):
            testfield4 = "koodaa" * 20
            validate_set4 = {"author": testfield4,
                         "title": testfield4,
                         "booktitle": testfield4,
                        "year":"1991"}
            validate_reference(validate_set4)
