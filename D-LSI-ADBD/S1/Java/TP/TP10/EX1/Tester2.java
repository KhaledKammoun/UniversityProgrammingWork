package EX1;

public class Tester2{
public static void main (String [] args){
	Integer i3 = 10;
	Integer i4 = 10;
	if(i3 == i4)
		System.out.println("même object");
	if(i3.equals(i4))
		System.out.println("significativement égaux");
	}
}