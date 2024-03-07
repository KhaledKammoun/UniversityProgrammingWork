class Book :
    def __init__(self, titre, auteur, prix) :
        self.titre = titre
        self.auteur = auteur
        self.prix = prix
    
    def view(self) :
        return f"{self.titre} de {self.auteur} est vendu à {self.prix} euros"

if __name__ == "__main__" :
    book1 = Book("L'histoire du temps", "Stephen Hawking", 15.50)
    print(book1.view())