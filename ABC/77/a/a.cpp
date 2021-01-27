/**
*    author:  kattsun
*    created: 27-01-2021 21:12:00
**/

#include <iostream>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
   cin.tie(0);
   ios_base::sync_with_stdio(false);
   string c1,c2,ans="YES";
   cin >> c1 >> c2;
   rep(i, 3) {
       if (c1[i] != c2[2-i]) ans = "NO";
   }
   cout << ans << endl;
   return 0;
}