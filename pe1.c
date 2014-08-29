// Demo for euler problem 1.
// From here: https://code.stypi.com/fossilet/duanrenyang
// Since Thu Feb 27 17:37:02 CST 2014

#include <stdio.h>

int calculate(int n)
{
    int sum=0;
    for(int i=1;i<=n;i++) {
        if(i%3==0||i%5==0) {
            sum+=i;
        }
    }
    return sum;
}


int calculate1(int n)
{
    int sum, sum3, sum5, sum15 = 0;
    for(int i=0;i<=n;i=i+3) {
        sum3+=i;
    }
    for(int j=0;j<=n;j=j+5) {
        sum5+=j;
    }
    for(int i = 0; i <= n; i+=15) {
        sum15 += i;
    }
    sum=sum3+sum5 - sum15;
    return sum;
}

// TODO: use summation formula of arithmetic progression.

int main() {
    int n = 999;
    printf("%d\n", calculate(n));
    printf("%d\n", calculate1(n));
}
