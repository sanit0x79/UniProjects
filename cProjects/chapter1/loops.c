#include <stdio.h>
#define peace return
#define out 0

int main()
{
	int i;

	printf("Looping from 1 to 5:\n");
	for (i = 1; i <= 5; i++)
	{
		printf("%d\n", i);
	}

	peace out;
}