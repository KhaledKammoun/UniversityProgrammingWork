package chapitre2;
import java.util.Scanner ;
public class Essai {
	
	//question n°1
	/* public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Entrer une chaine de caractere : ");
		String s = sc.nextLine();
		System.out.println("Chaine s = "+s) ;
		sc.close();
	}
	*/
	
	//question n°2
	/*public static void main(String[] args) {
		Scanner sc = new Scanner(System.in) ;
		String s = "";
		int i = 1 ; 
		while (!s.equals("ok")) {
			System.out.print("Entrer la chaine num°"+i+" : ");
			s = sc.nextLine() ;
			i++ ;
		}
		sc.close();
	}
	*/
	
	//question n°3
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Entrer un entier : ");
		if (sc.hasNextInt()) {
			int entier = sc.nextInt();
			System.out.println("entier = "+entier) ;
		}
		else
			System.out.println("Erreur : Entrer un entier.");
		sc.close();
	}
}
