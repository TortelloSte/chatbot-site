from doctorSte.utils import *

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
 
if __name__ == "__main__":
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


