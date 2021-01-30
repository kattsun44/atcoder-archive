#include<iostream>
using namespace std;

int main() {
    int n;
    string ans="No";
    cin >> n;
    if ((n - 9) % 10 == 0 || n >= 90) ans = "Yes";
    cout << ans << endl;
	return 0;
}
