#!/home/YOURUSERNAME/code/Python/venvs/env1/bin/python

import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import telegram_text

################################################################################################################################
def check(driver):
    # OTTIENI TABELLA PARTITE
    try:
        tables = driver.find_elements(By.CSS_SELECTOR, ".match-details.card.wrapped")
    except:
        telegram_text.send_to_telegram("Un errore si è verificato durante OTTIENI TABELLA GIOCATORI")
        sys.exit()

    # PER OGNI TABELLA PARTITE, RIGA PER RIGA, COLONNA PER COLONNA, CERCA IL MIO TEAM
    # SE TROVI IL MIO TEAM, LA MIA FORMAZIONE (O MESSAGGIO DI FORMAZIONE NON SCHIERATA) SARÀ DUE CELLE DOPO
    # ES 1:             ES 2:
    # ---------         ---------
    # | X | 1 |         |   | X |
    # ---------         ---------
    # | 2 |   |         | 1 | 2 |
    # ---------         ---------
    for table in tables:
        # PER OGNI TABELLA SCROLLA FINO ALLA TABELLA (SERVE A ATTIVARE IL JS)
        actions = ActionChains(driver)
        actions.move_to_element(table).perform()

        counter_celle = 0

        rows = table.find_elements(By.CSS_SELECTOR, "._row")
        for row in rows:

            columns = row.find_elements(By.CSS_SELECTOR, "._col-xs-6")
            for column in columns:

                if (counter_celle > 0):
                    counter_celle = counter_celle + 1

                if (counter_celle == 3):
                    telegram_text.send_to_telegram("FORMAZIONE NON SCHIERATA, INIZIO A SCHIERARE")

                if (column.text == 'YOURTEAM'):
                    counter_celle = counter_celle + 1

        time.sleep(1)

    # SCROLLA ALL'INIZIO (SERVE A ATTIVARE IL JS)
    driver.execute_script("window.scrollTo(0, 0)")
################################################################################################################################
