#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int mod(ll x, int n) {
    x %= n;
    if (x < 0) x += n;
    return (int)x;
}

ll extgcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }

    ll x1, y1;
    ll g = extgcd(b, a % b, x1, y1);

    x = y1;
    y = x1 - (a / b) * y1;

    return g;
}

int inv_mod(ll a, int n) {
    ll x, y;
    extgcd(a, n, x, y);
    return mod(x, n);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string type;
    cin >> type;

    int T;
    cin >> T;

    while (T--) {
        int n;
        cin >> n;

        vector<string> a(n);
        int black = 0;

        for (int i = 0; i < n; i++) {
            cin >> a[i];
            for (char c : a[i])
                black += (c == '#');
        }

        int total = n * n;

        if (type == "first") {
            int rx, cx;
            cin >> rx >> cx;

            // 0-based target
            --rx;
            --cx;

            // Choose the minority color.
            char minority;

            if (black < total - black)
                minority = '#';
            else
                minority = '.';

            int m = 0;
            ll sumR = 0, sumC = 0;

            for (int r = 0; r < n; r++) {
                for (int c = 0; c < n; c++) {
                    if (a[r][c] == minority) {
                        m++;
                        sumR += r;
                        sumC += c;
                    }
                }
            }

            int invM = inv_mod(m, n);

            // Current centroid.
            int cr = (sumR % n) * 1LL * invM % n;
            int cc = (sumC % n) * 1LL * invM % n;

            // We need the SUM to change by:
            // m * (target - current_centroid)
            int dr = mod(1LL * m * (rx - cr), n);
            int dc = mod(1LL * m * (cx - cc), n);

            // If no change is needed, swapping a cell with itself works.
            if (dr == 0 && dc == 0) {
                for (int r = 0; r < n; r++) {
                    bool done = false;

                    for (int c = 0; c < n; c++) {
                        if (a[r][c] == minority) {
                            cout << r + 1 << ' ' << c + 1 << ' '
                                 << r + 1 << ' ' << c + 1 << '\n';
                            done = true;
                            break;
                        }
                    }

                    if (done) break;
                }

                continue;
            }

            bool found = false;

            // Find minority cell A and majority cell B
            // such that B - A = (dr, dc) mod n.
            for (int r = 0; r < n && !found; r++) {
                for (int c = 0; c < n && !found; c++) {
                    if (a[r][c] != minority)
                        continue;

                    int nr = (r + dr) % n;
                    int nc = (c + dc) % n;

                    if (a[nr][nc] != minority) {
                        cout << r + 1 << ' ' << c + 1 << ' '
                             << nr + 1 << ' ' << nc + 1 << '\n';

                        found = true;
                    }
                }
            }
        } else {
            // Second run: find centroid of minority color.
            int minorityCount = min(black, total - black);

            char minority;

            if (black == minorityCount)
                minority = '#';
            else
                minority = '.';

            ll sumR = 0, sumC = 0;
            int m = 0;

            for (int r = 0; r < n; r++) {
                for (int c = 0; c < n; c++) {
                    if (a[r][c] == minority) {
                        m++;
                        sumR += r;
                        sumC += c;
                    }
                }
            }

            int invM = inv_mod(m, n);

            int rx = (sumR % n) * 1LL * invM % n;
            int cx = (sumC % n) * 1LL * invM % n;

            cout << rx + 1 << ' ' << cx + 1 << '\n';
        }
    }

    return 0;
}
