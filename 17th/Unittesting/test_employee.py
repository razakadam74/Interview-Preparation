import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setup')
        self.emp1 = Employee('Corey', 'Schafer', 50000)
        self.emp2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print('tearDown')

    def test_email(self):
        print('test_email')
        self.emp1.first = 'John'
        self.emp2.first = 'Jane'
        self.assertEqual(self.emp1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp2.fullname, 'Sue Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)

    def test_month_schedule(self):
        with patch('employee.requests.get') as mocked_get:
             mocked_get.return_value.ok = True
             mocked_get.return_value_text = 'Success'

             schedule = self.emp1.monthly_schedule('May')
             mocked_get.assert_called_with('http://company.com/Schafer/May')
             self.assertEqual(schedule, 'Success')

if __name__ == '__main__':
    unittest.main()
