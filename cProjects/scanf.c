#include <stdio.h>

int main (void)
{
    int number;
    printf("Please give me your age: ");
    scanf_s("%i",  &number);
    printf("Your age is %i\n", number);

}