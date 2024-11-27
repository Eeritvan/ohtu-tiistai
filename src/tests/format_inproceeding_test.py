import unittest
from services.format_inproceedings import format_inproceedings
from entities.reference import Inproceedings

class TestBibtexGeneration(unittest.TestCase):
    def setUp(self):
        pass

    def test_bibtex_format_is_generated_correctly(self):
        """Testing if bibtex export is generated correctly"""

        information = Inproceedings(
            db_id=1,
            ref_type="inproceeding",
            citekey="Martin2008CleanCode",
            author="Robert C. Martin",
            title="Clean Code",
            year="2008",
            booktitle="Clean Code",
            pages="100-110",
        )
        generated_format = format_inproceedings(information)

        # a bit odd formatting but this cant be changed without the test breaking
        expected_format ="""@inproceedings{Martin2008CleanCode,
    author = {Robert C. Martin},
    title = {Clean Code},
    year = {2008},
    booktitle = {Clean Code},
    pages = {100-110}
}"""

        self.assertEqual(generated_format, expected_format)
