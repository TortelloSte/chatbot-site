import sqlite3
import os

def creare_database_se_non_esiste(nome_database):
    """
    Crea un database SQLite se non esiste già.

    Args:
        nome_database (str): Il nome del database da creare.
    """
    try:
        if not os.path.exists(nome_database):
            with sqlite3.connect(nome_database) as conn:
                cursor = conn.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS preventivi (email TEXT)''')
            print(f"Database '{nome_database}' creato con successo.")
        else:
            print(f"Il database '{nome_database}' esiste già.")
    except sqlite3.Error as e:
        print(f"Errore durante la creazione del database: {e}")

def inserire_dati_preventivo(email, nome_database='preventivi.db'):
    """
    Inserisce dati di preventivo nel database.

    Args:
        email (str): L'email da inserire nel database.
        nome_database (str, optional): Il nome del database dei preventivi. Default è 'preventivi.db'.
    """
    try:
        with sqlite3.connect(nome_database) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO preventivi (email) VALUES (?)", (email,))
        print("Dati inseriti correttamente nel database dei preventivi.")
    except sqlite3.Error as e:
        print(f"Errore durante l'inserimento dei dati: {e}")

def inserire_dati_consiglio(nome, cognome, email, oggetto, messaggio, nome_database='consigli.db'):
    """
    Inserisce dati di consiglio nel database.

    Args:
        nome (str): Nome dell'utente.
        cognome (str): Cognome dell'utente.
        email (str): Email dell'utente.
        oggetto (str): Oggetto del messaggio.
        messaggio (str): Testo del messaggio.
        nome_database (str, optional): Il nome del database dei consigli. Default è 'consigli.db'.
    """
    try:
        if not os.path.exists(nome_database):
            creare_tabella_consiglio(nome_database)
        
        with sqlite3.connect(nome_database) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO consigli (nome, cognome, email, oggetto, messaggio) VALUES (?, ?, ?, ?, ?)",
                           (nome, cognome, email, oggetto, messaggio))
        print("Dati inseriti correttamente nel database dei consigli.")
    except sqlite3.Error as e:
        print(f"Errore durante l'inserimento dei dati: {e}")

def creare_tabella_consiglio(nome_database):
    """
    Crea la tabella dei consigli nel database se non esiste già.

    Args:
        nome_database (str): Il nome del database in cui creare la tabella.
    """
    try:
        with sqlite3.connect(nome_database) as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS consigli (
                                id INTEGER PRIMARY KEY,
                                nome TEXT,
                                cognome TEXT,
                                email TEXT,
                                oggetto TEXT,
                                messaggio TEXT
                            )''')
        print(f"Tabella 'consigli' creata con successo nel database '{nome_database}'.")
    except sqlite3.Error as e:
        print(f"Errore durante la creazione della tabella: {e}")
