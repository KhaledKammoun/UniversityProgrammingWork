package TP_Java_Package;

public class IndustrielOrder implements Ordonnable{
	public industriels ind1 ;
	public industriels ind2 ;
	public IndustrielOrder(industriels indus1, industriels indus2) {
        this.ind1 = indus1;
        this.ind2 = indus1;
    }
	
	public boolean orderBy() {
		// order by nom
		int compare = ind1.nom.compareToIgnoreCase(ind1.nom) ;
		if (compare < 0) {
			return false ;
			// ind1.nom < ind1.nom
		}
		return true ;
	}
}
