from time import sleep


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
sleep(3)
driver.maximize_window()


# Open the first link
driver.get("https://www.cowin.gov.in/")


# Open a new tab
driver.execute_script("window.open('about:blank', '_blank')")
sleep(3)
# window_handles = ["guvi.in", "about:blank", ... ]
driver.switch_to.window(driver.window_handles[1])
sleep(3)
driver.get("https://www.cowin.gov.in/faq")
sleep(3)


driver.execute_script("window.open('about:blank', '_blank')")
sleep(3)
driver.switch_to.window(driver.window_handles[2])
sleep(3)
driver.get("https://www.cowin.gov.in/our-partner")
sleep(3)


# First Tab
driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)
sleep(3)


# Second Tab
driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)
sleep(3)


# Third Tab
driver.switch_to.window(driver.window_handles[2])
print(driver.current_url)
sleep(3)




driver.quit()

