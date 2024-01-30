package usageModif ;
import modificateur.Tapis ;

public class Usage2Tapis {

	public static void main(String[] args) {
		if (args.length != 3) {
            System.out.println("Error, Donner 3 arguments");
            return;
        }
		float val1 = Float.parseFloat(args[0]) ;
		float val2 = Float.parseFloat(args[1]) ;
		float val3 = Float.parseFloat(args[2]) ;
		Tapis t2 = new Tapis(val1, val2, val3) ;
		
		// La méthode calculerSurfaceTapis est déclarée avec un accès package-private
        // dans la classe 'Tapis'. Cela signifie qu'elle est uniquement accessible à
        // d'autres classes du même package .
		// float surfaceTapis_t2 = t2.calculerSurfaceTapis() ;
		
		// La méthode calculerPrixTapis est déclarée avec un accès protected dans la classe Tapis.
        // Bien que cela autorise son accès aux sous-classes de 'Tapis', 'Usage2Tapis' n'est pas
        // une sous-classe de 'Tapis' .
		// float prixTapis_t2 = t2.calculerPrixTapis(surfaceTapis_t2) ;
		// System.out.println("Prix de t1 : " + prixTapis_t2) ;
	}

}
