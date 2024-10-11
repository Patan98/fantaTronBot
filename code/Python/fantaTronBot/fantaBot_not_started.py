#!/home/YOURUSERNAME/code/Python/venvs/env1/bin/python

import time
import sys
from selenium.webdriver.common.by import By

import fantaBot_not_started_schiera_formazione
import fantaBot_not_started_check

import telegram_text

################################################################################################################################
def not_started(driver):
    # CLICK SU FORMAZIONI
    try:
        driver.find_element(By.CSS_SELECTOR, 'a[href="https://leghe.fantacalcio.it/YOURLEAGUE/formazioni"]').click()
        time.sleep(3)
    except:
        telegram_text.send_to_telegram("Un errore si è verificato durante CLICK SU FORMAZIONI")
        sys.exit()

    # CHECK SE LA FORMAZIONE È STATA SCHIERATA
    fantaBot_not_started_check.check(driver)

    # CLICK SU SCHIERA FORMAZIONE
    try:
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Schiera Formazione').click()
        time.sleep(3)
    except:
        telegram_text.send_to_telegram("Un errore si è verificato durante CLICK SU SCHIERA FORMAZIONE")
        sys.exit()

    # SCHIERA FORMAZIONE
    fantaBot_not_started_schiera_formazione.schiera_formazione(driver)
################################################################################################################################
