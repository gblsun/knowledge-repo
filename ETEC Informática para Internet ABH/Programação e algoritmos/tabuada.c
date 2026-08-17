#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main ()
{
    setlocale (LC_ALL, "portuguese");

    int n1, n2;

    for (n1 = 0; n1 <= 100; n1++)
    {
        printf("Esta é a tabuada do numero:%d\n", n1);
        for (n2 = 0; n2 <= 10; n2++)

        {
        printf("%d x %d = %d\n", n1, n2, n1*n2);
        }
    }
    return 0;
}
