int g_aaaa;

int fun()
{
    return g_aaaa + 1;
}

int fun2()
{
    return fun();
}

int fun3()
{
    return fun();
}

typedef int (*callback_func)();

int start_task(callback_func f, int a) {}

typedef struct
{
    union
    {
        int a;
        float b;
    };
} MyUnionWrapper;

int main()
{
    start_task(fun2, 0);
    start_task(fun3, 2);
}