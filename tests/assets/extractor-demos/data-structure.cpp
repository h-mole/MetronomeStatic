#include <iostream>
typedef struct
{
    int abc;
    char *s;
    struct
    {
        int d;
        char *ui;
    };
} StructA;

StructA a;

using namespace std;

class Box
{
public:
    double length;  // 长度
    double breadth; // 宽度
    double height;  // 高度
private:
    double volume = 123;
    // 成员函数声明
    double get(void);
    void set(double len, double bre, double hei);
};
// 成员函数定义
double Box::get(void)
{
    return length * breadth * height + a.abc;
}

int a123123(void)
{
    return a.d + a.abc;
}