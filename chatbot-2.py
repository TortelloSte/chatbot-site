from doctorSte.utils import *


if __name__ == "__main__":
    # migliorare questa condizione, per renderlo un minimo decente e non semplicemente una funzione che viene eseguita, mettere un controllo
    # Verifica e creazione del database preventivi.db 
    creare_database_se_non_esiste('preventivi.db')
    
    # Inizio del flusso del programma
    risposta_iniziale = fare_domanda("Vuoi fare un preventivo?", ["Si", "No", "Ho bisogno di un consiglio"])
    
    if risposta_iniziale == "Si":
        fare_preventivo()
    elif risposta_iniziale == "No": # sistemare questa condizione per renderla efficiente e non solo un elif con tutti i dati dentro
        print("Nessun problema!")
        email = input("Inserisci la tua email per restare in contatto: ")
        inserire_dati_preventivo(email)
        print("Grazie per aver fornito le informazioni. Ti contatteremo presto.")
    else:
        ricevere_consiglio() # controllare la funzione per andare a capire come andare a sistemare il procedimento del consiglio