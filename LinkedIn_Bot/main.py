#Berk Küçük
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
Username = input("LinkedIn Username:")
Passwd = input("LinkedIn Password:")
Parameter = input("Enter Find Parameter")

class LinkedIn:

    def __init__(self,username,passwd):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver', chrome_options=self.browserProfile)
        self.username = username
        self.passwd = passwd

    def SignIn(self):
        self.browser.get("https://www.linkedin.com/login/SignIn=true&trk=guest_homepage-basic_nav-header-signin")
        self.browser.maximize_window()
        UsernameInput = self.browser.find_element_by_xpath('//*[@id="username"]')
        PasswdInput = self.browser.find_element_by_xpath('//*[@id="password"]')

        UsernameInput.send_keys(self.username)
        PasswdInput.send_keys(self.passwd)

        btnSubmit = self.browser.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
        btnSubmit.click()

        time.sleep(1)

    def Search(self, param):
        searchInput = self.browser.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input')
        searchInput.click()
        searchInput.send_keys(str(param))
        time.sleep(1)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(4)
        url = self.browser.current_url
        url = url.replace("all", "people")
        self.browser.get(url)

    def connct(self):
        counter = 1
        page = 1
        body = self.browser.find_element_by_css_selector('body')
        while True:

            time.sleep(1)
            connectButon = self.browser.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li['+str(counter)+']/div/div/div[3]/div')

            time.sleep(2)

            if connectButon.text == "Connect":
                try:
                    self.browser.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li['+str(counter)+']/div/div/div[3]/div').click()
                except:
                    print("Hata")
                body.send_keys(Keys.ESCAPE)
            counter += 1
            if counter == 4:
                body.send_keys(Keys.PAGE_DOWN)
            if counter == 10:
                counter = 1
                page += 1
                self.browser.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[4]/div/div/ul/li['+str(page)+']/button').click()

                time.sleep(3)
        time.sleep(2)
linkedIn =  LinkedIn(Username,Passwd)
linkedIn.SignIn()
linkedIn.Search(Parameter)
linkedIn.connct()
