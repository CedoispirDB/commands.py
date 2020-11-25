import selenium
from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

keep = True
browser = webdriver.Firefox()
browser.get("https://www.youtube.com/watch?v=WTauSDXSZg8")
while keep:
    try:
        button = browser.find_element_by_xpath(
            "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div["
            "1]/div/div/div/ytd-player/div/div/div[5]/button")
        time.sleep(5)
        button.click()
        print("passing")
        break
    except NoSuchElementException:
        continue
    except ElementNotInteractableException:
        time.sleep(2)

browser.quit()

# button = browser.find_element_by_xpath(
#     "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div["
#     "1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button "
# )
# button.click()
# //*[@id="ad-text:4"] -- Xpath do ad
