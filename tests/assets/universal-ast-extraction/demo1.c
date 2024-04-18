typedef struct
{
    int sub_value;
} SUB;

typedef struct
{
    int aaa;
    SUB sub;
} S;
int g_Config;

int basic_control_structures(S s, int a, int b[2], SUB sub_arr[2])
{

    if (a > 0)
    {
        a += 1;
        sub_arr[0].sub_value += g_Config;
        sub_arr[1].sub_value += g_Config + 3;
        if (a > 10)
        {
            a += 2;
            sub_arr[0].sub_value += g_Config;
        }
        else
        {
            a += 3;
            // return 0;
        }
    }
    // For loop
    for (int i = 0; i < 10; i++)
    {
        a += 1;
    }
    for (int i = 0; i < 114; i++)
    {
        if (a % 2 == 0)
        {
            break;
        }
        else if (a % 3 == 0)
        {
            break;
        }

        a += 1;
    }
    a = -10;

    // While loop
    while (a < 0)
    {
        a += 1;
    }
    while (1)
    {
        a += 1;
        if (a > 0)
        {
            break;
        }
    }
    while (11)
    {

        if (a > -100)
        {
            continue;
        }
        a += 1;
        if (a > 0)
        {
            break;
        }
    }

A:
    a += a;
    a += a;
    if (a < 113)
    {
        goto A;
    }

    return a;
}

