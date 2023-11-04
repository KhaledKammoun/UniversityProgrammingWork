package calcFunctions;

public class Cercle {

	//declarer une constant pi=3.14
	final static float pi = 3.14f ;
	public static void calculer_aire_per(double rayon){
	// Écrivez votre code ici
		System.out.println("aire = " + (rayon *rayon * pi)) ;
		System.out.println("perimetre = " + (2 *rayon * pi)) ;
	}
	public static void main(String[] args) {
		double rayon = 4.2 ;
		calculer_aire_per(rayon) ;
	}

}
