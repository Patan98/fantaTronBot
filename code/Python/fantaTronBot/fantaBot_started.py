#!/home/YOURUSERNAME/code/Python/venvs/env1/bin/python

import time
from selenium.webdriver.common.by import By

################################################################################################################################
def started(driver):
    # PER FUTURI UPDATES
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Live').click()
    time.sleep(3)
################################################################################################################################
