import os
import sys
from selenium import webdriver
import time

# Create a new folder and go into it
name = str(sys.argv[1])
lang = str(sys.argv[2])
path = os.path.join("/Users/marcobarreirinhas/Programs/" + lang, name)
os.mkdir(path)
newPath = "/" + lang + "/" + name

# Create new repository in GitHub
browser = webdriver.Firefox()
browser.get("https://github.com/login")
python_button = browser.find_element_by_xpath("//*[@id='login_field']")
python_button.send_keys("CedoispirDB")
python_button = browser.find_element_by_xpath("//*[@id='password']")
python_button.send_keys("recabucatrigo123")
python_button = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[12]")
python_button.click()
python_button = browser.find_element_by_xpath("/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a")
python_button.click()
python_button = browser.find_element_by_xpath("//*[@id='repository_name']")
python_button.send_keys(name)
python_button = browser.find_element_by_xpath("//*[@id='repository_visibility_private']")
python_button.click()
time.sleep(1)
python_button = browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/button")
python_button.click()
browser.quit()
sys.exit(newPath)

