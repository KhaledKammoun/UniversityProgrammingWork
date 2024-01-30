package heritfood;

public class Apple extends food.Fruit {
	public void caracteristique() {
		System.out.println("Apple ...") ;
	}
	public static void main(String[] args) {
		Apple apple = new Apple() ;
		apple.caracteristique();
	}
}
/* 3. explorer les package food et heritfood et les autres
 * packages que vous avez créées, qu’est-ce que vous remarquez ?
 * --> On remarque que qu'il existe deux dossiers bin et source, crées automatiquement .
 * bin : comporte les fichiers bytecode (.class)
 * src : comporte les fichiers code source (.java)
 * */
 