typedef struct
{
    int v;
} StructB;
typedef struct
{
    StructB a;
    StructB arr_property[10];
    StructB *arr_ptr_prop[10];
    StructB *ptr;
} StructA;

StructA g_A = {0};

int main()
{
    int c = 0;
    g_A.arr_property[0].v = 123;
    g_A.ptr->v = 123;
    g_A.arr_ptr_prop[c]->v = g_A.arr_property[c].v;
    return 0;
}