import unittest
from utils.ip_utils import is_valid_ipv4, is_valid_ipv6, identify_ip_version

class TestIPValidation(unittest.TestCase):
    def test_valid_ipv4(self):
        self.assertTrue(is_valid_ipv4("192.168.1.1"))
        self.assertFalse(is_valid_ipv4("999.999.999.999"))

    def test_valid_ipv6(self):
        self.assertTrue(is_valid_ipv6("::1"))
        self.assertFalse(is_valid_ipv6("GGGG::ZZZZ"))

    def test_identify_ip_version(self):
        self.assertEqual(identify_ip_version("8.8.8.8"), "IPv4 valide")
        self.assertEqual(identify_ip_version("::1"), "IPv6 valide")
        self.assertEqual(identify_ip_version("999.999.999.999"), "Adresse IP non valide")

if __name__ == "__main__":
    unittest.main()
