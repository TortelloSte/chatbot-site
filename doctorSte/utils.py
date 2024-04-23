import sqlite3
import os
from datetime import datetime

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

def check_data(data):
    if not data:
        return False
    
    try: 
        datetime.strptime(data,'%d/%m/%Y')
        return True
    except ValueError:
        return False


def fare_domanda(domanda, opzioni):
    print(domanda)
    for i, opzione in enumerate(opzioni, 1):
        print(f"{i}. {opzione}")
 
    while True:
        scelta = input("Inserisci il numero corrispondente alla tua risposta: ") # sistemiamo la domanda per la selezione?
        try:
            scelta = int(scelta)
            if 1 <= scelta <= len(opzioni):
                if domanda == "Di quale prodotto necessiti un preventivo?":
                    if scelta == 1 or scelta == 3:
                        materiali = ["Legno","Metallo","Acciaio"]
                    elif scelta == 2 :
                        materiali = ["Legno di noce","Legno di pino", "Legno di abete"]  
# da sistemare questa funzione, if non connesso a nulla, non prende il file csv?
                    scelta_materiale = int(input("Inserisci di quale materiale vuoi sia l'inferiata"))  # mancava uno spazio
                    if 1 <= scelta_materiale <= len(materiali):
                        #controllo_prezzo_db(materiali[scelta_materiale])
                        #pensavo di mettere qui una funzione che restituisce il prezzo in modo tale che nel passaggio successivo possa essere utilizzato per calcolare la spesa totale
                        quantita = int(input("Selezionare la quantità del prodotto: ")) 
                        #print("Spesa: %5,2f" % (quantita * il risultato del controllo prezzo))

                elif domanda=="Di quale classe vuoi che sia il servizio?" and scelta == 3:
                    ricevere_consiglio()
                elif domanda=="Quando hai bisogno del servizio?" and scelta == 1:
                    data = input("Inserisci una data nel formato gg/mm/aaaa: ")
                    while not check_data(data):
                        print("Data non valida")
                        data = input("Inserisci una data nel formato gg/mm/aaaa: ")
                return opzioni[scelta - 1]
            else:
                print("Inserisci un numero valido.")
        except ValueError:
            print("Inserisci un numero valido.")
 
def fare_preventivo():
    print("Bene, iniziamo a fare il preventivo.")
 
    # Domande relative al preventivo
    domande_preventivo = [
        ("Quanto spesso utilizzi il servizio? ", ["Raramente", "Occasionalmente", "Spesso"]),
        ("Di quale prodotto necessiti un preventivo?", ["Inferiata", "Portone", "Cancello"]),
        ("Di quale classe vuoi che sia il servizio?",["Classe 1","Classe 2","Vorrei il consiglio di un professionista", "Altro"]),
        ("Indica dove hai bisogno del servizio",["Milano","Roma","Ancona","Firenze","Napoli"]),
        ("Quando hai bisogno del servizio?",["Ho bisogno del servizio in una data specifica","Tra un mese","Tra un anno"])
    ]
 
    risposte_preventivo = []
 
    for domanda, opzioni in domande_preventivo:
        risposta = fare_domanda(domanda, opzioni)
        risposte_preventivo.append(risposta)
 
    email = input("Inserisci la tua email per restare in contatto: ")
    inserire_dati_preventivo(email)
    print("Grazie per aver fornito le informazioni. Ti contatteremo presto.")
 
def ricevere_consiglio():
    print("Va bene, posso darti un consiglio.")
 
    # Domande relative al consiglio
    nome = input("Inserisci il tuo nome: ")
    cognome = input("Inserisci il tuo cognome: ")
    email = input("Inserisci la tua email: ")
    oggetto = input("Inserisci l'oggetto del messaggio: ")
    messaggio = input("Inserisci il tuo messaggio: ")
 
    inserire_dati_consiglio(nome, cognome, email, oggetto, messaggio)
    print("Grazie per aver condiviso il tuo problema. Ti contatteremo presto con un consiglio.")