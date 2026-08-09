#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        long long a, b, c;
        cin >> a >> b >> c;

        vector<long long> v = {a, b, c};
        sort(v.begin(), v.end());

        auto x = v[0];
        auto y = v[1];
        auto z = v[2];

        cout << min(z - x, y) << '\n';
    }

    return 0;
}
