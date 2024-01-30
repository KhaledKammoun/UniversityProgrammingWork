package TP_Java_Package;

public class TestSeminaire {
	public static void main(String[] args) {
		Seminaire sem = new Seminaire("Data", "Janvier", "Sfax", 100, 200) ;
		industriels indu = new industriels("nom_part", "prenom_part", "ISIMS", "Ingénieur") ;
		Universitaire univ = new Universitaire("Khaled", "Kammoun", "ISIMS", "Etudiant") ;
		sem.addPart(indu) ;
		sem.addPart(univ) ;
		System.out.println(sem) ;
		System.out.println(indu) ;
		System.out.println(univ) ;
		System.out.println(sem.recette()) ;
	}
}
