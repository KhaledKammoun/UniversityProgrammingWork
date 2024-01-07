package EX2;
import java.util.Arrays ;
import java.util.Scanner ;
public class Operation {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in) ;
		System.out.print("Donner la longeur du tableau : ");
		int n = sc.nextInt() ;
		for (int i = 0 ; i<n ; i++) {
			args[i] = sc.next() ;
		}
		System.out.println("Les valeurs : ");
		for (int i = 0 ; i<n ; i++) {
			System.out.print(args[i] + " ");
		}
		sc.close() ;
		String[] t = new String[n] ;
		t = args.clone() ;
		//affichage
		Arrays.sort(t) ;
		System.out.println("Tableau triée" + Arrays.toString(t)) ;
		
	}
}
