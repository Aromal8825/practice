// check if armstrong or not for 3 digit numbers  //
#include<stdio.h>
void main()
{
    int num, rem, power, sum = 0, temp;
    printf("enter a number : ");
    scanf("%d", &num);
    temp = num;
    while(num > 0)
    {
        rem = num % 10;
        num = num / 10;
        power = rem * rem * rem;
        sum = sum + power;
    }
    if( sum == temp)
    {
        printf("\n armstrong number ");
    }
    else
    {
        printf("\n not armstrong number ");
    }
}
