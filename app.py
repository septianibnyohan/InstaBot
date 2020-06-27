from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utility_methods.utility_methods import *
from bs4 import BeautifulSoup
import time

class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password

        self.login_url = config['IG_URLS']['LOGIN']
        self.nav_user_url = config['IG_URLS']['NAV_USER']
        self.get_tag_url = config['IG_URLS']['SEARCH_TAGS']

        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username = bot.find_element_by_name("username")
        password = bot.find_element_by_name("password")
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(3)
        bot.find_element_by_class_name('Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB').click()
        time.sleep(8)
    
    def open_live(self, user_live):
        bot = self.bot
        # bot.find_element_by_class_name('sqdOP.yWX7d.y3zKF').click()
        # bot.find_element_by_class_name('aOOlW.HoLwm').click()
        # bot.find_element_by_class_name('_-3_95').click()
        bot.get("https://www.instagram.com/" +  user_live + "/live/")

    def follow_user(self, user):
        """
        Follows user(s)
        Args:
            user:str: Username of the user to follow
        """

        self.nav_user(user)

        follow_buttons = self.find_buttons('Follow')

        for btn in follow_buttons:
            btn.click()

    def nav_user(self, user):
        """
        Navigates to a users profile page
        Args:
            user:str: Username of the user to navigate to the profile page of
        """
        bot = self.bot
        bot.get(self.nav_user_url.format(user))

    def find_buttons(self, button_text):
        """
        Finds buttons for following and unfollowing users by filtering follow elements for buttons. Defaults to finding follow buttons.
        Args:
            button_text: Text that the desired button(s) has 
        """

        buttons = self.bot.find_elements_by_xpath("//*[text()='{}']".format(button_text))

        return buttons

    def close_all_notify(self):
        bot = self.bot
        bot.find_element_by_class_name('yWX7d').click()
        time.sleep(1)
        bot.find_element_by_class_name('HoLwm').click()

    def detect_live(self):
        html = self.bot.page_source
        soup = BeautifulSoup(html, 'html.parser')
        #results = soup.find_all("div",{"class":"eebAO"})
        results = soup.find_all("li",{"class":"Ckrof"})
        
        for result in results:
            res = result.find("div",{"class":"eebAO"})
            live = result.find("span",{"class":"_1iHbP"})

            if (live != None):
                user_live = res.get_text()
                self.open_live(user_live)

    def send_message(self,username, message):
        bot = self.bot;
        bot.find_element_by_class_name('xWeGp').click()
        bot.find_element_by_class_name('sqdOP').click()
        # type username for search
        search_user = bot.find_element_by_name('queryBox')
        search_user.clear()
        search_user.send_keys(username)
        time.sleep(2)
        bot.find_element_by_class_name('dCJp8').click()
        # click next
        bot.find_element_by_class_name('cB_4K').click()
        time.sleep(2)
        msg = bot.find_element_by_css_selector('div.vwCYk > textarea')
        msg.clear()
        msg.send_keys(message)

        #click send
        bot.find_element_by_css_selector('.JI_ht > .sqdOP').click()

if __name__ == '__main__':

    config_file_path = './config.ini' 
    logger_file_path = './bot.log'
    config = init_config(config_file_path)
    logger = get_logger(logger_file_path)

    # username = input("Masukkan username : ")
    # password = input("Masukkan password : ")
    username = 'medcollections18@gmail.com'
    password = 'lak1lak1'

    go = InstaBot(username, password)
    go.login()
    go.close_all_notify()
    go.send_message('septianyohan', 'test send message')
    
    '''
    res = result.find("div",{"class":"eebAO"})
    live = result.find("span",{"class":"_1iHbP"})
    if (res != None):
        if (live != None):
            print(".....................LIVE...................")
        print(res.get_text())
        print('=====================================')
    '''
    #print(html)
    #go.open_live()
    #go.nav_user('septianyohan')
    #go.follow_user('septianyohan')