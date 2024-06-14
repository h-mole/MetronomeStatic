void test_unary_operators(int a, int *p)
{
    +a;
    -a;
    // logics
    !(a);
    // pointer
    *p;
    &a;
    // arithmetic
    a++;
    ++a;
    a--;
    --a;
}

void test_assignments(int a, int b)
{
    // assignments;
    a = b;
    a += b;
    a -= b;
    a *= b;
    a /= b;
    a %= b;
    a <<= b;
    a >>= b;
    a &= b;
    a |= b;
    a ^= b;
}

void test_binary_operators(int a, int b)
{
    // arithmetic
    a + b;
    a - b;
    a *b;
    a / b;
    a % b;
    // bitwise
    a & b;
    a | b;
    a ^ b;
    a << b;
    a >> b;

    // relationships
    a == b;
    a != b;
    a >= b;
    a <= b;
    a < b;
    a > b;

    // logics
    a || b;
    a &&b;
}

int main()
{
    int a = 10, b = 20;
    int add, sub, mul, div, mod, and, or, xor, not ;

    // https://www.runoob.com/cprogramming/c-operators.html

    return 0;
}
