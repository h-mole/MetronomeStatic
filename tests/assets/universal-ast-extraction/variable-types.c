typedef struct A_
{
    int a;
    int (*func)(int, int);
} A;

int (*g_func)(int, int);

int register_func(int (*fptr)(int, int))
{
    g_func = fptr;
}
int add(int a, int b)
{
    return a + b;
}
int main()
{
    int a;
    int b, c = 10;
    int d = 10, e;
    register_func(add);
    A a1;
    a1.func = add;
    a1.func(0, 2);
}