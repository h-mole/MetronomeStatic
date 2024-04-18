#include <stdio.h>

int main(int a, int b)
{
    if (a < 0)
    {
        return -1;
    }
    for (int i = 0; i < b; i++)
    {
        a += i;
    }
}
