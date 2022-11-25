from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Controller
import pyautogui
import time


url = 'https://www.facebook.com/login.php'      #the main url that we will work on

class FbLog:        #define new class
    def __init__(self, email, browser, password):       #contructor of our class

        self.email = email
        self.password = password

        if browser == 'Chrome':
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())     #operate with the Chrome browser
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())     #operate with the Firefox browser

        self.driver.get(url)        #open url with the chosen browser

    def log(self):      #function that logs into facebook account using email and password
        mail = self.driver.find_element(By.ID,'email')      #search the element on the page with the id email
        mail.send_keys(self.email)      #write down email

        pw = self.driver.find_element(By.ID,'pass')      #search the element on the page with the id pass
        pw.send_keys(self.password)      #write down password
        time.sleep(2)       #stop execution for a couple of seconds in case the internet is bad
        log_but = self.driver.find_element(By.ID,'loginbutton')      #search the element on the page with the id loginbutton
        log_but.click()     #click the login button

    def Message(self, i):
        self.kb=Controller()      #create an object of the Controller() class to control the keyboard
        pyautogui.hotkey("p")       #open the post box
        time.sleep(5)
        pyautogui.hotkey('win','v')     #get access to the clipboard, you must have already coppied the texts you want to post
        time.sleep(3)
        for elem in range(i):
            self.kb.press(Key.down)
            self.kb.release(Key.down)       #each time post an element of the clipboard
            time.sleep(1)
        
        pyautogui.hotkey('enter')       #choose the clipboard element
            
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'enter')       #post element


if __name__ == '__main__':          #main program
    kb=Controller()
    emails = []     #a list to fill with the emails of the accounts
    passwords = []      #the paswords of the accounts
    likes = int(input("Number of likes: "))     #in case the user want to like some posts of friends
    while True:
        email = input("enter email or press enter if this was the last email: ")
        if email == "":     #if there is no more emails to enter, an empty string will stop the input prompt
            break
        password = input("Enter password: ")
        emails.append(email)        #add the email the the list of emails
        passwords.append(password)      #add the password the the list of password
        
    for i in range(len(emails)):
        fb_login = FbLog(emails[i], input("Chrome or Firefox? : ").title(), password)       #each time create an object of the FbLog class, give it the email and passord and choose the browser
        fb_login.log()      #log in the account
        time.sleep(15)      #always in case the net is bad
        fb_login.Message(i)     #post the message
        time.sleep(15)
        
        for j in range(likes):      #for the like button, like posts using keyboard shortcuts
            pyautogui.hotkey('j')
            time.sleep(1)
            pyautogui.hotkey('l')
            time.sleep(1)
            kb.press(Key.enter)
            time.sleep(2)
        

