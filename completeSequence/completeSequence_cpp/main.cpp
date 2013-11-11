#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN = 100+5;

int n,m,s[MAXN][MAXN];

int main() {
  int ncase;
  scanf("%d",&ncase);
  while (ncase--) {
    scanf("%d%d",&n,&m);
    for (int i = 0; i<n; i++)
      scanf("%d",&s[0][i]);
    for (int i = 1; i<n; i++)
      for (int j = 0; i+j<n; j++)
        s[i][j] = s[i-1][j+1]-s[i-1][j];
    for (int i = 1; i<=m; i++)
      s[n-1][i] = s[n-1][0];
    for (int i = n-2; i>=0; i--)
      for (int j = 0; j<m; j++)
        s[i][n-i+j] = s[i][n-i+j-1]+s[i+1][n-i+j-1];
    for (int i = 0; i<m-1; i++)
      printf("%d ",s[0][n+i]);
    printf("%d\n",s[0][n+m-1]);
  }
  return 0;
}
