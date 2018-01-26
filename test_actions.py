import unittest, json
import fields, utility

class TestBotActions2(unittest.TestCase):

    def test_find_doctor_by_name(self):
        pass

    def test_find_doctor_by_name2(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBotActions2)
    unittest.TextTestRunner(verbosity=2).run(suite)