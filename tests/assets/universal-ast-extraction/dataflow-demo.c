int demo1(int x, int y, int z)
{
    if (x > 1)
    {
        x += z;
    }
    while (z < 0)
    {
        if (y < 0)
        {
            y += 2;
        }
        else
        {
            z++;
        }
    }
}