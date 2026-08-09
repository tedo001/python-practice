#include <bits/stdc++.h>
using namespace std;

using ll = long long;

bool possible(const vector<ll>& a, int T) {
    int n = (int)a.size();

    // We process the requirements from largest to smallest.
    vector<ll> need = a;
    sort(need.rbegin(), need.rend());

    int ptr = 0;

    // Powers 2^30, 2^31, ... are larger than every ai.
    // If T > 30, these largest powers can immediately
    // satisfy one requirement each.
    int big = max(0, T - 30);

    if (big > n)
        big = n;

    ptr = big;

    // The first 'big' largest requirements are satisfied
    // by the huge powers.
    //
    // Now only powers 2^29 ... 2^0 remain.
    for (int p = min(29, T - 1); p >= 0 && ptr < n; p--) {
        ll power = 1LL << p;

        if (power >= need[ptr]) {
            ptr++;
        } else {
            need[ptr] -= power;
        }
    }

    return ptr == n;
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

        sort(a.rbegin(), a.rend());

        // At least n operations are needed because
        // every positive number needs at least one chosen round.
        //
        // n + 30 is always enough because the first n powers
        // can be chosen larger than every ai.
        for (int T = n; T <= n + 30; T++) {
            if (possible(a, T)) {
                cout << T << '\n';
                break;
            }
        }
    }

    return 0;
}
