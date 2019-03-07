import requests
import uuid
import os
from bs4 import BeautifulSoup
from login.videorank.feteadm_api import FateadmApi
from cookiespool.config import *

class VideoRankCookies():
    def __init__(self, mobile, password):
        self.url = 'https://videorank.cn/login'
        self.mobile = mobile
        self.password = password
        self.is_login = False

    def login(self):
        """
        登录
        :return:
        """

        #获取cookie
        response = requests.get(self.url)
        cookies = response.cookies
        #获取token
        token = ''
        soup = BeautifulSoup(response.text, 'lxml')
        token = soup.find(attrs={'name' : '_token'}).get('value')
        headers = {
            'Host': 'videorank.cn',
            'Origin': 'https://videorank.cn',
            'Referer': 'https://videorank.cn/login',
            'Accept' : 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Encoding': 'gzip',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
        }

        #通过cookie获取验证码
        response = requests.get('https://videorank.cn/captcha/default', headers= headers, cookies = cookies)
        # print(response.content)
        file_name = '/app/image/' + str(uuid.uuid1()) + '.png'
        with open(file_name, 'wb') as f:
            f.write(response.content)
        #解析验证码
        captcha = self.get_captcha_code(file_name)
        os.remove(file_name)
        #登录
        response = requests.post(
            'https://videorank.cn/login?_token=' + token + '&mobile=' + self.mobile + '&password=' + self.password + '&captcha=' + captcha.value, headers= headers, cookies=response.cookies, verify=False)
        # print(response.cookies)
        # print(response.text)
        if (response.text.find(self.mobile) > -1):
            self.is_login = True
            self.cookies = response.cookies._cookies.get('videorank.cn').get('/')

    def get_captcha_code(self, file_name):
        pd_id = FATEADM_API_MAP.get('pd_id')  # 用户中心页可以查询到pd信息
        pd_key = FATEADM_API_MAP.get('pd_key')
        app_id = FATEADM_API_MAP.get('app_id')  # 开发者分成用的账号，在开发者中心可以查询到
        app_key = FATEADM_API_MAP.get('app_key')
        # 识别类型，
        # 具体类型可以查看官方网站的价格页选择具体的类型，不清楚类型的，可以咨询客服
        pred_type = '30400'
        api = FateadmApi(app_id, app_key, pd_id, pd_key)
        rsp = api.PredictFromFile(pred_type, file_name)
        if (rsp != None and rsp.ret_code == 0):
            # print(rsp.pred_rsp)
            return rsp.pred_rsp

    def main(self):
        self.login()
        if (self.is_login):
            cookies = self.get_cookies()
            return {
                'status': 1,
                'content': cookies
            }
        else:
            return {
                'status': 3,
                'content': '登录失败'
            }

    def get_cookies(self):
        array = []
        for x, y in self.cookies.items():
            dict = {}
            dict['name'] = x
            dict['value'] = y.value
            array.append(dict)
        return array


if __name__ == '__main__':
    VideoRankCookies('', '').main();