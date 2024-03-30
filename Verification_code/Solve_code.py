import requests
from jfbym import YdmVerify
from RepairPictures import RepairPictures

"""
保存 修复 识别 验证码
"""


class SolveCode:
    def __init__(self):
        self.repic = RepairPictures()
        self.ydmverify = YdmVerify()

    def get_pic_url(self,json_url_data):
        try:
            question = json_url_data['data']['question']
            self.save_pic(question['url1'])
            self.save_pic(question['url2'])
            print("图片保存成")
            self.repic.change_pic()
            print("BIG.PNG修复成功")
            return self.slide_verify()
        except Exception as e:
            print("大概率因为这一次传来的不是滑块验证码")

    @staticmethod
    def get_headers():
        return {
            "authority": "verify.snssdk.com",
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "origin": "https://rmc.bytedance.com",
            "pragma": "no-cache",
            "referer": "https://rmc.bytedance.com/",
            "^sec-ch-ua": "^\\^Chromium^^;v=^\\^122^^, ^\\^Not(A:Brand^^;v=^\\^24^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }

    def save_pic(self,url):
        response = requests.get(url=url,headers=self.get_headers())
        if '1.png' in url:pic_name = "small.png"
        else:pic_name = "big.png"
        with open("./Verification_pic/"+pic_name,"wb") as file:
            file.write(response.content)

    def slide_verify(self):
        backImage = open('./Verification_pic/bigger.png', 'rb').read()
        slidingImage = open('./Verification_pic/small.png', 'rb').read()
        pic_data = self.ydmverify.slide_verify(slide_image=slidingImage, background_image=backImage,verify_type="20111")
        return pic_data


if __name__ == '__main__':
    solvecode = SolveCode()
    size = solvecode.get_pic_url({'code': 200, 'data': {'challenge_code': 99999, 'codifica': 'true', 'cyfreso': 2, 'host': '', 'id': '738be3cdcbaee038b1e36ff833cba5c5f9ffdbb1', 'mode': 'slide', 'question': {'url1': 'https://p3-catpcha.byteimg.com/tos-cn-i-188rlo5p4y/548f8230dd134efdad6a1dfb68d25902~tplv-188rlo5p4y-2.jpeg', 'url2': 'https://p3-catpcha.byteimg.com/tos-cn-i-188rlo5p4y/d4c5760c909541c2bb4cdfe0b4f6f0dc~tplv-188rlo5p4y-1.png', 'backup_url1': ['https://p6-catpcha.byteimg.com/tos-cn-i-188rlo5p4y/548f8230dd134efdad6a1dfb68d25902~tplv-188rlo5p4y-2.jpeg', 'https://p9-catpcha.byteimg.com/tos-cn-i-188rlo5p4y/548f8230dd134efdad6a1dfb68d25902~tplv-188rlo5p4y-2.jpeg'], 'backup_url2': ['https://p6-catpcha.byteimg.com/tos-cn-i-188rlo5p4y/d4c5760c909541c2bb4cdfe0b4f6f0dc~tplv-188rlo5p4y-1.png', 'https://p9-catpcha.byteimg.com/tos-cn-i-188rlo5p4y/d4c5760c909541c2bb4cdfe0b4f6f0dc~tplv-188rlo5p4y-1.png'], 'tip_y': 91, 'obfuscation': 'QWAYSS'}, 'region': '', 'version': 2}, 'message': '验证通过'})
    print(size)