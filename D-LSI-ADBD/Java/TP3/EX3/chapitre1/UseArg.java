package chapitre1;

public class UseArg {
    // Variables d'instance
     String nom;
     String prenom;

    // Constructeur
    public UseArg(String n, String p) {
        nom = n;
        prenom = p;
    }
    public void afficherNomPrenom() {
    	System.out.println("Nom : " + nom);
    	System.out.println("Prenom : " + prenom);
    }
    public static void main(String[] args) {
    	UseArg nomPrenom = new UseArg(args[0], args[1]) ;
    	nomPrenom.afficherNomPrenom();
    }
}
