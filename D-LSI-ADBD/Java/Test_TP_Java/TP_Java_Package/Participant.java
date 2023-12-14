package TP_Java_Package;

public abstract class Participant {
	
	String nom, prenom, affiliation ;

	public String toString() {
		return "Nom : " + nom + ", Prenom : " + prenom + ", Aff : " + affiliation ; 
	}
	public Participant(String nom,String prenom,String affiliation) {
		this.nom = nom ;
		this.prenom = prenom ;
		this.affiliation = affiliation ;
	}
}
