package TP_Java_Package;

public class Universitaire extends Participant {
	String specialite ;
	public String toString() {
		return ("Participant : {" + super.toString() + ", specialite : " + specialite + "}") ;
	}
	
	public Universitaire(String nom,String prenom,String affiliation, String specialite) {
		super(nom, prenom, affiliation) ;
		this.specialite = specialite ;
	}
}
