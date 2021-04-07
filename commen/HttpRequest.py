#encoding:utf-8
#anthor:mengdebin
import requests
'''取消HTTPS的警告'''
requests.packages.urllib3.disable_warnings()
'''封装http请求'''
class HttpRequest:
    def HttpRequestMethod(self,url,data,method,**kwargs):
        global res
        if method == 'get':
            res = requests.get(url,data,verify=False,**kwargs)
        elif method =='post':
            res = requests.post(url,data,verify=False,**kwargs)
        else:
            print("请输入正确的请求方式")
        return res


# if __name__ == '__main__':
#     url='https://api.shaoziketang.com/wap/v3.0/login/data'
#     data={"mobile":"17713162100","rand":"456987"}
#     res= HttpRequest().HttpRequestMethod(url,data,'post')
#     print('登录的token是', res.json()['data']['token'])
