import unittest
from util import validate_reference, UserInputError

class TestReferenceValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_length_does_not_raise_error(self):
        """All validated fields are filled and passed"""
        validate_reference("juokse", "juokse", "juokse", "2020", "juokse")
        validate_reference("a" * 100, "a" * 100, "a" * 100, "1999", "a" * 100)

    def test_too_short_or_long_raises_error(self):
        """All validated fields are filled with too short or long strings"""
        with self.assertRaises(UserInputError):
            validate_reference("ole", "ole", "ole", "ole", "ole")

        with self.assertRaises(UserInputError):
            validate_reference("koodaa" * 20, "koodaa" * 20, "koodaa" * 20, "1999", "koodaa" * 20)
