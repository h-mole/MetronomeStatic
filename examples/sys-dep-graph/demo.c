int *CONST_1;
int Add(int *a, int *b)
{
    *a = (*a) + (*b);
}

int Increment(int *z)
{
    Add(z, 1);
}

int A(int *x, int *y)
{
    Add(x, y);
    Increment(y);
}

int main()
{
    int sum = 0;
    int i = 1;
    while (i < 11)
    {
        A(&sum, &i);
        // {
        //     i += 1;
        //     i++;
        // }
    }
}