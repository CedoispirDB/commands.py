from selenium import webdriver
import time

subject = input("What would you like to watch? ")
browser = webdriver.Firefox()
browser.get("https://www.google.com/")
pythonButton = browser.find_element_by_xpath("/html/body/div/div[1]/header/div[1]/form/div/div/input")
pythonButton.send_keys(subject)
pythonButton = browser.find_element_by_xpath("/html/body/div/div[1]/header/div[1]/form/div/div/span/button")
pythonButton.click()


option = input("Are you done? ")
option = option.lower()

while True:
    if option == "yes" or option == "y":
        browser.quit()
        break
