#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const ll MOD = 998244353;
const int MAXN = 1000005;

ll fact[MAXN], invfact[MAXN];

ll modpow(ll a, ll e) {
    ll res = 1;
    while (e) {
        if (e & 1)
            res = res * a % MOD;
        a = a * a % MOD;<C-S-Del><C-S-Del><C-S-Del><C-S-Del>)
        return (x == 0 ? 1 : 0);

    if (x < k)
        return 0;

    return C(x - 1, k - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Precompute factorials.
    fact[0] = 1;

    for (int i = 1; i < MAXN; i++)
        fact[i] = fact[i - 1] * i % MOD;

    invfact[MAXN - 1] = modpow(fact[MAXN - 1], MOD - 2);

    for (int i = MAXN - 1; i >= 1; i--)
        invfact[i - 1] = invfact[i] * i % MOD;

    int T;
    cin >> T;

    while (T--) {
        int n;
        string s;

        cin >> n >> s;

        int zeros = 0;
        int ones = 0;
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

        ll ans = 0;

        // Case 1: resulting string starts with 0.
        {
            int zeroRuns = (runs + 1) / 2;
            int oneRuns = runs / 2;

            ll a = ways(zeros, zeroRuns);
            ll b = ways(ones, oneRuns);

            ans = (ans + a * b) % MOD;
        }

        // Case 2: resulting string starts with 1.
        {
            int oneRuns = (runs + 1) / 2;
            int zeroRuns = runs / 2;

            ll a = ways(ones, oneRuns);
            ll b = ways(zeros, zeroRuns);

            ans = (ans + a * b) % MOD;
        }

        cout << ans << '\n';
    }

    return 0;
}
