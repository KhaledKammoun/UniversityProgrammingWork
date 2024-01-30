package TP_Java_Package;

import java.util.Arrays;

public class operation {

	public static void main(String[] args) {
		for (int i = 0 ; i<args.length ; i++) {
			System.out.print(args[i] + " ") ;
		}
		System.out.println() ;
		String[] t = new String[args.length] ;
		t = args.clone() ;
		Arrays.sort(t);
		for (int i = 0 ; i<t.length ; i++) 
			System.out.print(t[i] + " ") ;
		
	}

}
