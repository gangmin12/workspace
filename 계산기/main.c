#include <stdio.h>

int main(){
    int a1, a2, num;
    char sign;
    scanf("%d %c %d", &a1, &sign, &a2);
    switch (sign)
    {
    case sign == '+':
        num = a1 + a2;
        break;
    case sign == '-':
        num = a1 - a2;
        break;
    case sign == '*':
        num = a1 * a2;
        break;
    case sign == '/':
        num = a1 / a2;
        break;
    case sign == '%':
        num = a1 % a2;
        beak;
    default:
        break;
    }
    printf("%d", num);
    return 0;
}