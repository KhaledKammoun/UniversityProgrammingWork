package modificateur;
import java.util.Scanner ;
public class Usage1Tapis {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in) ;
		System.out.print("Donner Trois Valeur Float : ") ;
		float vall = sc.nextInt();
		float val2 = sc.nextInt();
		float val3 = sc.nextInt();
		sc.close();
		Tapis t1 = new Tapis(vall, val2, val3) ;
		float surfaceTapis_t1 = t1.calculerSurfaceTapis() ;
		float prixTapis_t1 = t1.calculerPrixTapis(surfaceTapis_t1) ;
		System.out.println("Prix de t1 : " + prixTapis_t1) ;
	}

}
