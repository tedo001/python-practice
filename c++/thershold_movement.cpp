#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<long long> w(n + 1);

        for (int i = 1; i <= n; i++)
            cin >> w[i];

        if (n % 2 == 1) {
            cout << "NO\n";
            continue;
        }

        long long maxEven = 0;
        long long minOdd = 1e18;

        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0)
                maxEven = max(maxEven, w[i]);
            else
                minOdd = min(minOdd, w[i]);
        }

        if (maxEven < minOdd)
            cout << "YES\n";
        else
            cout << "NO\n";
    }

    return 0;
}
