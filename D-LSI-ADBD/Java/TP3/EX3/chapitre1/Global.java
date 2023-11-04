package chapitre1;

public class Global {
	static int a,b ;
	private int c;
	private int d;

	public Global() {
        System.out.println("Une instance Global Créée");
    }
	public static int useStatic() {
        a = 10;
        b = 15;
        return a * b;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
