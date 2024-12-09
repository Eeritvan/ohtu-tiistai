import unittest
from services.validate_tag import validate_tag, UserInputError

class TestReferenceValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_correct_tag_does_not_raise_error(self):
        """Tag is valid"""

        test_tag1 = "testtest"
        validate_tag(test_tag1)

        test_tag2 = "testtesttesttest"
        validate_tag(test_tag2)

    def test_invalid_tag_raises_error(self):
        """Tag is too long or too short"""

        with self.assertRaises(UserInputError):
            test_tag1 = "test" * 10
            validate_tag(test_tag1)

        with self.assertRaises(UserInputError):
            test_tag2 = "a"
            validate_tag(test_tag2)