__author__ = 'lihongchao'
import unittest
import  readconfig

class readconfig(unittest.TestCase):

    def test_ReadSection(self):
        rc=readconfig()
        rc.ReadConfig('host','ip')
        self.assertIsNotNone(rc.ReadConfig('host','ip'),"ok")


if __name__=="__main__":
    unittest.main()