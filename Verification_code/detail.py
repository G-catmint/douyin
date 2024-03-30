import time
import execjs
import requests
"""
获取 Verification_code.py 的参数信息
"""


class Detail:
    def __init__(self):
        self.url = "https://www.douyin.com/user/MS4wLjABAAAAx-mH1oMVAHDSCU4YM-_AnJyAK7wYYxYQeGniL_dmZw4BBbkZ-rLoRxon6WTbjrRd"


    @staticmethod
    def verificat_headers():
        return {
            "authority": "www.douyin.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "referer": "https://www.douyin.com/user/MS4wLjABAAAAx-mH1oMVAHDSCU4YM-_AnJyAK7wYYxYQeGniL_dmZw4BBbkZ-rLoRxon6WTbjrRd",
            "^sec-ch-ua": "^\\^Chromium^^;v=^\\^122^^, ^\\^Not(A:Brand^^;v=^\\^24^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }

    def reqresp(self,session):
        header = self.verificat_headers()
        __ac_response = session.get(self.url, headers=header)
        print(__ac_response.text)
        cookie = {
            "IsDouyinActive":"false",
            '__ac_nonce':__ac_response.cookies['__ac_nonce'],
            "__ac_referer":"__ac_blank",
            "__ac_signature":"",
            "architecture":"amd64",
            "device_web_cpu_core":"16",
            "device_web_memory_size":"8",
            "xg_device_score":"6.932970889109521"
        }
        print("第一次主页cookie值获取成功",cookie)
        with open("signature.js","r",encoding="UTF-8") as file:
            result = file.read()
        cookie['__ac_signature'] = execjs.compile(result).call('main', cookie['__ac_nonce'])
        response = session.get(self.url, headers=header,cookies=cookie)
        print("第二次主页参数获取成功")
        return response.text


if __name__ == '__main__':
    session = requests.session()
    detail = Detail()
    print('22222222222222222222222222',detail.reqresp(session))
