public class Global {
	public static int a,b ;
	public int c,d ;
    // static :  exécuté lorsque la classe est chargée
	static{
		a = 2 ;
		b = 3 ;
	}
	// non static : exécuté chaque fois qu'une instance de la classe est créée .
	{
		c = 5 ;
		d = 7 ;
	}
	public Global() {
		System.out.println("une instance Gobal Créée") ;
	}
	public static int useStatic() {
		a = 10 ;
		b = 15 ;
		return a * b ;
	}
	public int useInstance() {
		this.c = 20 ;
		this.d = 35 ;
		return a + b + c + d ;
	}
	public static void main(String[] args) {
		Global g = new Global() ;
		System.out.println(useStatic()) ;
		System.out.println(g.useInstance()) ;
	}
}
