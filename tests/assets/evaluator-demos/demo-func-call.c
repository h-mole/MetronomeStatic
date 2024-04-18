typedef struct
{
    int attr;
} MyStruct;

int add_with_c(int a, int b)
{
    int c = 10;
    return a + b + c;
}

int swap(int *pa, int *pb)
{
    int c = *pa;
    *pa = *pb;
}

int get_attr_value(MyStruct *s)
{
    return s->attr + 1140;
}

int caller_pointer()
{
    MyStruct s;
    return get_attr_value(&s);
}

int main()
{
    int a = 10;
    int b = 20;
    int c = add_with_c(a, b);
    return c;
}