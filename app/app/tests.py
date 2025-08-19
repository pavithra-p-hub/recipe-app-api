"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subract_numbers(self):
        """Test subract from x and y"""
        res = calc.subract(25, 20)

        self.assertEqual(res, 5)
