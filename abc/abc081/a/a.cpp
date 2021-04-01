/**
*    author:  kattsun
*    created: 26-01-2021 19:29:28
**/

#include <iostream>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    int s,s0,s1,s2;
    cin >> s;
    s0 = s % 100 % 10;
    s1 = (s - s0) % 100 / 10;
    s2 = (s- s0 + s1) / 100;
    cout << s0 + s1 + s2 << endl;
    return 0;
}