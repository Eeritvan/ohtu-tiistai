import unittest
from services.format_inproceedings import format_reference
from entities.reference import Inproceedings, Book, Article

class TestBibtexGeneration(unittest.TestCase):
    def setUp(self):
        pass

    def test_bibtex_format_is_generated_correctly(self):
        """Testing if bibtex export is generated correctly"""

        information = Inproceedings(
            db_id=1,
            ref_type="inproceedings",
            citekey="Martin2008CleanCode",
            author="Robert C. Martin",
            title="Clean Code",
            year="2008",
            booktitle="Clean Code",
            pages="100-110",
        )

        generated_format = format_reference(information)

        # a bit odd formatting but this cant be changed without the test breaking
        expected_format = """@inproceedings{Martin2008CleanCode,
    author = {Robert C. Martin},
    title = {Clean Code},
    year = {2008},
    booktitle = {Clean Code},
    pages = {100-110}
}"""

        self.assertEqual(generated_format, expected_format)

    def test_bibtex_format_is_generated_correctly_for_book(self):
        """Testing if bibtex export is generated correctly for book"""
        information = Book(
            db_id=1,
            ref_type="book",
            citekey="Martin2008CleanCode",
            author="Robert C. Martin",
            title="Clean Code",
            year="2008",
            publisher="Prentice Hall",
        )
        generated_format = format_reference(information)
        expected_format = """@book{Martin2008CleanCode,
    author = {Robert C. Martin},
    title = {Clean Code},
    year = {2008},
    publisher = {Prentice Hall}
}"""
        self.assertEqual(generated_format, expected_format)

    def test_bibtex_format_is_generated_correctly_for_article(self):
        """Testing if bibtex export is generated correctly for article"""
        information = Article(
            db_id=1,
            ref_type="article",
            citekey="Martin2008CleanCode",
            author="Robert C. Martin",
            title="Clean Code",
            year="2008",
            journal="Software Development",
            volume="10",
            number="2",
            pages="100-110",
        )
        generated_format = format_reference(information)
        expected_format = """@article{Martin2008CleanCode,
    author = {Robert C. Martin},
    title = {Clean Code},
    year = {2008},
    journal = {Software Development},
    volume = {10},
    number = {2},
    pages = {100-110}
}"""
        self.assertEqual(generated_format, expected_format)
