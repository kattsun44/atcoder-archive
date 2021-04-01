/**
*    author:  kattsun
*    created: 27-01-2021 20:58:56
**/

#include <iostream>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
   cin.tie(0);
   ios_base::sync_with_stdio(false);
   string X, Y, ans="=";
   cin >> X >> Y;

   if (X > Y) ans = ">";
   else if (X < Y) ans = "<";

   cout << ans << endl;

   return 0;
}