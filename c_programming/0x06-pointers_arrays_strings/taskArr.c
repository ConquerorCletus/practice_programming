#include <stdio.h>

int main()
{
	int a[5]= {0,1,2,3,4};
	int i;


	for (i = 4; i >= 0; i--)
		printf("%d\n", a[i]);
	return(0);
}
