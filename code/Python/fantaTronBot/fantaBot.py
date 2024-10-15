#!/home/YOURUSERNAME/code/Python/venvs/env1/bin/python

import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

import fantaBot_not_started
import fantaBot_started

import telegram_text

################################################################################################################################
# ██ ███    ██ ██ ████████
# ██ ████   ██ ██    ██
# ██ ██ ██  ██ ██    ██
# ██ ██  ██ ██ ██    ██
# ██ ██   ████ ██    ██
def fantabot_init():
    driver=webdriver.Chrome()

    driver.get("https://leghe.fantacalcio.it")
    driver.maximize_window()

    # COOKIE
    try:
        driver.find_element(By.ID, 'pt-accept-all').click()
        time.sleep(3)
    # NO COOKIE
    except:
        telegram_text.send_to_telegram("Un errore si è verificato durante COOKIE\nErrore non critico")

    # CLICK SU LOGIN PAGE
    try:
        driver.find_element(By.CSS_SELECTOR,".hidden-logged.btn.btn-primary.btn-sm.btn-raised.navbar-btn.navbar-right.mw-auto").click()
        time.sleep(3)
    except:
        telegram_text.send_to_telegram("Un errore si è verificato durante CLICK SU LOGIN PAGE")
        sys.exit()

    # COMPILA IL LOGIN
    try:
        driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Username"]').send_keys("YOUREMAIL")
        driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]').send_keys("YOURPASSWORD")
        time.sleep(3)
    except:
        telegram_text.send_to_telegram("Un errore si è verificato durante COMPILA IL LOGIN")
        sys.exit()

    # CLICK SU LOGIN
    try:
        driver.find_element(By.XPATH,'/html/body/app-root/layout-auth/div[1]/div/view-login/nz-card/div[2]/form/button').click()
        time.sleep(5)
    except:
        telegram_text.send_to_telegram("Un errore si è verificato durante CLICK SU LOGIN")
        sys.exit()

    started = 0

    try:
        # GIORNATA NON ANCORA INIZIATA
        try:
            test = driver.find_element(By.PARTIAL_LINK_TEXT, 'Schiera Formazione')
            started = 0
        # GIORNATA INIZIATA
        except:
            test = driver.find_element(By.PARTIAL_LINK_TEXT, 'Live')
            started = 1
    except:
        telegram_text.send_to_telegram("Un errore si è verificato durante la scelta di GIORNATA INIZIATA / GIORNATA NON ANCORA INIZIATA")
        sys.exit()

    if (started == 0):
        fantaBot_not_started.not_started(driver)
    elif (started == 1):
        fantaBot_started.started(driver)

    driver.close()
################################################################################################################################
# ███    ███  █████  ██ ███    ██
# ████  ████ ██   ██ ██ ████   ██
# ██ ████ ██ ███████ ██ ██ ██  ██
# ██  ██  ██ ██   ██ ██ ██  ██ ██
# ██      ██ ██   ██ ██ ██   ████
def main():
    telegram_text.send_to_telegram("FANTABOT IN FUNZIONE 🤖")

    fantabot_init()
################################################################################################################################

main()

# draggable = driver.find_element(By.ID, "draggable")
# droppable = driver.find_element(By.ID, "droppable")
# ActionChains(driver).drag_and_drop(draggable, droppable).perform()

# TODO: 3) GET MODULO IN USO
# TODO: 4) VERIFICA SE ABBASTANZA GIOCATORI PER OGNI RUOLO DA COPRIRE CAMPO E PANCHINA (PANCHINA SEMPRE 1-3-3-2) (NO INFORTUNI, ROSSI O VENDUTI FUORI ITALIA)
# TODO: 5) SE I GIOCATORI NON SONO ABBASTANZA MANDA UN ALLARME TELEGRAM (IL MODULO VA CAMBIATO A MANO CON UNO ADEGUATO)
