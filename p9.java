#Author : Mackenzie Park-McInnes
#Title : P9
#Purpose : Solve 'projecteuler.net' archived problem 9

import java.lang.*;

public class Pytrip {
	public static void main(String []args) {
		double axb;
		double sum;
		double product;

		for (double a = 1; a <= 1000; a++) {
			for (double b = a+1; b <= 1000; b++) {
				for (double c = b+1; c <= 1000; c++) {
					axb = Math.pow(a, 2) + Math.pow(b, 2);
					if (axb == Math.pow(c, 2)) {
						sum = a + b + c;
						if (a + b + c == 1000) {
							System.out.println(a);
							System.out.println(b);
							System.out.println(c);
							product = a*b*c;
							long number = Double.valueOf(product).longValue();
							System.out.println(number);
						}
					}
				}
			}
		}
	}
}
