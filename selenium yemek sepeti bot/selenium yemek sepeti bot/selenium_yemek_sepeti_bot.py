
from YmkSptUserInfo import email, password, address
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha


class YemekSepeti:
    def __init__(self, email, password, address):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-blink-features=AutomationControlled')    
        self.browser = webdriver.Chrome()
        driver = self.browser
        #WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))
        #WebDriverWait(self.browser, 20).until(EC.frame_to_be_available_and_switch_to_it(("xpath","//iframe[@title='reCAPTCHA']")))
        self.email = email
        self.password = password
        self.address = address
     

    def signIn(self):
        self.browser.get("https://www.yemeksepeti.com/login/new")
        try:
            element = WebDriverWait(self.browser, 120).until(
            EC.presence_of_element_located((By.ID, "recaptcha-anchor"))
    )
        finally:
            self.browser.quit()

        #button = self.browser.find_element("xpath", "//*[@id='login-page-react-root']/main/div/div/div[2]/button").click
        #time.sleep(2)
        emailInput = self.browser.find_element("xpath","//*[@id='email']")
        emailButton =self.browser.find_element("xpath","//*[@id='login-page-react-root']/main/div/form/div[3]/button").click
        passwordInput = self.browser.find_element("xpath","//*[@id='_password']")
        adressInput = self.browser.find_element("xpath","//*[@id='delivery-information-postal-index']")
        addresssButton = self.browser.find_element("xpath","//*[@id='delivery-information-postal-index-form']/div[2]/button[1]").click
        
        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
        adressInput.send_keys(self.address)

ymkspt = YemekSepeti(email, password, address)
ymkspt.signIn()

        
#print(email) 
#print(address)