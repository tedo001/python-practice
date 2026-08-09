#include <bits/stdc++.h>
using namespace std;

const long long MOD = 998244353;

long long countPattern(const string& s, int start) {
    long long ways = 0;
    for (int first = 0; first <= 1; first++) {
        bool ok = true;

        for (int i = start, step = 0; i < (int)s.size(); i += 2, step++) {
            int expected = first ^ (step & 1);

            if (s[i] != '?' && s[i] - '0' != expected) {
                ok = false;
                break;
            }
        }

        if (ok) ways++;
}

    return ways;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n;
        string s;
        cin >> n >> s;

        long long oddWays = countPattern(s, 0);
        long long evenWays = countPattern(s, 1);

        cout << (oddWays * evenWays) % MOD << '\n';
    }

    return 0;
}
