int main(int a, int b)
{
    int c = a + b;
    c = a - b;
    a = c + b;
    c = a;
    if (a > 0)
    {
        return c;
    }
}

int main2(int a, int b)
{

    if (a > 0)
    {
        int c = a + b;
        c = a - b;
        a = c + b;
        c = a;
    }
    else
    {
        int d = 123;
        int e = 445;
    }
    int c1 = a + b;
    c1 = a - b;
    a = c1 + b;
    c1 = a;
}