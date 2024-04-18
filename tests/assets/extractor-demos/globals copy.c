typedef struct
{
    int abc;
} StructA;

int a = 32;
int b = 444;
int c = 123;
int *p = 0;
StructA st = {0};
StructA *pst = {0};
extern int extvar = 0;

int f(int);
int ff2()
{
}
int use_global(int y, float z)
{
    int x;
    int c = *p + y;
    a = 114514;
    f(b);
}

int use_global_2(int y, float z)
{
    int x[1919];
    int q = a;
    x[q];
    x[a];
    if (y > 114)
    {
        f(x[y]);
    }
    else
    {
        f(x[(int)z]);
    }
}

int main()
{
    StructA not_global = {0};
    return 0;
}