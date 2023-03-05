#include <stdio.h>
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


/*To make sure pass phrase are the same.*/          for (a = 0; passphrase[a] != '\0' && pass[a] != '\0'; a++) 
{                                                       if (passphrase[a] == pass[a])                            {                                                      printf("Sign-in successful!!\n");                              break;                                  } 
	else if (passphrase[a] != pass[a])
	{                                       
	printf("Wrong passphrase!!!\n");
	break;
	}
	else if (name[a] == '\0')/* || pass[a] =='\0' || userName == '\0' || name == '\0')*/
	{
		printf("Empty field noticed!!!\n");
	}

}

	return (0);
}

