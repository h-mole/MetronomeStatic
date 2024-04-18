int read_pointer(int *value)
{
    int a = *value;
    *value += 1;

    int *ptr;
    ptr = value;
    *ptr += 1;
}

typedef struct
{
    int a;
    int powers[3];
} MyStruct;

int read_pointer_structural(int v, MyStruct *stru)
{
    stru->a = v;
    stru->powers[0] = stru->powers[1] + stru->powers[2];
    return 0;
}