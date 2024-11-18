import unittest
from util import validate_reference, UserInputError

class TestReferenceValidation(unittest.TestCase):
    # MISSING all form fields
    def setUp(self):
        pass

    def test_mandatory_valid_length_does_not_raise_error(self):
        """All validated fields are filled and passed"""

        validate_set1 = {"author": "author",
                         "title":"juokse",
                         "booktitle": "juokse",
                         "year":"2020"}
        validate_reference(validate_set1)

        testfield2 = "a" * 100
        validate_set2 = {"author": testfield2,
                         "title": testfield2,
                         "booktitle": testfield2,
                         "year":"2021"}
        validate_reference(validate_set2)

    def test_mandatory_too_short_or_long_raises_error(self):
        """All validated fields are filled with too short or long strings"""

        with self.assertRaises(UserInputError):
            testfield1 = "ab"
            validate_set1 = {"author": testfield1,
                             "title": testfield1,
                             "booktitle": testfield1,
                             "year":"1991"}
            validate_reference(validate_set1)

        with self.assertRaises(UserInputError):
            testfield2 = "koodaa" * 100
            validate_set2 = {"author": testfield2,
                             "title": testfield2,
                             "booktitle": testfield2,
                             "year":"1991"}
            validate_reference(validate_set2)

    def test_invalid_year(self):
        """Year is negative or in the future"""

        with self.assertRaises(UserInputError):
            testfield1 = "test"
            validate_set1 = {"author": testfield1,
                             "title": testfield1,
                             "booktitle": testfield1,
                             "year":"-10"}
            validate_reference(validate_set1)

        with self.assertRaises(UserInputError):
            testfield2 = "test"
            validate_set2 = {"author": testfield2,
                             "title": testfield2,
                             "booktitle": testfield2,
                             "year":"10000"}
            validate_reference(validate_set2)

    def test_invalid_year(self):
        """Year is negative or in the future"""

        with self.assertRaises(UserInputError):
            testfield1 = "test"
            validate_set1 = {"author": testfield1,
                             "title": testfield1,
                             "booktitle": testfield1,
                             "year":"-10"}
            validate_reference(validate_set1)

        with self.assertRaises(UserInputError):
            testfield2 = "test"
            validate_set2 = {"author": testfield2,
                             "title": testfield2,
                             "booktitle": testfield2,
                             "year":"10000"}
            validate_reference(validate_set2)

    def test_valid_optional_fields(self):
        """Tests are filled with valid inputs"""

        testfield1 = "test"
        validate_set1 = {"author": testfield1,
                         "title": testfield1,
                         "booktitle": testfield1,
                         "year":"2000",
                         "address":testfield1,
                         "series":testfield1}
        validate_reference(validate_set1)

    def test_valid_optional_fields(self):
        """Tests are filled with valid inputs"""

        testfield1 = "test"
        validate_set1 = {"author": testfield1,
                         "title": testfield1,
                         "booktitle": testfield1,
                         "year":"2000",
                         "address":testfield1,
                         "series":testfield1}
        validate_reference(validate_set1)

    def test_invalid_optional_fields(self):
        """Tests are filled with valid inputs"""

        with self.assertRaises(UserInputError):
            testfield1 = "test" * 200
            validate_set1 = {"author": "testtest",
                            "title": "testtest",
                            "booktitle": "testtest",
                            "year":"2000",
                            "address":"testtest",
                            "series":testfield1}
            validate_reference(validate_set1)

        with self.assertRaises(UserInputError):
            testfield2 = "test" * 200
            validate_set2 = {"author": "testtest",
                            "title": "testtest",
                            "booktitle": "testtest",
                            "year":"2000",
                            "address":testfield2,
                            "series":"testtest"}
            validate_reference(validate_set2)

        with self.assertRaises(UserInputError):
            testfield3 = "ab"
            validate_set3 = {"author": "testtest",
                            "title": "testtest",
                            "booktitle": "testtest",
                            "year":"2000",
                            "address":testfield3,
                            "series":"testtest"}
            validate_reference(validate_set3)