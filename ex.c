#include <stdio.h>
#include <stdlib.h>

void func1(void) {
	while (1) {
		if (1 == 0) {
			printf("GG\n");
		}
		while (0) {
			;
		}
	}
}


int main(void) {
	int a = 0;
	while (a++ < 10) {
		;
	}
	return 0;
}

