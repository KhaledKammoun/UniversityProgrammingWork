package TP_Java_Package;

public class UniversitaireOrder implements Ordonnable{
	public Universitaire univ1 ;
	public Universitaire univ2 ;
	public UniversitaireOrder(Universitaire univ1, Universitaire univ2) {
        this.univ1 = univ1;
        this.univ2 = univ2;
    }
	
	public boolean orderBy() {
		// order by nom
		int compare = univ1.nom.compareToIgnoreCase(univ2.nom) ;
		if (compare < 0) {
			return false ;
			// univ1.nom < univ2.nom
		}
		return true ;
	}
}
