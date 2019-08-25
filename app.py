from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Whatsapp_Bot:
    def __init__(self,recipient,rep,msg):
        print("Initializing Whatapp_Bot...")
        self.to = recipient
        self.rep = rep
        self.msg = '#  ' + msg
        self.bot = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        self.count = 0

    def start_service(self):
        print('opening browser...')
        browser = self.bot
        browser.get("https://web.whatsapp.com")
        res = input("Scan QR Code to login and press enter key to continue...")
        if(res==''):
            print("Searching recipient...")
            searchbox = browser.find_element_by_class_name('_2zCfw') #searchBox
            searchbox.clear()
            searchbox.send_keys(self.to)
            searchbox.send_keys(Keys.RETURN)
            time.sleep(3)
            def send(number):
                i = 0
                while(i<number):
                    i+=1
                    try:
                        body = browser.find_element_by_tag_name("body")
                        body.send_keys(self.msg)
                        btn = browser.find_element_by_class_name("_3M-N-")
                        btn.click()
                        self.count += 1
                        print(self.count) # Couting
                        time.sleep(1)
                    except:
                        print(self.count,"Messages sended Successfully,",self.rep-self.count,"Missed.")
                        print("Retrying... Starting form",self.count)
                        send(self.rep - self.count)
                        break                    
            send(self.rep)  #Calling for initial state...
        else:
            print("Okay Exiting...")
            browser.close()

to = input("To : ")
msg = input("Message : ")
reps = int(input("No. of repetitions : "))

app = Whatsapp_Bot(to,reps,msg) # parameters (<recipient>,<repetitions>,<message>)
app.start_service()
input()