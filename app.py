from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Whatsapp_Bot:
    def __init__(self,recipient,rep,msg):
        print("Initializing Whatapp_Bot...")
        self.to = recipient
        self.rep = rep
        self.msg = '#    ' + msg
        self.bot = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
    def auth(self):
        print('opening browser...')
        browser = self.bot
        browser.get("https://web.whatsapp.com")
        time.sleep(8)
        print('Done')
        res = input("Scan QR Code to login and press enter key to continue...")
        if(res==''):
            print("continuing...")
            searchbox = browser.find_element_by_class_name('_2zCfw') #searchBox
            searchbox.clear()
            searchbox.send_keys(self.to)
            searchbox.send_keys(Keys.RETURN)
            time.sleep(3)
            body = browser.find_element_by_tag_name("body") 
            for i in range(0,self.rep):
                try:
                    body.send_keys(self.msg)
                    btn = browser.find_element_by_class_name("_3M-N-")
                    btn.click()
                    time.sleep(0.5)
                except:
                    print(i,"Messages sended Successfully,",self.rep-i,"Missed.")
                    break
                print(i+1) # Couting             
        else:
            print("Okay Exiting...")
            browser.close()

to = input("To : ")
msg = input("Message : ")
reps = int(input("No. of repetitions :"))
app = Whatsapp_Bot(to,reps,msg) # parameters (<recipient>)
app.auth()
input()