#include <stdio.h>

//Title : P1
//Author : Mackenzie Park-McInnes
//Purpose : Solve 'projecteuler.net' archived problem 1
//Date : 2016/08/04
//Compilation Instructions: gcc -o p1 p1.c

int main() {
	
	int sum = 0;
	int i = 0;

	while (i < 1000) {
		if (i % 3 == 0 or i % 5 == 0) {
			sum += i;
		}
	}
	printf("%d", sum);
}