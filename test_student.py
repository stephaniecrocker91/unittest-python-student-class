import unittest
from student import Student

class TestStudent(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print("set up class")

    def setUp(self):
        print('setup')
        # student is an instance variable 
        # Since student is now an instance variable,  
        # we’ll need to go and change every 
        # reference from student to self.student.
        student = Student('John', 'Doe')

    @classmethod
    def tearDownClass(cls):
        print("tear down Class")

    def tearDown(self):
        print("tear down")


    def test_full_name(self):
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_alert_santa(self):
        student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    
    def test_email(self):
        self.assertEqual(self.student.email, "john.doe@email.com")

# we can run the file  without having to specify the Unittest module.
if __name__ == '__main__':    
    unittest.main()