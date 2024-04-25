#include <stdio.h>

int calc(int a)
{
    return a + 1;
}

int close_data(int channel)
{
    return 0;
}

int goto_structure(int a)
{

    a += 2;
    a += 3;
A:
    if (a < 10)
    {
        a = a + 2;
        a += 5;
    }
    if (a < 100)
    {
        a -= calc(calc(a));
        close_data(a);
        goto A;
    }
    a += 10;
    return a;
}

int main()
{
    printf("%d\n", goto_structure(0));
    return 0;
}

int f(int a, int b)
{
    if (a < 0)
    {
        return -1;
    }
    else
    {
        for (int i = 0; i < b; i++)
        {
            a += i;
        }
    }
    return a;
}