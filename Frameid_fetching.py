from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class RadioButton:

    
    def __init__(self, url = "https://www.cowin.gov.in/"):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    def boot(self):
       self.driver.get(self.url)
       sleep(3)
       self.driver.maximize_window()
       sleep(10)


    def clickFAQ(self):
       fullXpath = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a"
       element = self.driver.find_element(by=By.XPATH, value=fullXpath)
       element.click
       sleep(5)

           
    def clickPARTNERS(self):
       relativeXpath = "//div[@class='menunavigation']/ul/li[5]/a"
       element = self.driver.find_element(by=By.XPATH, value=relativeXpath)
       element.click
       sleep(5)
       
                                                                                                                                                                                                            
                                                                                                                                                                                                       #to get window ID
       print("inventory")                                                                                                                                                                                                                                                                                                                                                                               
       print(self.driver.current_window_handle)
       
       self.driver.execute_script("window.open('about:blank', '_blank')")
       self.driver.switch_to.window(self.driver.window_handles[1])
       self.driver.get(self.url)                                                                                                        
       
       print("login")
       print(self.driver.current_window_handle)
                                                                                                                                                                                                                                                                
       
       #to close current window
       self.driver.close()                                                                                                                                                                                                                                                          
       sleep(3)
       #self.quit
       
           
obj = RadioButton()
obj.boot()
obj.clickFAQ()
obj.clickPARTNERS()





 

