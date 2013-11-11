#include <stdio.h>
#include <limits.h>

int ntest,a,b,c,d;

int min(int a,int b) {
    return a<b?a:b;
}

int gcd(int a,int b) {
    return b==0?a:gcd(b,a%b);
}

int check(int a,int b) {
    int ret = 0,ca = 0,cb = 0;
    for (;;) {
        if (ca==c || cb==c) return ret;
        if (cb==b) cb = 0;
        else if (ca==0) ca = a;
        else {
            int dt = min(b-cb,ca);
            ca -= dt; cb += dt;
        }
        ret++;
    }
}

int main() {
    scanf("%d",&ntest);
    while (ntest--) {
        scanf("%d%d%d",&a,&b,&c);
        d = gcd(a,b);
        if (c%d!=0 || c>a && c>b) printf("-1\n");
        else {
            int ans = check(a,b);
            ans = min(ans,check(b,a));
            printf("%d\n",ans);
        }
    }
    return 0;
}
