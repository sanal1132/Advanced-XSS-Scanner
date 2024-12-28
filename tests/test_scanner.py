import unittest
from src.scanner.parameter_finder import find_parameters
from src.scanner.field_detector import detect_input_fields

class TestScanner(unittest.TestCase):
    def test_find_parameters(self):
        url = "http://example.com/?id=1&search=query"
        self.assertEqual(find_parameters(url), ["id", "search"])

    def test_detect_input_fields(self):
        url = "http://example.com/"
        self.assertTrue(detect_input_fields(url))
