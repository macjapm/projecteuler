#Author : Mackenzie Park-McInnes
#Title : P4
#Purpose : Solve 'projecteuler.net' archived problem 4

import java.lang.StringBuilder;
import java.lang.String;

public class Pal {
	public static void main(String []args) {

		int num = 0;
		String numString;
		String reverseString;
		int currentLargest = 0;

		for (int i = 100; i <= 999; i++) {
			for (int j = 100; j <= 999; j++) {
				num = i * j;
				numString = Integer.toString(num);
				reverseString = stringReverse(numString);

				if (numString.compareTo(reverseString) == 0 && num > currentLargest) {
						currentLargest = num;
				}
				System.out.println("Current Multiple: " + num + " :: Current Palindrome: " + currentLargest);
			}
		}
	}

	public static String stringReverse(String s) {
		String revS;
		revS = new StringBuilder(s).reverse().toString();
		return (revS);
	}
}
