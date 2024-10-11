# FantaTron Bot

<p align="center">
  <img src="https://github.com/user-attachments/assets/b512b5a5-d089-4b0b-aae8-48a30ab4972f">
</p>

Questo è un piccolo software in Python con Selenium per l'automatizzazione delle attività di routine di Leghe Fantacalcio.
Software a scopo non commerciale e tutti i dati e i contenuti utilizzati sono di proprietà dei rispettivi titolari, il bot non intende violare alcun copyright o diritto di terze parti e/o di Quadronica s.r.l.

## Idea
L'obiettivo del software è di automatizzare lo schieramento della formazione, aiutare gli utenti a schierare automaticamente la formazione a ogni giornata, evitando così di dimenticare di farlo manualmente.
I giocatori vengono divisi in liste per ruolo ordinate per 'media fanta voto' in ordine decrescente, e poi schierati in campo uno ad uno.
I giocatori infortunati ricevono priorità minima (-1) e i giocatori che ancora non hanno una 'media fanta voto' ricevono priorità bassa (0).

TODO: Aggiungere funzionalità di scelta dinamica del modulo di gioco in base ai giocatori disponibili e ai punti di forza 
  ES:
  - Se hai tanti attaccanti forti e pochi centrocampisti forti punta su un modulo sbilanciato in attacco
  - Se hai tutti i difensori infortunati punta su un modulo che abbia il minimo numero di difensori
TODO: Aggiungere supporto per la scelta pesata dei giocatori, non basando tutto solo sulla 'media fanta voto' ma anche sulla probabilità di successo del giocatore in quella giornata
  ES:
  - A parità (o quasi) di media fanta voto, Tizio gioca contro la squadra prima in classifica e Caio gioca contro la squadra ultima in classifica, scegli Caio
  - Minimo peso da dare anche se il giocatore in questione gioca in casa o in trasferta
TODO: Aggiungere supporto allo switch
TODO: Aggiungere supporto al modificatore di difesa (se risulta attivo bisogna scegliere se conviene sfruttarlo e schierare 4 difensori o lasciare perdere e puntare su centro e attacco)

![Card](https://github.com/user-attachments/assets/8082c544-cf53-4008-8f1f-dd98b1367bb4)

## Requirements

## Usage

## Install

