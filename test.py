import unittest

import accessing as a
class MyTestCase(unittest.TestCase):
    def test_something(self):
       print("Executing two testcases --")
       try:
           if  not(self.assertEqual(len(a.x.d), 1)):
               pass #error raises
           else:
               print("Welcome user ! Create a new account !")
       except:
              print("user present already"),
    # def test_something(self):
       if len(a.x.read("sayannah"))>0:
           print("Read function works properly")
       else:
           print("not working")



if __name__ == '__main__':
    unittest.main()
