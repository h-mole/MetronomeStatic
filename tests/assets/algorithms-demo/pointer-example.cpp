

class Number
{
public:
    Number(int value) : value(value) {}

    int get() const
    {
        return value;
    }

private:
    int value;
};

class One : public Number
{
public:
    One() : Number(1) {}
};

class Two : public Number
{
public:
    Two() : Number(2) {}
};

class C
{
public:
    static void main()
    {
        C *c = new C(); // o_l_34 (o_3)
        (*c).m();
    }

    void m()
    {
        One *n1 = new One(); // o_12
        Two *n2 = new Two(); // o_13
        Number *x = (*this).id(n1);
        Number *y = (*this).id(n2);
        (*x).get();
    }

    Number *id(Number *n)
    {
        return n;
    }
};

int main()
{
    C::main();
}