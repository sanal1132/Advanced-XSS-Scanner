import unittest
from src.utils.encoder import encode_payload

class TestUtils(unittest.TestCase):
    def test_encode_payload_html(self):
        payload = "<script>alert('XSS')</script>"
        self.assertEqual(encode_payload(payload, "html"), "&lt;script&gt;alert(&#x27;XSS&#x27;)&lt;/script&gt;")

if __name__ == "__main__":
    unittest.main()
