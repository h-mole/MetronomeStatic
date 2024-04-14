int f(int a, int b)
{
    return a * b;
}

int main(int paramA, int paramB)
{
    return paramA + paramB + f(paramA, paramB);
}