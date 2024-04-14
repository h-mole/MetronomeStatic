int simple_for_loop(int a)
{
    for (int i = 0; i < 2; i++)
    {
        a += 1;
    }
    return a;
}

int for_loop_with_condition(int a)
{
    for (int i = 0; i < 1; i++)
    {
        if (a % 2 == 0)
        {
            a += 1;
        }
        else
        {
            a += 2;
        }
        a += 2;
    }
    return a;
}

int for_loop_and_after_for(int a)
{
    for (int i = 0; i < 2; i++)
    {
        a += 2;
    }
    a += 2;
    return a;
}

int nested_for_loops(int a)
{
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            a += 2;
        }
    }
    a += 2;
    return a;
}

int if_wrapping_for(int a)
{
    if (a >= 8)
    {
        for (int i = 0; i < 2; i++)
        {
            a += 2;
        }
        a += 9;
    }
    a += 2;
    return a;
}