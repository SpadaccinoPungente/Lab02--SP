class Dictionary:
    def __init__(self):
        self.dizioniario_alieno = {}

    def addWord(self, parola_aliena, traduzione):
        if parola_aliena in self.dizioniario_alieno:
            self.dizioniario_alieno[parola_aliena].append(traduzione)
        else:
            self.dizioniario_alieno[parola_aliena] = [traduzione]

    def translate(self):
        pass

    def translateWordWildCard(self):
        pass