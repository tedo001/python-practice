#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve() {
    int n;
    ll k;
    cin >> n >> k;

    string s;
    cin >> s;

    int m = 2 * n;

    // Number of potatoes on even positions.
    int even = 0;
    for (int i = 0; i < m; i++) {
        if (s[i] == '1' && (i + 1) % 2 == 0)
            even++;
    }

    if (k <= 2 * n) {
        while (k--) {
            string t = s;

            for (int i = 0; i < m; i++) {
                int j = (i + 1) % m;

                if (s[i] == '1' && s[j] == '0') {
                    t[i] = '0';
                    t[j] = '1';
                }
            }

            s = t;
        }
    } else {
        // After 2n rounds the movement pattern becomes periodic.
        k %= 2 * n;

        while (k--) {
            string t = s;

            for (int i = 0; i < m; i++) {
                int j = (i + 1) % m;

                if (s[i] == '1' && s[j] == '0') {
                    t[i] = '0';
                    t[j] = '1';
                }
            }

            s = t;
        }
    }

    int red = 0, blue = 0;

    for (int i = 0; i < m; i++) {
        if (s[i] == '1') {
            if ((i + 1) % 2 == 0)
                red++;
            else
                blue++;
        }
    }

    cout << red << ' ' << blue << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        solve();
    }

    return 0;
}
