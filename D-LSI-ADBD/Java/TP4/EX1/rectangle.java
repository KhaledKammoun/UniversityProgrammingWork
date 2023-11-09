package chapitre1;
public class rectangle {
	float largeur, longeur ;
	
	public rectangle(float longu, float large) {
		this.largeur = large ;
		this.longeur = longu ;
	}
	public float calculerSurface() {
		return largeur * longeur ;
	}
	
	public float calculerPerimetre() {
		return (largeur + longeur)*2 ;
	}
	
	public static boolean comparerRectangles(rectangle rect1, rectangle rect2) {
		if (rect1.longeur == rect2.longeur && rect1.largeur == rect2.largeur)
			return true ;
		return false ;
			
	}
	class Zoo {
		public String coolMethod() {
		return "Wow baby"; }
	}
	
	public static rectangle additionRectangle(rectangle rect1, rectangle rect2) {
		return new rectangle(rect1.longeur + rect2.longeur, rect1.largeur + rect2.largeur);
	}
	public String toString() {
		return "longuer = " + longeur + " largeur = " + largeur ;
	}
	
	public static void main(String[] args) {
		rectangle r = new rectangle(5,5) ;
		rectangle r1 = new rectangle(6,8) ;
		
		float surface = r.calculerSurface() ;
		float surface1 = r1.calculerSurface() ;
		
		System.out.println("Surface de rect = " + surface) ;
		System.out.println("Surface de rect1 = " + surface1) ;
		System.out.println(r.toString()) ;
		float perimetre = r.calculerPerimetre() ;
		float perimetre1 = r1.calculerPerimetre() ;
		
		System.out.println("Perimetre = " + perimetre) ;
		System.out.println("Perimetre1 = " + perimetre1) ;
		System.out.println(r1.toString()) ;
		boolean b = comparerRectangles(r, r1) ;
		if (b)
			System.out.println("rect == rect1") ;
		else
			System.out.println("rect != rect1") ;
		
		//question 9
		rectangle r2 = additionRectangle(r,r1) ;
		System.out.println("rect2 = rect + rect1 : ") ;
		System.out.println("longeur2 = " + r2.longeur + " | largeur2 = "  + r2.largeur) ;
		
		float surface2 = r2.calculerSurface() ;
		float perimetre2 = r2.calculerPerimetre() ;
		System.out.println("Surface de rect2 = " + surface2) ;
		System.out.println("Perimetre2 = " + perimetre2) ;
		
	}
}

