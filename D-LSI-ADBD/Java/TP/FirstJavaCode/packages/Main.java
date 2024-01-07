package packages;


import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        
        calculation();
        compare();
    }
    public static void calculation(){
        int a, b;
        System.out.print("Donner a et b : ") ;
        Scanner reader = new Scanner(System.in);
        a = reader.nextInt();
        b = reader.nextInt();
        reader.close() ;
        // calculation
        System.out.println("a + b = " + (a + b));
        System.out.println("a - b = " + (a - b));
        float divisionFloat = (float) a / b; // Cast one operand to float for accurate division.
        int divisionInt = a / b;
        System.out.println("a / b = " + divisionFloat);
        System.out.println("a // b = " + divisionInt);
        System.out.println("a % b = " + (a % b));
        
    }
    public static void compare(){
        System.out.print("Donner 3 entiers a, b et c : ") ;
        Scanner reader = new Scanner(System.in);
        int a = reader.nextInt();
        int b = reader.nextInt();
        int c = reader.nextInt() ;
        reader.close() ;
        int max = Math.max(a, Math.max(b, c));
        int min = Math.min(a, Math.min(b, c));
        int moyenne = 0;
        if ((a == max && b == min) || (b == max && a == min))
            moyenne = c ;
        if ((a == max && c == min) || (c == max && a == min))
            moyenne = b ;
        if ((c == max && b == min) || (b == max && c == min))
            moyenne = a ;
        System.out.println(a+" | "+b+" | "+c) ;
        System.out.println(min+" | "+moyenne+" | "+max) ;

        
    }

}
