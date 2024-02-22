class Personne : 
    def __init__(self,nom,prenom, telephone = None, email = None) :
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email

    def __str__(self) :
        return "Nom: {} | Prenom : {} | Telephone : {} | email : {}".format(self.nom,self.prenom, self.telephone, self.email)
        
        
personne1 = Personne("Nom1", "Prenom1", "tel1", "email1")
print(personne1.__str__()) 