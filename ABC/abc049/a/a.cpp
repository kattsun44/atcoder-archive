/**
*    author:  kattsun
*    created: 29-01-2021 21:57:21
**/

#include <iostream>
using namespace std;
using ll = long long;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
   cin.tie(0);
   ios_base::sync_with_stdio(false);
   char c, a[5] = {'a', 'i', 'u', 'e', 'o'};
   string ans="consonant";
   cin >>c;
   rep(i,5) {
       if (c == a[i]) ans = "vowel";
   }
   cout << ans << endl;
   return 0;
}