import os
import sqlite3
from datetime import datetime
from doctorSte.utils import *
 
def check_data(data):
    try: 
        dataValore = datetime.strptime(data,'%d/%m/%Y')
        return True
    except ValueError:
        return False


def fare_domanda(domanda, opzioni):
    print(domanda)
    for i, opzione in enumerate(opzioni, 1):
        print(f"{i}. {opzione}")
 
    while True:
        scelta = input("Inserisci il numero corrispondente alla tua risposta: ")
        try:
            scelta = int(scelta)
            if 1 <= scelta <= len(opzioni):
                if domanda=="Di quale classe vuoi che sia il servizio?" and scelta == 3:
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
        ("Di quale servizio hai bisogno? ", ["Servizio A", "Servizio B", "Servizio C","Altro"]),
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
 
creare_database_se_non_esiste('preventivi.db')
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

# una volta che queste funzionano implemantare le funzioni che gestiscono la creazione del pdf e il file csv
# il file csv si trova dentro alla cartella doctorSte, che fa da libreria quindi se si importa la libreria viene di default preso