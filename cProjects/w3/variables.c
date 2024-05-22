#include <stdio.h>

int main()
{
	int studentID = 15; // 2 or 4 bytes 
	int studentAge = 23; 
	float studentFee = 30.75; // 4 bytes
	char studentGrade = 'A'; // 1 byte

	printf("The students ID is %d\n", studentID);
	printf("The students age is %d\n", studentAge);
	printf("The student fee is currently %.2f\n", studentFee);
	printf("The students grade is %c\n", studentGrade);
}
