from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class LinkedInScraper:
    def __init__(self, email, password):
        self.EMAIL = email
        self.PASSWORD = password
        self.options = Options()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
    
    def login(self):
        self.driver.get("https://www.linkedin.com/")
        email_field = self.driver.find_element('xpath', "/html/body/main/section[1]/div/div/form/div[2]/div[1]/input")
        email_field.send_keys(self.EMAIL)
        time.sleep(1)
        password_field = self.driver.find_element('xpath', "/html/body/main/section[1]/div/div/form/div[2]/div[2]/input")
        password_field.send_keys(self.PASSWORD)
        time.sleep(1)
        login_button = self.driver.find_element('xpath', "/html/body/main/section[1]/div/div/form/button")
        login_button.click()
        time.sleep(5)
    
    def scrape_profile(self, profile_url):
        self.driver.get(profile_url)
        start = time.time()
        initial_scroll = 0
        final_scroll = 1000
        while True:
            self.driver.execute_script(f"window.scrollTo({initial_scroll},{final_scroll})")
            initial_scroll = final_scroll
            final_scroll += 1000
            time.sleep(3)
            end = time.time()
            if round(end - start) > 20:
                break
        name=self.driver.find_element('xpath','/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/h1')
        bio = self.driver.find_element('xpath','/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[2]')
        address = self.driver.find_element('xpath','/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[2]/span[1]')
        return name.text, bio.text, address.text
    
    def close_browser(self):
        self.driver.close()
