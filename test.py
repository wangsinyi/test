import unittest
import time
import requests
import json
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
from XTestRunner import HTMLTestRunner
from XTestRunner import SMTP

class Test(unittest.TestCase):
    """QPK完整測試"""   
    def test_QPK(self):
        """主畫面測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
        self.driver.delete_all_cookies()
        self.base_url = "https://qpk.qparking.com.tw/Intro"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(5)
        try :
            response = requests.get('https://qpk.qparking.com.tw/Intro')
            self.images.append(self.driver.get_screenshot_as_base64())
            self.assertEqual(response.status_code, 200)
            if response.status_code == 200:
                print("1")
                login = self.driver.find_element(By.XPATH, "/html/body/div[1]/a")
                login.click()
                self.images.append(self.driver.get_screenshot_as_base64())
                ch = self.driver.find_element(By.XPATH,"/html/body/div/div/div[1]/a/img") 
                ch.click() 
                self.images.append(self.driver.get_screenshot_as_base64())        
        except:
                print("2")
                self.assertEqual(response.status_code, 200)
if __name__ == '__main__':
    Case1 = unittest.TestSuite()
    Case1.addTests([ 
          Test('test_QPK'),     
    ])

#       以下為測試報告內容撰寫部分
#       title為頁面報告名稱
#       description為描述
#       tester為測試者
#       language為測試報告使用的語系，目前僅支援zh-CN與en語系  
#       rerun: 測試失敗或是判定Fail時重跑次數，Fail測試要是rerun設定的次數皆Fail才會判定Fail。
#       test  
    with(open('./result.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            tester="sinyi.wang",
            title='QPK test report',
            description='test',
            language='zh-CN',
            rerun=3
        )
        runner.run(Case1)