package chapitre2 ;
public class Main {
	 public static void main(String[] args) {
		 Sub1Ex1 s = new Sub1Ex1();
		 s.m2();
		 int val = s.m1();
		 System.out.println(val);
		 s.m3();
	 }
}

abstract class Ex1{
	int x ;
	String z;
	abstract int m1();
	void m2(){
		int p = 5;
		System.out.println(p);
		System.out.println(z.length());//affiche le nombre de caractères de z
		// Ex1 c = new Ex1();
	}
}
//question 3
abstract class SubEx3 extends Ex1{
	abstract void m3() ;
}

//question 4
 class Sub1Ex1 extends SubEx3 {
	 int m1() {
		 System.out.println("Ici m1") ;
		 x = 0 ;
		 return x ;
	 }
	 void m3() {
		 System.out.println("Ici m3") ;
	 }
	 public static void main(String[] args) {
		 Sub1Ex1 s = new Sub1Ex1();
		 s.m2() ;
		 int val = s.m1();
		 System.out.println(val) ;
		 s.m3();
	 }
	  
 }