#include <stdio.h>

int goto_structure(int a)
{

    a += 2;
    if (a < 10)
    {
        goto A;
    }
    a += 2;
A:
    a += 10;
    return a;
}

int main()
{
    printf("%d\n", goto_structure(0));
    return 0;
}