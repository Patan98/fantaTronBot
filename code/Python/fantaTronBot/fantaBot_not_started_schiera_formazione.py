#!/home/YOURUSERNAME/code/Python/venvs/env1/bin/python

import time
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import telegram_text

################################################################################################################################
def fill_formazione(driver, players_list):
    # PER OGNI LISTA GIOCATORE PER RUOLO
    roles = len(players_list)
    for role in range(roles):

        # Si ripete NxN, (PER OGNI GIOCATORE IN LISTA GIOCATORE PER RUOLO)x(GIOCATORE IN LISTA GIOCATORE PER RUOLO)

        # PER OGNI GIOCATORE IN LISTA GIOCATORE PER RUOLO
        for player in players_list[role]:

            # OTTIENI TABELLA GIOCATORI
            try:
                players_table = driver.find_elements(By.CLASS_NAME, 'formation-item')
            except:
                telegram_text.send_to_telegram("Un errore si è verificato durante OTTIENI TABELLA GIOCATORI")
                sys.exit()

            # PER OGNI RECORD (PLAYER) NELLA TABELLA GIOCATORI (PLAYERS)
            for player_table in players_table:
                # INIZIALIZZA GLI ATTRIBUTI DEL GIOCATORE DALLA TABELLA GIOCATORI
                player_match_name = None
                player_match_role = None
                # OTTIENI GLI ATTRIBUTI DEL GIOCATORE DALLA TABELLA GIOCATORI
                try:
                    player_match_name = player_table.find_element(By.CLASS_NAME, 'player-name').text
                    player_match_role = player_table.find_element(By.CLASS_NAME, 'role').text
                except:
                    pass

                # SE IL NOME DEL GIOCATORE DALLA TABELLA GIOCATORI MATCHA CON IL NOME DELL'ATTUALE GIOCATORE IN LISTA GIOCATORE PER RUOLO
                if (player_match_name == player[2]):
                    # CLICCA SUL GIOCATORE DALLA TABELLA GIOCATORI
                    try:
                        player_table.click()
                    except:
                        continue

                    # INIZIALIZZA LE POSIZIONI IN CAMPO LIBERE PER RUOLO
                    players_field = None
                    # IN BASE AL RUOLO DEL GIOCATORE DALLA TABELLA GIOCATORI, OTTIENI LE POSIZIONI IN CAMPO LIBERE PER QUEL RUOLO
                    match player_match_role:
                        case "P":
                            try:
                                players_field = driver.find_elements(By.CSS_SELECTOR, ".formation-item.role-p.empty")
                            except:
                                pass
                        case "D":
                            try:
                                players_field = driver.find_elements(By.CSS_SELECTOR, ".formation-item.role-d.empty")
                            except:
                                pass
                        case "C":
                            try:
                                players_field = driver.find_elements(By.CSS_SELECTOR, ".formation-item.role-c.empty")
                            except:
                                pass
                        case "A":
                            try:
                                players_field = driver.find_elements(By.CSS_SELECTOR, ".formation-item.role-a.empty")
                            except:
                                pass

                    # CLICCA SULLA PRIMA POSIZIONE IN CAMPO LIBERA PER QUEL RUOLO
                    if (len(players_field) > 0):
                        try:
                            players_field[0].click()
                        except:
                            telegram_text.send_to_telegram("Un errore si è verificato durante CLICCA SULLA PRIMA POSIZIONE IN CAMPO LIBERA PER QUEL RUOLO")
                            sys.exit()
                    # SE NON CI SONO PIÙ POSIZIONI IN CAMPO LIBERE CLICCA DI NUOVO SUL GIOCATORE DALLA TABELLA GIOCATORI PER TOGLIERE LA SELEZIONE
                    else:
                        try:
                            player_table.click()
                        except:
                            telegram_text.send_to_telegram("Un errore si è verificato durante SE NON CI SONO PIÙ POSIZIONI IN CAMPO LIBERE...")
                            sys.exit()
                        break

    telegram_text.send_to_telegram("FORMAZIONE SCHIERATA CORRETTAMENTE")
################################################################################################################################
def players_lists_roles_ordered(players_list):
    # INIZIALIZZA LA NUOVA LISTA RUOLI DI LISTE GIOCATORI
    players_list_new = [[], [], [], []]

    # PER OGNI LISTA GIOCATORE PER RUOLO
    roles = len(players_list)
    for role in range(roles):
        for player in players_list[role]:
            if (player[1] == 2):
                player[3] = -1

        # INIZIALIZZA IL GIOCATORE TEMPORANEO E IL CONTATORE TEMPORANEO
        player_last_bigger = [None, None, None, 0]
        player_last_bigger_number = 0

        # NUMERO DI GIOCATORI IN QUEL RUOLO (N)
        players_number = len(players_list[role])

        # PER N VOLTE (NUMERO DI GIOCATORI IN QUEL RUOLO)
        # SCORRI
        # PER OGNI GIOCATORE IN LISTA GIOCATORE PER RUOLO
        # IN SINTESI SI RIPETE NXN
        for N in range(players_number):
            counter = 0
            for player in players_list[role]:
                # VERIFICA IL GIOCATORE FIN ORA PIÙ FORTE
                if (player) and (player[3] >= player_last_bigger[3]):
                    player_last_bigger = player
                    player_last_bigger_number = counter
                counter = counter + 1
            # ALLA FINE AGGIUNGI IL GIOCATORE PIÙ FORTE
            players_list_new[role].append(player_last_bigger)

            # RESETTA IL GIOCATORE TEMPORANEO E IL CONTATORE TEMPORANEO
            players_list[role][player_last_bigger_number] = None
            player_last_bigger = [None, None, None, 0]

    return players_list_new
