import unittest
from services.validate_reference import validate_reference, UserInputError
from entities.reference import Inproceedings, Article

class TestReferenceValidation(unittest.TestCase):
    # MISSING all form fields
    def setUp(self):
        pass

    def test_mandatory_valid_length_does_not_raise_error(self):
        """All validated fields are filled and passed"""

        validate_set1 = Inproceedings(
            author = "author",
            title = "juokse",
            booktitle = "juokse",
            year = 2020
        )

        validate_reference(validate_set1)

        testfield2 = "a" * 100
        validate_set2 = Inproceedings(
            author = testfield2,
            title = testfield2,
            booktitle = testfield2,
            year = 2021
        )
        validate_reference(validate_set2)

    def test_mandatory_too_short_or_long_raises_error(self):
        """All validated fields are filled with too short or long strings"""

        with self.assertRaises(UserInputError):
            testfield1 = ""
            validate_set1 = Inproceedings(
                author = testfield1,
                title = testfield1,
                booktitle = testfield1,
                year = 1991
            )
            validate_reference(validate_set1)

        with self.assertRaises(UserInputError):
            testfield2 = "koodaa" * 100
            validate_set2 = Inproceedings(
                author = testfield2,
                title = testfield2,
                booktitle = testfield2,
                year = 1991
            )
            validate_reference(validate_set2)

    def test_invalid_year(self):
        """Year is negative or in the future"""

        with self.assertRaises(UserInputError):
            testfield1 = "test"
            validate_set1 = Inproceedings(
                author = testfield1,
                title = testfield1,
                booktitle = testfield1,
                year = -10
            )
            validate_reference(validate_set1)

        with self.assertRaises(UserInputError):
            testfield2 = "test"
            validate_set2 = Inproceedings(
                author = testfield2,
                title = testfield2,
                booktitle = testfield2,
                year = 10000
            )
            validate_reference(validate_set2)

    def test_valid_optional_fields(self):
        """Tests are filled with valid data"""

        testfield1 = "test"
        validate_set1 = Inproceedings(
            author = testfield1,
            title = testfield1,
            booktitle = testfield1,
            year = 2000,
            address = testfield1,
            series = testfield1
        )
        validate_reference(validate_set1)

    def test_invalid_page_data(self):
        """Page field is filled with invalid number"""

        with self.assertRaises(UserInputError):
            testfield1 = "test" * 200
            validate_set1 = Inproceedings(
                author = "testtest",
                title = "testtest",
                booktitle = "testtest",
                year = 2000,
                pages = testfield1
            )
            validate_reference(validate_set1)

    def test_invalid_volume_data(self):
        """Volume field is filled with invalid number"""

        with self.assertRaises(UserInputError):
            validate_set1 = Inproceedings(
                author = "testtest",
                title = "testtest",
                booktitle = "testtest",
                year = 2000,
                volume = -20
            )
            validate_reference(validate_set1)

    def test_invalid_number_data(self):
        """Number field is filled with invalid number"""

        with self.assertRaises(UserInputError):
            validate_set1 = Inproceedings(
                author = "testtest",
                title = "testtest",
                booktitle = "testtest",
                year = 2000,
                number = -20
            )
            validate_reference(validate_set1)

    def test_invalid_month(self):
        """Month field is filled with invalid number"""

        with self.assertRaises(UserInputError):
            validate_set1 = Inproceedings(
                author = "testtest",
                title = "testtest",
                booktitle = "testtest",
                year = 2000,
                month = 55
            )
            validate_reference(validate_set1)

    def test_invalid_optional_fields(self):
        """Some field is filled with invalid data"""

        with self.assertRaises(UserInputError):
            testfield1 = "test" * 200
            validate_set1 = Inproceedings(
                author = "testtest",
                title = "testtest",
                booktitle = "testtest",
                year = 2000,
                address = "testtest",
                series = testfield1
            )
            validate_reference(validate_set1)

        with self.assertRaises(UserInputError):
            testfield2 = "test" * 200
            validate_set2 = Inproceedings(
                author = "testtest",
                title = "testtest",
                booktitle = "testtest",
                year = 2000,
                address = testfield2,
                series = "testtest"
            )
            validate_reference(validate_set2)
