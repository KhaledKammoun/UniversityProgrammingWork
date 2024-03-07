format_adresse = "numéro, nom rue, code pastal, région"

class Personne:
    def __init__(self, nom, prenom, address, telephone=None, email=None):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email
        self.__address = address
    def region(self):
        if self.__address is not None:
            parts = self.__address.split(",")
            if "région" in format_adresse:
                index_région = [c.strip() for c in format_adresse.split(",")].index("région")
                if index_région < len(parts):
                    region = parts[index_région].strip()
                    return f"région {region} connue"
            return "région inconnue"
        else:
            return "région inconnue"

    def __str__(self):
        personne_info = "Nom : {}\nPrénom : {}".format(self.nom, self.prenom)
        return self.region() + "\n" + personne_info

# Partie 2
liste_personne = []
    
def lire_personne() :
    nom = input("Donner Votre Nom : ")
    prenom = input("Donner Votre Prénom : ")
    telephone = input("Donner Votre numéro de téléphone : ")
    email = input("Donner Votre Email : ")
    print("---------Adresse---------")
    num_adresse = input("   Donner le numéro D'adresse : ")
    nom_rue_adresse = input("   Donner le nom de rue : ")
    code_postal_adresse = input("   Donner le code postal d'adresse : ")
    région_adresse = input("   Donner la région de votre adresse : ")
    adresse = " ,".join([num_adresse, nom_rue_adresse, code_postal_adresse, région_adresse])
    print(f"Personne {nom} {prenom} est Ajouté !!")
    print("-------------------------------")
    return Personne(nom, prenom, adresse, telephone, email)
def print_personne(liste_personne) :
    commande = input(":: all : afficher tous les personnes | String : nom du personne\n    Type Commande : ")
    if liste_personne and commande :
        if (commande.lower() == "all") :
            for personne in liste_personne :
                print("----Person-----")
                print(personne.__str__())
        elif (commande.lower()) :
            for personne in liste_personne :
                if personne.nom.lower() == commande.lower() :
                    print("----Person-----")
                    print(personne.__str__())
    else :
        print("\n   Liste Personne est Vide !!!\n")   
    print("-------------------------------")

def drop_personne(liste_personne) :
    print("-----Drop------")
    nom = input("Donner le Nom : ")
    prenom = input("Donner le Prénom : ")
    for i in range(len(liste_personne)) : 
        if liste_personne[i].nom == nom and prenom == liste_personne[i].prenom :
            liste_personne.pop(i)
            print(f"Personne {nom} {prenom} est supprimé !!!")
            break
    print(f"\n  Personne {nom} {prenom} n'existe pas !!!\n")
    print("-------------------------------")

if __name__ == '__main__' :
    while True :
        print("exit : fin du programme\ndrop : supprimer un personne\ninsert : ajouter un personne\nprint : afficher tous les personnes")
        case = input("Type Commande : ").lower()
        if case == 'exit' :
            break
        elif case == 'drop' :
            drop_personne(liste_personne)
        elif case == 'insert' :
            liste_personne.append(lire_personne())
        elif case == "print" :
            print_personne(liste_personne)