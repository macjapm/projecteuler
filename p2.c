#include <stdio.h>

//###################
//Command Line Applet
//###################
//Author : Mackenzie Park-McInnes
//Title : P2
//Purpose : Solve 'projecteuler.net' archived problem 2
//Usage : ./p2 Takes single argument corresponding to limit with which to generate fibonacci sequence up to
//Compilation : gcc -o p2 p2.c

int one = 1;
int two = 1;
int temp = 0;
int sum = 0;
int limit;

int main(int argc, char* argv[]) {

	if (argc == 2) {
		limit = atoi(argv[1]);
	}
	else {
		printf("Error: Inconsistent Parameter Number\n");
		return(-1);
	}

	while (two <= limit) {
		temp = two;
		two += one;
		one = temp;

		if (two % 2 == 0) {
			sum += two;
		}
	}

	printf("%d\n", sum);
}
