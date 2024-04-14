typedef struct
{
    int value;
} MyStruct;

int sequential_func(int a)
{
    a += 100;
    return a;
}

int func_with_one_branch(int a)
{
    if (a < 100)
    {
        a += 100;
    }
    a += 9;
    if (a > 1000)
    {
        a += 1;
    }
    return a;
}

int func_with_nested_branch(int a)
{
    if (a < 100)
    {

        if (a > 1000)
        {
            a += 1;
        }
        a += 100;
    }
    return a;
}

int func_with_nested_branch_2(int a)
{
    if (a < 100)
    {
        a += 100;
    }
    else
    {
        if (a > 1000)
        {
            a += 1;
        }
        a += 100;
    }
    return a;
}

int func_with_branch(int a)
{
    if (a < 100)
    {
        if (a < 150)
        {
            a += 10;
        }
        a += 100;
    }
    else
    {
        a += 1;
    }
    a += 2;
    a += 3;
    if (a < 200)
    {
        a += 5;
    }
    return a;
}

int func_with_attributes(MyStruct s)
{
    if (s.value < 100)
    {
        s.value += 1;
    }
    else
    {
        s.value += -1;
    }
    s.value += 123;
    return s.value;
}