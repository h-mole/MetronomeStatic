int input();
int main(int x, int y, int z)
{
    x = x + input();
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