//Copy input to output, 1st version

#include <stdio.h>

main()
{
	c = getchar();

	while (c != EOF) {
		putchar(c);
		c = getchar();
	}
}