import unittest
import rubik.info as info

class InfoTest(unittest.TestCase):
    
    def test_Info_010_ShouldReturnMyUserName(self):
        expectedResult = {'info': 'umphrda'}
        parms = {'op': 'info'}
        actualResult = info._info(parms)
        self.assertDictEqual(expectedResult, actualResult)