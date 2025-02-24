/**
*    author:  kattsun
*    created: 27-01-2021 20:41:38
**/

#include <iostream>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
   cin.tie(0);
   ios_base::sync_with_stdio(false);

   string N,N0,N1,ans="No";
   int cnt0=0,cnt1=0;

   cin >> N;
   N0 = N[0];
   N1 = N[1];
   rep(i, 2) {
       if (N[i] == N[i+1]) cnt0++; 
       if (N[i+1] == N[i+2]) cnt1++; 
   }

   if (cnt0 == 2 || cnt1 == 2) ans = "Yes";
   cout << ans << endl;

   return 0;
}