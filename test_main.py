import unittest
from main import add
class TestMain(unittest.TestCase):
    def test_add(self):
        assert add(2,3) == 5
        assert add(-1,1) == 0
        
# if expected output and actual output is same then we will get the result as pass        
#Assert is Assertion  function which checking