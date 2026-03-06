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
        traduzioni_trovate = []

        indice_jolly = query.find("?") # restituisce l'indice numerico del jolly

        # string[start_index:stop_index] prende da start_index incluso fino a stop_index escluso
        prefisso = query[:indice_jolly]  # prende tutto fino al jolly (escluso)
        suffisso = query[indice_jolly + 1:]  # prende tutto dopo il jolly

        # .items() per ciclare su chiavi e valori
        for parola_aliena, lista_traduzioni in self.dizionario_alieno.items():
            if len(parola_aliena) == len(query):
                if parola_aliena.startswith(prefisso) and parola_aliena.endswith(suffisso):
                    traduzioni_trovate.extend(lista_traduzioni) # .extend() fonde due liste

        return traduzioni_trovate

    """
    # modo di implementazione alternativa "fatta a mano":
    def translateWordWildCard(self, query):
        traduzioni_trovate = []
        
        # CICLO ESTERNO: passiamo in rassegna tutte le parole del dizionario
        for parola_aliena, lista_traduzioni in self.dizionario_alieno.items():
            
            # se non hanno la stessa lunghezza, scartiamo subito la parola
            if len(parola_aliena) == len(query):
                
                # flag per ricordarci se la parola va bene
                corrisponde = True 
                
                # CICLO INTERNO: scorriamo gli indici da 0 fino alla fine della parola
                for i in range(len(query)):
                    carattere_query = query[i]
                    carattere_dizionario = parola_aliena[i]
                    
                    # se i caratteri sono DIVERSI e il carattere della query NON è il jolly '?'...
                    if carattere_query != carattere_dizionario and carattere_query != "?":
                        # ...allora la parola non va bene! 
                        corrisponde = False
                        break # Interrompiamo subito il ciclo interno, inutile controllare le altre lettere
                
                # controllati tutti i caratteri, guardiamo il flag
                # se è ancora True, significa che tutti i caratteri combaciavano (o erano il jolly)
                if corrisponde:
                    traduzioni_trovate.extend(lista_traduzioni)
                    
        return traduzioni_trovate
    """

    def getDizionarioAlieno(self):
        return self.dizionario_alieno