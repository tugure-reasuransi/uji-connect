import unittest
from app import H

class Uji(unittest.TestCase):
    def test_kelas_http_ada(self):
        self.assertTrue(issubclass(H, object))

if __name__ == "__main__":
    unittest.main()
