//Author : Mackenzie Park-McInnes
//Title : P12
//Purpose : Solve 'projecteuler.net' archived problem 12
//Compilation Instructions : gcc -o p12 p12.c

#include <stdio.h>
#include <stdlib.h>

int main() {
	int i;
	int d;
	int index = 1;
	long triangle = 0;
	int pdivs = 0;
	int lrg = 0;
	
	long * divs = malloc(1000 * sizeof(long));
	//int divs_max = 0;

	while (lrg <= 501) {
		for(i=1;i<=index;i++){
			triangle = triangle + i;
		}

		for(d=1;d<=triangle;d++) {
			if (triangle % d == 0) {
				pdivs += 1;
			}
		}
		printf("Tri Num %d = %ld with %d proper divisors :: %d ::\n", index, triangle, pdivs, lrg);
		if (pdivs > lrg) {
			lrg = pdivs;
		}
		index++;
		triangle = 0;
		pdivs = 0;
	}
	printf("%d\n", lrg);
}