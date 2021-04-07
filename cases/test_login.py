#encoding:utf-8
import unittest
import requests
from commen.HttpRequest import HttpRequest
'''取消HTTPS的警告'''
requests.packages.urllib3.disable_warnings()
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        print("开始测试")
        self.url='https://api.shaoziketang.com/wap/v3.0/login/data'
        self.data={"mobile":"17713162100","rand":"456987"}
    def test_login(self):
        print("开始校验登录功能")
        res=HttpRequest().HttpRequestMethod(self.url,self.data,'post')
        print(res.json())
        try:
            self.assertEqual(200, res.json()['code'])
        except AssertionError as e:
            print("test_login的错误是{}".format(e))
            raise e