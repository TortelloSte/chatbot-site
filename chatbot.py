import os
import sqlite3
 
def creare_database_se_non_esiste(nome_database):
    if not os.path.exists(nome_database):
        conn = sqlite3.connect(nome_database)
        conn.execute('''CREATE TABLE preventivi (email TEXT)''')
        conn.close()
 
def inserire_dati_preventivo(email):
    conn = sqlite3.connect('preventivi.db')
    c = conn.cursor()
    c.execute("INSERT INTO preventivi (email) VALUES (?)", (email,))
    conn.commit()
    conn.close()
 
def inserire_dati_consiglio(nome, cognome, email, oggetto, messaggio):
    conn = sqlite3.connect('consigli.db')
    c = conn.cursor()
    c.execute("INSERT INTO consigli (nome, cognome, email, oggetto, messaggio) VALUES (?, ?, ?, ?, ?)", (nome, cognome, email, oggetto, messaggio))
    conn.commit()
    conn.close()
 
def fare_domanda(domanda, opzioni):
    print(domanda)
    for i, opzione in enumerate(opzioni, 1):
        print(f"{i}. {opzione}")
 
    while True:
        scelta = input("Inserisci il numero corrispondente alla tua risposta: ")
        try:
            scelta = int(scelta)
            if 1 <= scelta <= len(opzioni):
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
        ("Di quale servizio hai bisogno? ", ["Servizio A", "Servizio B", "Servizio C"])
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
 
# Verifica e creazione del database preventivi.db
creare_database_se_non_esiste('preventivi.db')
 
# Inizio del flusso del programma
risposta_iniziale = fare_domanda("Vuoi fare un preventivo?", ["Si", "No", "Ho bisogno di un consiglio"])
 
if risposta_iniziale == "Si":
    fare_preventivo()
elif risposta_iniziale == "No":
    print("Nessun problema!")
    email = input("Inserisci la tua email per restare in contatto: ")
    inserire_dati_preventivo(email)
    print("Grazie per aver fornito le informazioni. Ti contatteremo presto.")
else:
    ricevere_consiglio()