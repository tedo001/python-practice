#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const ll MOD = 998244353;
const int MAXN = 1000005;

ll fact[MAXN], invfact[MAXN];

ll modpow(ll a, ll e) {
    ll res = 1;

    while (e > 0) {
        if (e & 1)
            res = res * a % MOD;

        a = a * a % MOD;
        e >>= 1;
    }

    return res;
}

ll C(int n, int k) {
    if (k < 0 || k > n)
        return 0;

    return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Factorials
    fact[0] = 1;

    for (int i = 1; i < MAXN; i++)
        fact[i] = fact[i - 1] * i % MOD;

    // Inverse factorials
    invfact[MAXN - 1] = modpow(fact[MAXN - 1], MOD - 2);

    for (int i = MAXN - 1; i >= 1; i--)
        invfact[i - 1] = invfact[i] * i % MOD;

    int T;
    cin >> T;

    while (T--) {
        int n;
        string s;

        cin >> n >> s;

        int zeros = 0, ones = 0;
        int transitions = 0;

        for (char c : s) {
            if (c == '0')
                zeros++;
            else
                ones++;
        }

        for (int i = 1; i < n; i++) {
            if (s[i] != s[i - 1])
                transitions++;
        }

        int runs = transitions + 1;

        // Number of runs of each color.
        int zeroRuns, oneRuns;

        if (s[0] == '0') {
            zeroRuns = (runs + 1) / 2;
            oneRuns = runs / 2;
        } else {
            oneRuns = (runs + 1) / 2;
            zeroRuns = runs / 2;
        }

        // Split zeros and ones into their required non-empty runs.
        ll ans = C(zeros - 1, zeroRuns - 1)
               * C(ones - 1, oneRuns - 1) % MOD;

        cout << ans << '\n';
    }

    return 0;
}
