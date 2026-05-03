# Parte 1 

titolo = "La Divina Commedia"
copie = 5
prezzo_medio = 18.50
stato = copie > 0

print("Titolo:", titolo)
print("Copie disponibili:", copie)
print("Prezzo medio:", prezzo_medio)
print("Disponibile:", stato)

# Parte 2 – Strutture dati

lista_libri = [
    "Moby Dick",
    "1984",
    "Il Nome della Rosa",
    "I Promessi Sposi",
    "La Divina Commedia"
]

copie_libri = {
    "Moby Dick": 3,
    "1984": 5,
    "Il Nome della Rosa": 2,
    "I Promessi Sposi": 4,
    "La Divina Commedia": 1
}

utenti_registrati = {
    "Mario Martinez",
    "Luca Nespoli",
    "Anna Tatangelo",
    "Giulia Piccinini"
}

print(lista_libri)
print(copie_libri)
print("Copie totali disponibili:", sum(copie_libri.values()))
print(utenti_registrati)

#Parte2
#Inserisco nell'esercizio classi astratte, eccezioni personalizzate per utilizzare tutti gli stumenti appresi

from abc import ABC, abstractmethod

#Errore personalizzato
class LibroNonDisponibileError(Exception):
    pass

#classi astratte
class Prestabile(ABC):

    @abstractmethod
    def diminuisci_disponibilita(self):
        pass
    
class PrestitoService(ABC):

    @abstractmethod
    def presta(self, utente, oggetto_prestabile, giorni):
        pass

#classe Libro
class Libro(Prestabile):
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili
        
    @property
    def copie_disponibili(self):
        return self._copie_disponibili

    @copie_disponibili.setter
    def copie_disponibili(self, valore):
        if valore < 0:
            raise ValueError("Le copie disponibili non possono essere negative.")
        self._copie_disponibili = valore

    def diminuisci_disponibilita(self):
        if self._copie_disponibili < 1:
            raise LibroNonDisponibileError(
                f"Il libro '{self.titolo}' non ha copie disponibili."
            )

        self._copie_disponibili -= 1

    def info(self):
        return f"""Titolo: {self.titolo}
Autore: {self.autore}
Anno: {self.anno}
Copie disponibili: {self.copie_disponibili}"""

#classe Utente
class Utente:
    auto_increment_id = 1

    @classmethod
    def increment_id(cls):
        current_id = cls.auto_increment_id
        cls.auto_increment_id += 1
        return current_id

    def __init__(self, nome, eta):
        self.id_utente = Utente.increment_id()
        self.nome = nome
        self.eta = eta

    def scheda(self):
        return f"""Nome: {self.nome}
Età: {self.eta}
ID utente: {self.id_utente}"""

class PrestitoLibro:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni
        
    def dettagli(self):
        print(f"""Dettagli prestito
Utente:
{self.utente.scheda()}
Libro:
{self.libro.info()}
Durata prestito: {self.giorni} giorni
""")
        
class PrestitoLibroService(PrestitoService):
    def presta(self, utente, libro, giorni):
        try:
            libro.diminuisci_disponibilita()
            return PrestitoLibro(utente, libro, giorni)

        except LibroNonDisponibileError as error:
            print("Errore:", error)
            return None

# Esempio

libro1 = Libro("Moby Dick", "Melville", 1851, 3)
libro2 = Libro("1984", "Orwell", 1949, 5)
libro3 = Libro("I Promessi Sposi", "Manzoni", 1827, 4)

libro1.info()
print()
libro2.info()
print()
libro2.info()

# Utenti
utente1 = Utente("Mario Martinez", 35)
utente2 = Utente("Luca Nespoli", 42)
utente3 = Utente("Anna Tatangelo", 28)

print(utente1.scheda())
print()
print(utente2.scheda())
print()
print(utente3.scheda())

servizioPrestito = PrestitoLibroService() 
prestiti = [
    servizioPrestito.presta(utente1, libro1, 10),
    servizioPrestito.presta(utente2, libro2, 7),
    servizioPrestito.presta(utente3, libro3, 5)
]

print("\nCopie aggiornate:")
for libro in [libro1, libro2, libro3]:
    print(f"{libro.titolo}: {libro.copie_disponibili}")

print("\nDettagli prestiti:")
for p in prestiti:
    if(p):
        p.dettagli()
        print()
        
