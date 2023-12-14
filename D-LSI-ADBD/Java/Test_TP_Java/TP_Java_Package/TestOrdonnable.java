package TP_Java_Package;

public class TestOrdonnable {

	public static void main(String[] args) {
		industriels ind1 =  new industriels("Nom", "Prenom", "Entreprise B", "Ingénieur") ;
		industriels ind2 = new industriels("Khaled", "Kammoun", "Entreprise A", "Ingénieur");
		
		 Universitaire univ1 = new Universitaire("Nom1", "Prenom1", "Université A", "Math");
	     Universitaire univ2 = new Universitaire("Nom2", "Prenom2", "Université B", "Phy");
	     
	     
	     IndustrielOrder ind_compare= new IndustrielOrder(ind1, ind2) ;
	     UniversitaireOrder univ_compare= new UniversitaireOrder(univ1, univ2) ;
	     System.out.println("Avant le Tri : ") ;
	     System.out.println("Industriel 1 : " + ind1);
	     System.out.println("Industriel 2 : " + ind2);
	     System.out.println("Universitaire 1 : " + univ1);
	     System.out.println("Universitaire 2 : " + univ2);
	     
	     if (ind_compare.orderBy()) {
	    	 industriels ind_var = ind1 ;
	    	 ind1 = ind2 ;
	    	 ind2 = ind_var ;
	     }
	     
	     if (univ_compare.orderBy()) {
	    	 Universitaire univ_var = univ1 ;
	    	 univ1 = univ2 ;
	    	 univ2 = univ_var ;
	     }
	     
	     System.out.println("Aprés le Tri : ") ;
	     System.out.println("Industriel 1 : " + ind1);
	     System.out.println("Industriel 2 : " + ind2);
	     System.out.println("Universitaire 1 : " + univ1);
	     System.out.println("Universitaire 2 : " + univ2);
	}

}
