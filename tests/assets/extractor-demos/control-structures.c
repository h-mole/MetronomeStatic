float sin()
{
    return 0.0;
}
int for_demo_1(int a)
{
    for (int i = 0; i < 10; i++)
    {
    }
    return a;
}

int for_demo_omitting_body(int a)
{
    for (int i = 0; i < 10; i++)
        i += 1;
    return a;
}

int for_demo_omitting_1(int a)
{
    int i = 0;
    for (; i < 10; i++)
    {
    }
    return a;
}

int for_demo_omitting_2(int a)
{

    for (int i = 0;; i++)
    {
    }
    return a;
}

int for_demo_omitting_3(int a)
{

    for (int i = 0; i < 10;)
    {
    }
    return a;
}

int for_demo_omitting_1_3(int a)
{
    int i = 0;
    for (; i < sin();)
    {
    }
    return a;
}
int for_demo_omitting_1_2(int a)
{
    int i = 0;
    for (;; i++)
    {
    }
    return a;
}

int for_demo_omitting_2_3(int a)
{

    for (int i = 0;;)
    {
    }
    return a;
}

int for_demo_omitting_all(int a)
{

    for (;;)
    {
    }
    return a;
}