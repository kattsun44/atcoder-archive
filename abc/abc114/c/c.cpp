/**
*    author:  kattsun
*    created: 07-02-2021 18:05:57
**/

#include <iostream>
#include <vector>
using namespace std;
using ll = long long;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

void func(ll N, ll cur, ll use, ll &counter) {
    // base case
    if (cur > N) return;
    if (use == 0b111) ++counter;

    func(N, cur * 10 + 7, use | 0b100, counter);
    func(N, cur * 10 + 5, use | 0b010, counter);
    func(N, cur * 10 + 3, use | 0b001, counter);
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    ll N, counter=0;
    cin >> N;
    func(N, 0, 0, counter);
    cout << counter << endl;
    return 0;
}