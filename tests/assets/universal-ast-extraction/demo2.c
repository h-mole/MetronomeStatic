int basic_control_structures(int a, int b[2])
{
    if (a > 0)
    {
        a = 1;
    }
    else if (a < 0)
    {
        a = 2;
    }
    else
    {
        a = 3;
    }

    if (a > 0)
    {
        return a;
    }
    else if (a < 0)
    {
        return -a;
    }
    else
    {
        return 0;
    }
}