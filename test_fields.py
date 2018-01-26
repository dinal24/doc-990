import unittest, json
import fields, utility

at, rt = utility.get_token()

class TestBotActions(unittest.TestCase):
    def test_get_payment_methods(self):
        self.assertRaises(fields.get_payment_methods(at))
#
#     def test_get_hospital_list(self):
#         self.assertRaises(fields.get_hospital_list(at))
#
#     def test_get_doctor_list(self):
#         self.assertRaises(fields.get_doctor_list(at))
#
#     def test_get_specialization_list(self):
#         self.assertRaises(fields.get_specialization_list(at))

class TestBotActions2(unittest.TestCase):

    # def test_get_doctors_by_name(self):
    #     self.assertRaises(fields.get_doctors_by_name(at, "NIMALI FERNANDO"))

    # def test_get_session_by_doctor_hospital(self):
    #     self.assertRaises(fields.get_session_by_doctor_hospital(at, 147, 70))

    def test_get_session_availability(self):
        self.assertRaises(fields.get_session_availability(at, 'ECL-D0350-H03-1516874400-2'))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBotActions)
    unittest.TextTestRunner(verbosity=2).run(suite)