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


while(True):

    t.printMenu()

    t.loadDictionary("filename.txt")

    txtIn = input()

    acceptable_inputs = {1, 2, 3, 4, 5}

    if txtIn not in acceptable_inputs:
        raise ValueError

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        txtIn = input()
        t.handleAdd(txtIn)
    if int(txtIn) == 2:
        print("Ok, quale parola devo cercare?")
        txtIn = input()
        t.handleTranslate(txtIn)
    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare (wildcard)?")
        txtIn = input()
        t.handleWildCard(txtIn)
    if int(txtIn) == 4:
        print("Ok, termino programma.")
        break

