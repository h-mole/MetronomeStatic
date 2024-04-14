typedef struct
{
    int sub_value;
    unsigned int v2;
} SUB;

typedef struct
{
    int aaa;
    SUB sub;
} S;

int add_with_c(int a, int b)
{
    int c = 20;
    return a + b + c;
}

int main()
{
    int a = 10;
    int b = 20;
    int c = add_with_c(a, b);
    return c;
}