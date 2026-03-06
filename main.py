"""
Realizzare in linguaggio Python una semplice applicazione che funga da traduttore di parole aliene.
Deve essere possibile sia l’aggiunta di nuove parole che la ricerca di quelle esistenti.
L’applicazione dovrà essere dotata di un menù stampato su terminale, tramite il quale l’utente può
selezionare la funzionalità richiesta digitando il numero corrispondente.

Le funzionalità del programma richieste sono:
- Leggere un dizionario iniziale dal file “dictionary.txt”
- Inserire una nuova parola e la relativa traduzione secondo il seguente pattern:
                            <parola aliena> <traduzione> (separate da uno spazio)
  Alla pressione del tasto invio, la parola e la sua traduzione verranno aggiunte al dizionario.
- Cercare la traduzione di una parola esistente inserendo <parola aliena> e facendo pressione sul tasto
invio. La traduzione verrà visualizzata sul terminale.

Implementare i controlli per eventuali errori sull’input: gli unici caratteri ammessi sono [a-zA-Z] (ossia solo
le lettere alfabetiche, siano essere maiuscole o minuscole), ma la ricerca deve essere case insensitive. Si
suggerisce di convertire tutto il testo ricevuto in minuscolo prima di elaborarlo.
"""

import translator as tr

t = tr.Translator()

t.loadDictionary("dictionary.txt")

running = True

while running:

    t.printMenu()

    txtIn = input()

    input_accettabili = {"1", "2", "3", "4", "5"}

    # 1. Aggiungi nuova parola
    # 2. Cerca una traduzione
    # 3. Cerca con wildcard
    # 4. Stampa dizionario corrente
    # 5. Exit

    if txtIn not in input_accettabili:
        print("Scelta non valida, riprova.")
        continue

    if txtIn == "1":
        print("Ok, quale parola devo aggiungere?")
        txtIn = input()
        t.handleAdd(txtIn)
    elif txtIn == "2":
        print("Ok, quale parola devo cercare?")
        txtIn = input()
        t.handleTranslate(txtIn)
    elif txtIn == "3":
        print("Ok, quale parola devo cercare (wildcard)?")
        txtIn = input()
        t.handleWildCard(txtIn)
    elif txtIn == "4":
        print("Ok, dove vuoi salvare il dizionario corrente? Premi Invio per 'output.txt'.")
        txtIn = input()
        if txtIn:
            t.handlePrint(txtIn)
        else:
            t.handlePrint()
    elif txtIn == "5":
        print("Ok, termino programma.")
        running = False