#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Author: Mackenzie Park-McInnes
//Title: P4
//Purpose: Solve 'projecteuler.net' archived problem 4
//Date: 2016/08/09
//Compilation Instructions: gcc -o p4 p4.c

const char *stringReverse(char []);

int main() {
	char arr[7];
	char rev_arr[7];

	int i;
	int j;
	int id;
	int ir;

	int len;
	int num;
	int lrg;
	int cmp = 0;

	for(i=100;i<=999;i++) {
		for(j=100;j<=999;j++) {
			num = i*j;
			sprintf(arr, "%d", num);

			len = strlen(arr)-1;
			ir = len;
			for(id=0;id<=len;id++) {
				rev_arr[ir] = arr[id];
				ir--;
			}

			cmp = strcmp(arr, rev_arr);
			if (cmp == 0 && num > lrg) {
				lrg = num;

			printf("Array: %s Reversed Array: %s Largest Palindrome: %d\n", arr, rev_arr, lrg);

			}
		}
	}
}