#include <stdio.h>

void checkCars()
{
	int cars = 2;
	switch(cars)
	{
		case 1:
			printf("One Car\n");
			break;

		case 2:
			printf("Two Cars\n");
			break;
		
		case 3:
			printf("Three Cars\n");
			break;
		
		default:
			printf("No Cars\n");
			break;
	}
}

int main()
{
	checkCars();
	return 0;
}