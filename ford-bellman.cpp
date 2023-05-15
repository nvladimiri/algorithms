#include <iostream>
#include <iterator>
#include <vector>
using namespace std;

int const infinity = 0x3F3F3F3F;

struct Edge { int v; int w; };

int main() {
    int n, m;
    cin >> n >> m;
    vector <vector <Edge> > adj(n);

    for (int j = 0; j < m; j++) {
        int u, v, w;
        cin >> u >> v >> w;
        u -= 1;
        v -= 1;
        adj[u].push_back({ v, w });
        adj[v].push_back({ u, w });
    }

    vector <int> d(n, infinity);
    vector <int> p(n, infinity);
    d[0] = 0;
    for (int k = 0; k < n - 1; k++) {
        for (int u = 0; u < n; u++)
            for (auto e : adj[u])
                if (d[e.v] > d[u] + e.w) {
                    d[e.v] = d[u] + e.w;
                    p[e.v] = u;
                }
    }

    int x = 0, y = n - 1;
    cout << d[y] << endl;
    vector <int> path;
    while (x != y) {
        y = p[y];
        path.push_back(y + 1);
    }
    copy(path.rbegin(), path.rend(),
        ostream_iterator <int>(cout, " "));
    cout << n << endl;
    return 0;
}