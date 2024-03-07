class CompteBancaire :
    def __init__(self, numeroCompte, nom, solde) :
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde
    def Versement(self) :
        montant = float(input("Montant du versement : "))
        self.solde += montant
    
    def Retrait(self) :
        montant = float(input("Montant du retrait : "))
        self.solde -= montant
    
    def Agios(self) :
        agios = self.solde * 0.05
        self.solde -= agios

    def afficher(self) :
        print(f"Le compte de {self.nom} a pour numéro {self.numeroCompte} et un solde de {self.solde} euros.")
if __name__ == "__main__" :
    compte1 = CompteBancaire(123456789, "user1", 1000)
    compte1.Versement()
    compte1.Retrait()
    compte1.Agios()
    compte1.afficher()
