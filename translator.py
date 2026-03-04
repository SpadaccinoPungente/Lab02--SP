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
        print("4. Exit")
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
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        pass