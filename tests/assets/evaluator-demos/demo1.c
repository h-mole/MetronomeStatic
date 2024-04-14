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
int use_config(S s)
{

    int a = g_Config;
    s.aaa += 1;
    s.sub.sub_value += 2;
    int b[2] = {
        0,
        1,
    };
    b[0] += 1;
    SUB sub_arr[2] = {{0}, {1}};
    sub_arr[0].sub_value += g_Config;

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
    }
}