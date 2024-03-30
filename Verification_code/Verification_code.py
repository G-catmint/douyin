from detail import Detail
from Solve_code import SolveCode
import requests
import re
import time
import execjs
"""
main
获取 验证码 图片信息
获取导请求get链接返回的mstoken
"""


class Verification:
    def __init__(self):
        self.session = requests.session()
        self.detail = Detail()
        self.socode = SolveCode()
        self.url = "https://verify.snssdk.com/captcha/get"

    # @staticmethod
    # def get_headers():
    #     return {
    #         "authority": "verify.snssdk.com",
    #         "accept": "*/*",
    #         "accept-language": "zh-CN,zh;q=0.9",
    #         "cache-control": "no-cache",
    #         "origin": "https://rmc.bytedance.com",
    #         "pragma": "no-cache",
    #         "referer": "https://rmc.bytedance.com/",
    #         "^sec-ch-ua": "^\\^Chromium^^;v=^\\^122^^, ^\\^Not(A:Brand^^;v=^\\^24^^, ^\\^Google",
    #         "sec-ch-ua-mobile": "?0",
    #         "^sec-ch-ua-platform": "^\\^Windows^^^",
    #         "sec-fetch-dest": "empty",
    #         "sec-fetch-mode": "cors",
    #         "sec-fetch-site": "cross-site",
    #         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    #     }

    def get_params(self,html):
        print("开始处理params")
        try:
            return {
                "aid":re.findall("aid: (.*?),",html)[0],
                'lang': 'zh',
                "subtype": re.findall(',"subtype":"(.*?)",',html)[0],
                "detail": re.findall(',"detail":"(.*?)",',html)[0],
                "server_sdk_env": re.findall(',"server_sdk_env":"(.*?)","',html)[0].replace("\\",""),
                "mode": "slide",
                "fp": re.findall(',"fp":"(.*?)",',html)[0],
                "h5_check_version": "3.5.2",
                "os_name": "windows",
                "platform": "pc",
                "os_type": "2",
                "h5_sdk_version": "3.5.34",
                "webdriver": "false",
                "tmp":str(int(time.time()*1000))
            }
        except Exception as e:
            print("错误信息:",e)

    def re_detail(self):
        self.detail_html = self.detail.reqresp(self.session)
        response = self.session.get(url=self.url,headers=self.socode.get_headers(),params=self.get_params(self.detail_html))
        print("获取两张验证码图片信息：",response.json())
        print("获取GET链接返回的cookie[msToken]：",response.cookies['msToken'])
        return [self.socode.get_pic_url(response.json()),response.cookies]

    def verify(self):
        list_detail = self.re_detail()
        url = "https://verify.snssdk.com/captcha/verify"
        params = self.get_params(self.detail_html)
        params['xx-tt-dd'] = "qJI7ttpVdGKKbSBvYqmaf0aPo"
        params['msToken'] = list_detail[1]['msToken']
        with open('./GetCaptchBody.js',"r",encoding="utf-8") as file:
            result = file.read()
        js_code = execjs.compile(result).call("main")
        response = self.session.post(url=url,headers=self.socode.get_headers(),params=params,data={"captchaBody":js_code})
        print(response.text)
        print(response)



if __name__ == '__main__':
    verification = Verification()
    verification.verify()
    # print("========size====&&======mstoken==========",verification.re_detail())

