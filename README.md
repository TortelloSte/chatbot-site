# chatbot-site

## Chatbot per Generazione di Preventivi

Questo repository è dedicato alla definizione dell'ambiente di controllo e creazione del nostro chatbot predefinito, progettato per la generazione e il calcolo dei preventivi.

L'ispirazione per questo progetto nasce dall'osservazione di come viene utilizzato un chatbot con risposte predefinite su questo [Link](https://prontopro.it/quote/installazione-porta-blindata/112655/2)
Tuttavia, l'obiettivo è di andare oltre tale modello, arricchendolo con funzionalità avanzate come la generazione automatica di preventivi in formato PDF.


### TODO:

   1. creazione di una libreria strutturata ad hoc per andare a definire tutto il progetto
   2. creazione della API per questo progetto cosi da riuscire a sfruttarlo dentro a un sito web
   3. creazione di un sito web per questo progetto
   4. creazione del database per riuscire a inserire i dati

## come utilizzare questo codice:
   - installare la libreria doctorSte per utilizzare le funzioni
   - spostarsi dentro alla cartella doctorSte
```bash
      cd ./doctorSte/
```
   - installare la libreria doctorSte
   
```bash
      pip install .
```



# --------------------------------
entro mercoledi sera terminare le modifiche a questo codice, per renderlo funzionante, con database, registrazione utente, modifica delle funzioni e creazione della libreria completa

- modifica delle funzioni per renderle ottimizzate, creare l'api per renderlo accessibile online
- fare i test e inserire il file dei test all'interno della repository!

(sarebbe interessante usare helm e le kubernetes per andare a strutturare un POD che possieda al suo interno tutto questo)