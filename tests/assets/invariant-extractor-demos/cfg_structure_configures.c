int cfg_structure_configures(int a, int max, int min)
{
    int value = -1;
    a = a + 20;
    if (min <= a && a <= max)
    {
        value = a;
    }
    else if (a > max)
    {
        value = max;
    }
    else
    {
        value = min;
    }
    return value;
}