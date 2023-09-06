#include <stdio.h>
#include <string.h>
/**
 * main - Get user signed in.
 * Return:0
 * Date:05-03-2023
 */

int main()
{
	char name[50];
	char userName[20];
	char passphrase[30];
	char pass[30];
	int a;


	printf("input your full name:\n");
        fgets(name, sizeof(name),stdin);

	printf("input desired username:\n");
        fgets(name, sizeof(name),stdin);

	printf("Enter your passphrase(2):\n");
	fgets(passphrase, sizeof(passphrase),stdin);
	printf("Enter your passphrase again(1):\n");
	fgets(pass, sizeof(pass),stdin);
	
	/*To make sure pass phrase are the same.*/
	if (strcmp(passphrase, pass) == 0)
		printf("Sign-in successful!!\n"); 
	else if (strcmp(passphrase, pass) != 0)
		printf("Wrong passphrase!!!\n");
	
	
	if (name == '\0' || userName == '\0')
		printf("Empty field noticed!!!\n");
	

	return (0);
}

