import unittest
from util import generate_citekey

class TestCitekeyGeneration(unittest.TestCase):
    def setUp(self):
        pass

    def test_citekey_is_generated_correctly(self):
        """Testing if citekey is generated correctly"""

        information = {"author": "Robert C. Martin",
                       "title":"Clean Code",
                       "year":"2008"}
        
        generated_key = generate_citekey(information)
        self.assertEqual(generated_key, "Martin2008CleanCode")

    def test_citekey_is_generated_correctly_with_long_title(self):
        """Testing if citekey is generated correctly even if the title is long"""

        information = {"author": "Erich Gamma",
                       "title":"Design Patterns: Elements of Reusable Object-Oriented Software",
                       "year":"1994"}
        
        generated_key = generate_citekey(information)
        self.assertEqual(generated_key, "Gamma1994DesignPatternsE")

    def test_citekey_is_generated_correctly_with_removed_stopwords(self):
        """Testing if citekey is generated correctly even if the title contains stopwords"""

        information = {"author": "Roy Osherove",
                       "title":"The Art of Unit Testing",
                       "year":"2013"}
      
        generated_key = generate_citekey(information)
        self.assertEqual(generated_key, "Osherove2013ArtUnitTesting")