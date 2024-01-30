package modificateur;
import java.util.Scanner ;
public class Usage1Tapis {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Donner Trois Valeur Float : ") ;
		String floats_String[] = sc.nextLine().split("\\s");
		sc.close();
		float vall = Float.parseFloat(floats_String[0]) ;
		float val2 = Float.parseFloat(floats_String[1]) ;
		float val3 = Float.parseFloat(floats_String[2]) ;
		Tapis t1 = new Tapis(vall, val2, val3) ;
		float surfaceTapis_t1 = t1.calculerSurfaceTapis() ;
		float prixTapis_t1 = t1.calculerPrixTapis(surfaceTapis_t1) ;
		System.out.println("Prix de t1 : " + prixTapis_t1) ;
	}
 
}
