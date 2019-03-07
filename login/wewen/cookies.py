import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WewenCookies():
    def __init__(self, username, password, browser):
        self.url = 'https://api.weibo.com/oauth2/authorize?client_id=3998129927&redirect_uri=http%3A%2F%2Fwewen.io%2Fconnect%2Fweibo%2Fresponse&response_type=code'
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 20)
        self.username = username
        self.password = password
        self.is_login = False

    def login(self):
        """
        打开网页输入用户名密码并点击
        :return: None
        """

        """
                打开网页输入用户名密码并点击
                :return: None
                """
        self.browser.delete_all_cookies()
        self.browser.get(self.url)
        username = self.wait.until(EC.presence_of_element_located((By.ID, 'userId')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'passwd')))
        submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@tabindex=''4'']')))
        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(1)
        submit.click()
        time.sleep(5)
    def get_cookies(self):
        """
        获取Cookies
        :return:
        """
        return self.browser.get_cookies()

    def login_successfully(self):
        """
        判断是否登录成功
        :return:
        """
        try:
            return bool(
                WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'ui dropdown se item'))))
        except TimeoutException:
            return False

    def main(self):
        self.login()
        if (self.login_successfully):
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
        """
        获取Cookies
        :return:
        """
        return self.browser.get_cookies()


if __name__ == '__main__':
    WewenCookies('@163.com', '').main();