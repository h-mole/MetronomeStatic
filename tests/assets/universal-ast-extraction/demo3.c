int basic_control_structures(int a, int b[2])
{
    if (a > 0)
    {
        a = 1;
    }
    switch (a)
    {
    case 1:
        a += 1;
        break;
    case 2:
        a += 2;
    case 3:
        a += 3;
        break;
    default:
        break;
    }
}