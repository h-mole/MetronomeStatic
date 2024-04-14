int if_demo_1(int a)
{
    if (a > 0)
    {
        a += 1;
    }
    else
    {
        a += 2;
    }
    return a;
}

int if_demo_2(int a)
{
    if (a > 0)
    {
        a += 1;
    }
    else if (a == 0)
    {
        a += 1145;
    }
    else
    {
        a -= 1;
    }
    return a;
}

int for_demo_1(int a)
{
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            a += 1;
        }
    }
    return a;
}

int for_demo_2(int a)
{
    int i = 0;
    for (; i < 10; i++)
    {
        a += 1;
    }
    for (; i < 15; i++)
        a += 1;

    return a;
}