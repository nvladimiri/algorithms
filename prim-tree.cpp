#include <iostream>
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
    vector <bool> vis(n);
    int u = 0;
    d[u] = 0;
    int res = 0;
    while (u != -1) {
        if (u != 0)
            cout << u + 1 << " " <<
            p[u] + 1 << " " << d[u] << endl;
        res += d[u];
        vis[u] = true;
        for (auto e : adj[u])
            if (d[e.v] > e.w) {
                d[e.v] = e.w;
                p[e.v] = u;
            }
        u = -1;
        for (int v = 0; v < n; v++)
            if (!vis[v])
                if (u == -1 || d[u] > d[v])
                    u = v;
    }
    cout << res << endl;
    return 0;
}