class Etudiant :
    def __init__(self, nom, note1, note2) :
        self.nom = nom
        self.note1 = note1
        self.note2 = note2
    def calc_moy(self) :
        return (self.note1 + self.note2) / 2
    def afficher(self) :
        print(f"Le nom de l'étudiant est {self.nom} et sa moyenne est {self.calc_moy()}")
if __name__ == "__main__" :
    etudiant1 = Etudiant("etudient1", 10, 15)
    etudiant1.afficher()

