from dictionary import Dictionary


class Translator:

    def __init__(self):
        self.diz = Dictionary()

    def printMenu(self):
        print("-"*30)
        print(" "*3+"Translator Alien-Italian"+" "*3)
        print("-"*30)
        print("1. Aggiungi una nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa dizionario corrente")
        print("5. Exit")
        print("-" * 30)

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(dict, "r", encoding="utf-8") as fin:
            for riga in fin:
                campi = riga.split()
                if len(campi) >= 2:
                    parola_aliena = campi[0].lower()
                    traduzione = campi[1].lower()
                    self.diz.addWord(parola_aliena, traduzione)

    def handleAdd(self, entry):
        # entry is a string <parola_aliena> <traduzione1 traduzione2 ...>
        entry = entry.lower()
        campi = entry.split()

        if len(campi) < 2:
            print("Errore: formato entry non valido.\nInserire: <parola_aliena> <traduzione1 traduzione2 ...>")
            return

        parola_aliena = campi[0]

        if not parola_aliena.isalpha():
            print("Errore: la parola aliena può contenere solo lettere.")
            return

        traduzioni = campi[1:]
        print(campi)

        for trad in traduzioni:
            if trad.isalpha():
                self.diz.addWord(parola_aliena, trad)
            else:
                print(f"Errore: la traduzione {trad} contiene caratteri non validi e verrà scartata.")

        print("Aggiunta!")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        query = query.strip()
        query = query.lower()

        if not query.isalpha():
            print("Errore: la parola aliena può contenere solo lettere.")
            return

        print(query)
        traduzioni_trovate = self.diz.translate(query)

        if traduzioni_trovate:
            print(traduzioni_trovate)
        else:
            print("Parola non presente nel dizionario.")

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        query = query.strip()
        query = query.lower()

        if query.count("?") != 1:
            print("Errore: la parola da cercare deve contenere esattamente un solo simbolo '?'.")
            return

        # sostituire "?" con stringa vuota e usare .isalpha()
        query_senza_jolly = query.replace("?", "")
        if not query_senza_jolly.isalpha():
            print("Errore: la parola aliena può contenere solo lettere.")
            return

        traduzioni_trovate = self.diz.translateWordWildCard(query)

        if traduzioni_trovate:  # se la lista restituita non è vuota
            print(traduzioni_trovate)
        else:
            print("Nessuna corrispondenza trovata nel dizionario.")

    def handlePrint(self, filename="output.txt"):
        dizionario_corrente = self.diz.getDizionarioAlieno()

        print(f"Stampa dizionario corrente nel file '{filename}' in corso...")

        with open(filename, "w", encoding="utf-8") as fout:
            for parola_aliena, traduzioni in dizionario_corrente.items():
                traduzioni_formattate = " ".join(traduzioni) # .join() per unire tutte le traduzioni con uno spazio
                fout.write(f"{parola_aliena} {traduzioni_formattate}\n")

        print("Finito!")