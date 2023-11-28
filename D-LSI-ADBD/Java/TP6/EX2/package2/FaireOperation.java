package chapitre2;

public interface FaireOperation {
	String t="jeu";
	static int multiplier(int a, int b) {
		return a*b;
	}
	default String afficher(int a, int b){
		return t+a+b;
	}
	abstract boolean testerValeur(int c) ;
	abstract void jouer();
}
