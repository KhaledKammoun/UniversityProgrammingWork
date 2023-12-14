package TP_Java_Package;

public class industriels extends Participant {
	String fonction ;
	public String toString() {
		return ("Participant : {" + super.toString() + ", Fonction : " + fonction + "}") ;
	}
	public industriels(String nom,String prenom,String affiliation, String fct) {
		super(nom, prenom, affiliation) ;
		this.fonction = fct ;
	}
	
}
