#include <stdlib.h>
#include <stdio.h>

//Author : Mackenzie Park-McInnes
//Title : P5
//Purpose : Solve 'projecteuler.net' archived problem 5
//Compilation : gcc -o p5 p5.c

int main() {
	int sm = 1;
	int i;
	int td = 1;

	while (1) {
		for(i=1; i <= 20; i++) {
			if (sm % i != 0) {
				td = 0;
				break;
			}
		}
		
		if (td == 1) {
			printf("%d", sm);
			break;
		} else {
			td = 1;
			sm++;
		}
	}
}
