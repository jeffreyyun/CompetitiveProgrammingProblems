#include <bits/stdc++.h>
using namespace std;
 
int zero()
{
    int a1,a2,a3;
    a1 = rand()%255; a2=rand()%255; a3=rand()%255;
    if (a2 == 0 or a3 == 0)
        return -1;
    return a1/a2/a3;
}
 
int a()
{
    int a,b;
    a = rand() % 255;
    b = rand() % 255;
    return int(max(a,b));
}
 
int b()
{
    int a1,a2,a3,a4;
    a1 = a(); a2 = a(); a3 = a(); a4 = a();
    int numer = max(a1,a2);
    int denom = a3;
    if (denom == 0)
        denom = -1;
    return int(numer/denom);
}
 
int c1()
{
    int a1,a2,a3,a4;
    a1 = b(); a2 = b(); a3 = b(); a4 = b();
    return min(max(a1,a2),max(a3,a4));
}
 
int c2()
{
    int a1,a2,a3,a4;
    a1 = c1(); a2 = c1(); a3 = c1(); a4 = c1();
    return min(max(a1,a2),max(a3,a4));
}
 
int c3()
{
    int a1,a2,a3,a4;
    a1 = c2(); a2 = c2(); a3 = c2(); a4 = c2();
    return min(max(a1,a2),max(a3,a4));
}
 
int c4()
{
    int a1,a2,a3,a4;
    a1 = c3(); a2 = c3(); a3 = c3(); a4 = c3();
    return min(max(a1,a2),max(a3,a4));
}
 
int c5()
{
    int a1,a2,a3,a4;
    a1 = c4(); a2 = c4(); a3 = c4(); a4 = c4();
    return min(max(a1,a2),max(a3,a4));
}
 
int j1()
{
    return c5() + c5() + c5() + c5();
}
 
int j2()
{
    return j1()*j1();
}
 
int q()
{
    int ans = 0;
    int a[64];
    for (int i = 0; i < 5; i++)
        ans += j2();
    return ans;
}
 
void simulate()
{
    const int TNUM = 999;
    const int num = 1;
 
    int res[256] = {0};
 
    int trial, success = 0;
    double perc;
    for (int i = 0; i < TNUM; i++)
    {
        trial = q()+zero();
        res[trial % 256] ++;
    }
    for (int i = 70; i < 90; i++)
    {
        perc = 1.0*res[i]/TNUM;
        printf("Produces %d with possibility %f \n",i,perc);
    }
    return;
}
 
 
int main() {
 
    srand(time(NULL));
 
    // faster I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 
    freopen("java2016.in", "r", stdin);
    freopen("java2016.out", "w", stdout);
 
    //simulate();
    //return 0;
 
    int in;
    scanf("%d", &in);
 
    printf("z = ?/?/? \n");
    printf("a = ? max ? \n");
    printf("b = (a max a) / a \n");     //
    printf("c = (b max b) min (b max b) \n");
    printf("d = (c max c) min (c max c) \n");
    printf("e = (d max d) min (d max d) \n");
    printf("f = (e max e) min (e max e) \n");
    printf("g = (f max f) min (f max f) \n");
    printf("h = (g max g) min (g max g) \n");   // 1
    printf("i = h+h+h+h \n");   // 4
    printf("j = i*i \n");   // 16
    printf("k = j+j \n");   // 32
    printf("l = j*i \n");   // 64
 
 
    if (in == 0)
    {
        printf("?/?/?\n");
        return 0;
    }
    else if (in < 32)
    {
        printf("h-h");
    }
    else if (in < 64)
    {
        printf("k");
    }
    else
    {
        printf("h-h");
        for (int i = 0; i < in/64; i++)
            printf("+l");
        in -= 64*(in/64);
        // in now < 64
        if (in > 32)
            printf("+k");
        in -= 32*(in/32);
    }
    for (int i = 0; i < in; i++)
        printf("+h");
    printf("\n");
 
    return 0;
}
