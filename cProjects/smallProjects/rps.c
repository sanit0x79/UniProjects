#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>


int main()
{
    char playerChoice[16];
    const char *words[] = {"Rock", "Paper", "Scissors"};
    int len = strlen(playerChoice);
    srand(time(NULL));
    int randomIndex = rand() % 3;
    const char *computerChoice = words[randomIndex];

    printf("Choose your pick:\n Rock\n Paper\n Scissors\n");
    fgets(playerChoice, sizeof(playerChoice), stdin);
    printf("Your choice was: %s\n", playerChoice);
    printf("Computer Choice: %s\n", computerChoice);

    if(len > 0 && playerChoice[len-1] == '\n')
    {
        playerChoice[len-1] = '\0';
    }

    if(strcmp(computerChoice, playerChoice) == 0)
    {
        printf("It's a tie!\n");
    } else 
    {
        printf("It's not a tie!\n");
    }
}