################################################################################################################################
def players_lists_roles(players_list):
    # INIZIALIZZA LISTA RUOLI DI LISTE GIOCATORI
    players_lists_new = []

    # INIZIALIZZA LE LISTE GIOCATORI PER RUOLO
    players_list_portieri = []
    players_list_difensori = []
    players_list_centrocampisti = []
    players_list_attaccanti = []

    # DIVIDI I GIOCATORI DELLA LISTA GIOCATORI NELLE LISTE DIVISE PER RUOLO GIOCATORI

    # PER OGNI GIOCATORE NELLA LISTA GIOCATORI
    for player in players_list:
        # INIZIALIZZA LISTA GIOCATORE
        player_new = []

        # POPOLA LA LISTA GIOCATORE
        role = player[0]
        player_new.append(role)
        condition = float(player[1])
        player_new.append(condition)
        name = player[2]
        player_new.append(name)
        if (player[3] == '-'):
            fanta_media_voto = 0
        else:
            fanta_media_voto = float(player[3])
        player_new.append(fanta_media_voto)

        # AGGIUNGI LA LISTA GIOCATORE A LISTE GIOCATORI PER RUOLO IN BASE AL RUOLO
        match player[0]:
            case "P":
                players_list_portieri.append(player_new)
            case "D":
                players_list_difensori.append(player_new)
            case "C":
                players_list_centrocampisti.append(player_new)
            case "A":
                players_list_attaccanti.append(player_new)

    # AGGIUNGI LE LISTE GIOCATORI PER RUOLO ALLA LISTA RUOLI DI LISTE GIOCATORI
    players_lists_new.append(players_list_portieri)
    players_lists_new.append(players_list_difensori)
    players_lists_new.append(players_list_centrocampisti)
    players_lists_new.append(players_list_attaccanti)

    return players_lists_new
################################################################################################################################
def players_list_table(driver):
    # INIZIALIZZA LISTA GIOCATORI
    players_list_table = []

    # OTTIENI TABELLA GIOCATORI
    try:
        players = driver.find_elements(By.CLASS_NAME, 'formation-item')
    except:
        telegram_text.send_to_telegram("Un errore si è verificato durante OTTIENI TABELLA GIOCATORI")
        sys.exit()

    # PER OGNI RECORD (PLAYER) NELLA TABELLA GIOCATORI (PLAYERS)
    for player in players:
        try:
            # INIZIALIZZA LISTA GIOCATORE
            player_list = []

            # POPOLA LA LISTA GIOCATORE
            role = player.find_element(By.CLASS_NAME, 'role').text
            player_list.append(role)
            condition = player.get_attribute('data-status')
            player_list.append(condition)
            name = player.find_element(By.CLASS_NAME, 'player-name').text
            player_list.append(name)
            fanta_media_voto = player.find_element(By.CLASS_NAME, 'player-fmv').text
            player_list.append(fanta_media_voto)

            # AGGIUNGI LA LISTA GIOCATORE ALLA LISTA GIOCATORI
            players_list_table.append(player_list)

        except:
            pass

    return players_list_table
################################################################################################################################
def schiera_formazione(driver):
    # SCROLLA FINO A ATTACCANTI (SERVE A TE PER VEDERE)
    try:
        scroller = driver.find_elements(By.CSS_SELECTOR, ".btn.btn-raised.btn-mega.btn-blue.aid-control")
        actions = ActionChains(driver)
        actions.move_to_element(scroller[0]).perform()
    except:
        telegram_text.send_to_telegram("Un errore si è verificato durante SCROLLA FINO A ATTACCANTI\nErrore non critico")

    # SVUOTA LA FORMAZIONE
    try:
        driver.find_element(By.CSS_SELECTOR, 'button[onclick="resetFormation()"]').click()
        time.sleep(3)
    except:
        telegram_text.send_to_telegram("Un errore si è verificato durante SVUOTA IL CAMPO")
        sys.exit()

    # OTTIENI LISTA GIOCATORI
    players_list = players_list_table(driver)
    # OTTIENI LISTA RUOLI DI LISTE GIOCATORI DA LISTA GIOCATORI
    players_list = players_lists_roles(players_list)
    # ORDINA LA LISTA RUOLI DI LISTE GIOCATORI IN ORDINE DECRESCENTE PER PUNTEGGIO
    players_list = players_lists_roles_ordered(players_list)

    # POPOLA LA FORMAZIONE CON LA LISTA RUOLI DI LISTE GIOCATORI
    fill_formazione(driver, players_list)

    driver.find_element(By.CSS_SELECTOR, 'button[onclick="saveFormation()"]').click()
################################################################################################################################
