```markdown
# Telegram Bot per Promozioni

Questo programma Python consente di inviare messaggi promozionali riguardanti prodotti tramite un bot di Telegram. Il bot genera messaggi con contenuti dinamici basati sull'input dell'utente e risponde solo agli utenti autorizzati, inviando i messaggi a una chat di gruppo specificata.

## Caratteristiche

- Generazione casuale di messaggi promozionali.
- Risposta solo da parte di utenti autorizzati.
- Invia messaggi a un gruppo Telegram specifico.
- Semplice da configurare e utilizzare.

## Requisiti

- Python 3.x
- `python-telegram-bot` library

## Come Eseguire il Programma in un IDE

Segui questi passaggi per eseguire il programma nel tuo IDE Python preferito (come PyCharm, VSCode, o altri):

### 1. Clona o Scarica il Repository

Clona o scarica questo repository sul tuo computer locale:

```bash
git clone https://github.com/nicofontani/Python_Projects/Telegram_Bot_Promotions_v1.0.0
```

Oppure, se preferisci, puoi scaricare il file ZIP da GitHub ed estrarlo in una directory.

### 2. Installa Python

Assicurati di avere Python 3.x installato sul tuo computer. Se non hai Python, scaricalo e installalo dal sito ufficiale di Python: [python.org/downloads](https://www.python.org/downloads/)

### 3. Installa le Dipendenze Necessarie

Per installare la libreria `python-telegram-bot`, usa il seguente comando:

```bash
pip install python-telegram-bot
```

### 4. Apri il Progetto nel Tuo IDE

Apri la cartella del progetto nel tuo IDE Python scelto.

### 5. Esegui il Programma

Trova lo script `telegram_bot_promotions.py` nel progetto e eseguilo direttamente dal tuo IDE. Il bot inizierà a funzionare e potrai iniziare a inviare messaggi promozionali.

## Come Creare un File Eseguibile (.exe) Usando PyInstaller

Per eseguire il programma su una macchina Windows senza richiedere Python, puoi creare un file eseguibile (`.exe`) utilizzando **PyInstaller**.

### 1. Installa PyInstaller

Apri il terminale (prompt dei comandi o PowerShell) e installa PyInstaller usando `pip`:

```bash
pip install pyinstaller
```

### 2. Crea l'Eseguibile

Dopo aver installato PyInstaller, naviga nella directory del progetto dove si trova il tuo script Python. Ad esempio:

```bash
cd path/to/your/project
```

Poi, usa PyInstaller per creare il file `.exe` eseguendo il seguente comando:

```bash
pyinstaller --onefile --windowed --icon=your_icon.ico telegram_bot_promotions.py
```

Spiegazione delle opzioni:
- `--onefile`: Pacchetta tutto in un singolo file `.exe`.
- `--windowed`: Impedisce l'apertura di una finestra del terminale insieme all'applicazione (utile per le applicazioni GUI).
- `--icon=your_icon.ico`: Aggiunge un'icona personalizzata al file `.exe` (sostituisci `your_icon.ico` con il percorso del tuo file icona).

### 3. Trova l'Eseguibile

Dopo aver eseguito il comando sopra, PyInstaller creerà diverse cartelle nella tua directory di progetto. Il file `.exe` sarà situato nella cartella `dist`.

Ad esempio:

```
dist/
  telegram_bot_promotions.exe
```

### 4. Esegui l'Eseguibile

Ora puoi eseguire il file `telegram_bot_promotions.exe` direttamente su una macchina Windows senza bisogno di Python installato. Basta fare doppio clic sul file `.exe` per aprire l'applicazione.

### 5. Distribuisci l'Eseguibile

Per condividere il programma, puoi distribuire il file `telegram_bot_promotions.exe` ad altri. Saranno in grado di eseguire il programma senza dover installare Python.
```