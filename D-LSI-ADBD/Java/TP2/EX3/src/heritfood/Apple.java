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
 * --> On remarque que la structure des fichiers ,comme la class Fruit dans le package food, est bien organisée et on
 * peut comprendre aussi l'héritage des class .
 * */
 