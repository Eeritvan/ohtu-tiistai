import unittest
from services.generate_color import generate_color

class TestColorGeneration(unittest.TestCase):
    def setUp(self):
        pass

    def test_generate_color(self):
        """Tests if generate returns color names correctly"""

        #Id is given
        generated_color = generate_color(5)
        expected_color = "255, 165, 0" # code for orange

        self.assertEqual(generated_color, expected_color)

        # No id, database not working yet
        generated_color = generate_color()
        expected_color = "Black"

        self.assertEqual(generated_color, expected_color)
