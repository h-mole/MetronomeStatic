int main(int paramA, int paramB)
{
    if (paramA < 0)
    {
        return -1;
    }
    for (int i = 0; i < paramB; i++)
    {
        paramA += i;
    }
    return paramA;
}