package chapitre2 ;
abstract class Ex1{
	int x ;
	String z;
	abstract int m1();
	void m2(){
		int p;
		System.out.println(z);
		System.out.println(z.length());//affiche le nombre de caractères de z
		// Ex1 c = new Ex1();
	}
}
//question 3
abstract class SubEx3 extends Ex1{
	abstract void m3() ;
}

//question 4
 abstract class Sub1Ex1 extends SubEx3 {
	 public static void main() {
		 Sub1Ex1 s ;
	 }
	  
 }
 