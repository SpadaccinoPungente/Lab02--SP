class Dictionary:

    def __init__(self):
        self.dizionario_alieno = dict()

    def addWord(self, parola_aliena, traduzione):
        if parola_aliena in self.dizionario_alieno.keys():
            self.dizionario_alieno[parola_aliena].add(traduzione)
        else:
            self.dizionario_alieno[parola_aliena] = {traduzione}

    def translate(self, query):
        if query in self.dizionario_alieno:
            return self.dizionario_alieno[query]
        else:
            return None

    def translateWordWildCard(self, query):
        pass

    def printDizionarioAlieno(self):
        for elem in self.dizionario_alieno:
            print(elem)