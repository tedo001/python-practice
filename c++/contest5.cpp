#include <bits/stdc++.h>
using namespace std;

using ll = long long;

bool possible(const vector<ll>& a, int T) {
    ll need = 1LL * ((int)a.size() - 1) * T;
    ll have = 0;

    if (T >= 31) {
        // Since ai <= 1e9 < 2^30,
        // q_i(T) = T - 1 for every i.
        return T >= (int)a.size();
    }

    ll pw = 1LL << T;

    for (ll x : a) {
        if (pw <= x)
            return false;

        ll v = pw - x;

        // floor(log2(v))
        int q = 63 - __builtin_clzll(v);

        have += q;

        if (have >= need)
            return true;
    }

    return have >= need;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<ll> a(n);

        for (ll &x : a)
            cin >> x;

        for (int T = 1; T <= 31; T++) {
            if (possible(a, T)) {
                cout << T << '\n';
                break;
            }
        }
    }

    return 0;
}
