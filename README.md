# Progetto Cap Query Remoto(MySQL)

Il progetto è la trasformazione del corrispondente progetto locale, che appoggia il database su SQLite3. 
In questa versione il progetto può servire più utenti appoggiando la base dati su un server MySQL, raggiungibile sia dalla LAN, che dalla WAN, a seconda della configurazione scelta da chi utilizza il progetto.

## Scelta dell'ambiente

Il pacchetto è stato sviluppato anni fa in Python 2 e convertito in questi giorni in Python 3.
Come interfaccia, ai tempi, fu scelta una interfaccia testuale pura, perché l'azienda in cui veniva usato, aveva i più disparati sistemi operativi in uso: dal dos sino al windows 7 passato da Osx e Linux. 

Creare un'interfaccia grafica valida per tutti avrebbe richiesto un lavoro eccessivo per il risultato che si voleva ottenere, per cui la scelta è caduta sul testuale puro per poter essere usato da tutti senza problemi di librerie e metodologie che chiedessero fork per sistema.

## Moduli necessari. 

Diversi, ma tutti preinstallati con Python3. L'unico modulo che va installato, se non si usa l'ambiente virtuale predisposto via *venv* è: **pymysql**. L'installazione si ottiene con l'esecuzione del seguente codice:
`pip install pymysql`. Se invece si attiva l'ambiente virtuale al primo lancio eseguire:

```
cd DirDelProgetto
source bin/activate
pip install -r requirements.txt        ## installazione del moduli necessari localmente per il progetto
./CapQuery.Remote
```
 
Terminato il programma eseguire `deactivate` per uscire dall'ambiente virtuale

Nel caso **non** si usi l'ambiente virtuale, e **non** sia già installato il modulo *pymysql*, il programma notifica l'assenza all'utente fornendo le istruzioni per installarlo.

Nella cartella esiste il file *dump* per poter caricare la tavola CAP con i dati necessari a far funzionare le query.

## Variabili: da configurare e non:

1. **User**: nome utente per l'accesso al database: viene popolata dalla funzione  **GetLogin()**
2. **Password**: password per l'accesso al database: viene popolata dalla funzione  **GetLogin()**
3. **Host**: macchina su cui è stato caricato il database CAP - **deve** essere popolata prima dell'avvio
4. **DbName**: nome del database creato in cui è appoggiata la tabella CAP - **deve** essere popolata prima dell'avvio

## Uso

All'avvio vengono chiesti UserName e Password per la connessine al database MySQL. Sono gestiti errori sia per credenziali errate che per impossibilità di collegare il database. 
Se il collegamento va a buon fine compare un menu di quattro voci:

        (1) Cerca Per Cap
        (2) Cerca Per Comune
        (3) Cerca Per Provincia e/o Comune
        (4) Esci
        
        Seleziona voce menu [ 1 - 4 ] 

### Voce del menu 1
Viene richiesto il CAP e si ottiene il record corrispondente.
### Voce del menu 2
Digitare nome del comune, o sotto stringa del nome, e si ottengono i record corrispondenti.
### Voce del menu 3
Digitare la sigla del comune, o dare invio a vuoto;
Digitare nome del comune, o sotto stringa del nome, e si ottengono i record corrispondenti.
### Voce del menu 4
Uscita dal programma.

**NOTE** 
* tutti gli input sono ***case insensitive***
* nelle visualizzazioni, visto che possono essere elencate più di una pagina, viene richiesto di inserire un codice specifico per uscire dalla schermata: questo permette di poter scorrere all'indietro la pagina in cui il numero di righe superi l'altezza della schermata del terminale.

---
Ultimo aggiornamento, verso python 3, effettuato il 13/02/2020# CapQuery.Remote
