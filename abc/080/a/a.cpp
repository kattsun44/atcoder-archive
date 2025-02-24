/**
*    author:  kattsun
*    created: 27-01-2021 21:06:18
**/

#include <iostream>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
   cin.tie(0);
   ios_base::sync_with_stdio(false);
   int t,a,b;
   cin >> t >> a >> b;
   cout << min(t*a, b) << endl;
   return 0;
}