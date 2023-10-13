from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the soundcloud.com homepage
driver.get("https://soundcloud.com/")
time.sleep(3)

# Accepting terms & condition
agree = driver.find_element("id","onetrust-accept-btn-handler")
agree.click()

# Waiting for home page to load
time.sleep(3)

# Finding the search bar and entering text
search = driver.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/span/span/form/input")
search.send_keys("Shape of you")
search.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(3)

# Finding the song to play
play = driver.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/ul/li[1]/div/div/div/div[2]/div[1]/div/div/div[1]/a")
play.click()

# Waiting for the song to play
time.sleep(10)

# Closing the webdriver
driver.close()