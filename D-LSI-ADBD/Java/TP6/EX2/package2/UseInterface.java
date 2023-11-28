package chapitre2;

public class UseInterface implements FaireOperation{
	String t="jeu";
	static int multiplier(int a, int b) {
		return a*b;
	}

	private int x,y ;
	private static int z ;
	
	// UseInterface est un constructeur
	UseInterface(int a, int b){
		x=a ;
		y=b ;
	}
	public boolean testerValeur(int c) {
		return c != 0 ;
	}
	public void jouer() {
		System.out.print("On commence à utiliser les interfaces") ;
	}
	
	public static void main(String[] args) {
		UseInterface uI = new UseInterface(3, 10) ;
		z = uI.y ;
		boolean b = uI.testerValeur(z) ;
		uI.jouer();
		int mul = multiplier(uI.x, uI.y) ;
		String s = uI.afficher(uI.x, uI.y) ;
	}

}
