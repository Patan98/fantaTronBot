# FantaTron Bot

<p align="center">
  <img src="https://github.com/user-attachments/assets/b512b5a5-d089-4b0b-aae8-48a30ab4972f">
</p>

Questo è un piccolo software in Python con Selenium per l'automatizzazione delle attività di routine di Leghe Fantacalcio, con sistema di notifiche su bot telegram. <br />
Software a scopo non commerciale e tutti i dati e i contenuti utilizzati sono di proprietà dei rispettivi titolari, il bot non intende violare alcun copyright o diritto di terze parti e/o di Quadronica s.r.l. <br />
Tested on Debian 12 / 6.1.0-23-amd64. <br />

## Idea
<div class="row" >
<img height="200" width="200" alt="Python" src="https://github.com/user-attachments/assets/32eaba02-6799-4ba1-a1bb-c34e3b87e8b4">
<img height="200" width="200" alt="Selenium" src="https://github.com/user-attachments/assets/274f5ff8-c77a-4264-afc0-ad7f243c617c">
<img height="200" width="200" alt="Telegram" src="https://github.com/user-attachments/assets/3e5e6669-a905-4f0a-b3fe-27182e7618e0">
</div>

L'obiettivo del software è di automatizzare lo schieramento della formazione, evitando così di dimenticare di farlo manualmente. <br />
I giocatori vengono divisi in liste per ruolo ordinate per 'media fanta voto' in ordine decrescente, e poi schierati in campo uno ad uno. <br />
I giocatori infortunati ricevono priorità minima (-1) e i giocatori che ancora non hanno una 'media fanta voto' ricevono priorità bassa (0). <br />

## Requirements
È necessario installare python3: <br />

    sudo apt install python3
    pip install virtualenv

E successivamente nel venv creato installare le dipendenze da requirements.txt: <br />

    Requests==2.32.3
    selenium==4.25.0

## Install
* Prima di tutto copiare la cartella code nella propria home. <br />

* Creare un virtual environment per Python e installare le dipendenze: <br />
  
      python3 -m venv /home/$(whoami)/code/Python/venvs/env1
      source /home/$(whoami)/code/Python/venvs/env1/bin/activate
      pip install -r ./requirements.txt

* Sostituire il PATH venv del progetto con il vostro PATH venv appena creato <br />

      cd code/Python/fantaTronBot/
      for filename in *; do sed -i -e 's/YOURUSERNAME/'$(whoami)'/g' "$filename"; done
      cd

* Sostituire YOUREMAIL e YOURPASSWORD in fantaBot.by con le proprie credenziali. <br />
Sostituire YOURLEAGUE in fantaBot_not_started.py con il nome della propria lega <br />
Sostituire YOURTEAM in fantaBot_not_started_check.py con il nome della propria squadra <br />

* OPZIONALE MA CONSIGLIATO: Creare un bot telegram e ottenerne apiKey e chatId (consultare una guida esterna). <br />
  Sostituire le le credenziali YOURAPITOKEN e YOURCHATID nel file telegram_text.py con quelle ottenute alla creazione del bot.

## Usage
Il modo di utilizzo principale è reiterare l'esecuzione ogni ora con cron. <br />
Va da se che serve un pc / server / raspberryPi sempre acceso per far funzionare sempre lo script. <br />
In alternatica è possibile anche eseguire lo script manualmente quando desiderato. <br />

    crontab -e

Aggiungici sostituendo YOURUSERNAME con il tuo username:

    0 * * * * ./home/YOURUSERNAME/code/Python/fantaTronBot/fantaBot.py


## TODO
TODO: Aggiungere funzionalità di scelta dinamica del modulo di gioco in base ai giocatori disponibili e ai punti di forza <br />
  ES: <br />
  - Se hai tanti attaccanti forti e pochi centrocampisti forti punta su un modulo sbilanciato in attacco <br />
  - Se hai tutti i difensori infortunati punta su un modulo che abbia il minimo numero di difensori <br />
  
TODO: Aggiungere supporto per la scelta pesata dei giocatori, non basando tutto solo sulla 'media fanta voto' ma anche sulla probabilità di successo del giocatore in quella giornata <br />
  ES: <br />
  - A parità (o quasi) di media fanta voto, Tizio gioca contro la squadra prima in classifica e Caio gioca contro la squadra ultima in classifica, scegli Caio <br />
  - Minimo peso da dare anche se il giocatore in questione gioca in casa o in trasferta <br />
  
TODO: Aggiungere supporto allo switch. <br />

TODO: Aggiungere supporto al modificatore di difesa (se risulta attivo bisogna scegliere se conviene sfruttarlo e schierare 4 difensori o lasciare perdere e puntare su centro e attacco). <br />

TODO: Aggiungere invio di notifica di inizio giornata imminente, circa un ora prima dell'inizio della giornata. <br />

![Card](https://github.com/user-attachments/assets/8082c544-cf53-4008-8f1f-dd98b1367bb4)
