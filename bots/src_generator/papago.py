import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')


class Papago:
    """
    result = Papago('en').translate('what is this ?')
    print(result)

    """
    def __init__(self, lang:str='en'):
        self._lang=lang
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('lang=ko_kr')
        
        self._wd = webdriver.Chrome('chromedriver.exe', options=chrome_options)
        self._wd.get('https://papago.naver.com/')# 웹페이지 가져 오기
        pass
        
    
        
    def translate(self, text="hello"):

        # 입력 언어 선택
        dropMenu = WebDriverWait(self._wd, 20).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="ddSourceLanguageButton"]')))
        dropMenu.click()
        selector_lang = WebDriverWait(self._wd, 20).until(EC.element_to_be_clickable((By.XPATH , self._get_dict_lang())))
        selector_lang.click()

        # 입력
        input_text = WebDriverWait(self._wd, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sourceEditArea"]')))
        input_text.send_keys('d'+text) # 텍스트 입력,  텍스트의 가장 앞에는 더미 문자 추가해줘야 함
        
        # 출력 언어 선택
        # 구현 안함, 입력 언어와 동일한 방식으로 선택

        
        #번역하기 버튼 클릭
        trans_btn = WebDriverWait(self._wd, 20).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="btnTranslate"]')))
        # self._wd.find_element(By.XPATH , '//*[@id="btnTranslate"]')  
        trans_btn.click()
        time.sleep(1)
        
        #번역된 결과 보기
        result = WebDriverWait(self._wd, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="targetEditArea"]')))

        return result.text

    def _get_dict_lang(self, lang:str='auto') ->str: # 언어 선택
        dict_lang={'auto':'//*[@id="ddSourceLanguage"]/div[2]/ul/li[1]/a',
                   'kr':'//*[@id="ddSourceLanguage"]/div[2]/ul/li[2]/a',
                   'en':'//*[@id="ddSourceLanguage"]/div[2]/ul/li[3]/a',
                   'jp':'//*[@id="ddSourceLanguage"]/div[2]/ul/li[4]/a',
                   'cn':'//*[@id="ddSourceLanguage"]/div[2]/ul/li[3]/a'}
        return dict_lang.get(lang)



