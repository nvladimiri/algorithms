#include <iostream>
#include <set>
#include <utility>
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
    vector <bool> vis(n);
    set <pair <int, int> > s;
    int x = 0;
    d[x] = 0;
    s.insert({ d[x], x });
    while (!s.empty()) {
        auto u = s.begin()->second;
        s.erase(s.begin());
        vis[u] = true;
        for (auto e : adj[u])
            if (!vis[e.v])
                if (d[e.v] > d[u] + e.w) {
                    s.erase({ d[e.v], e.v });
                    d[e.v] = d[u] + e.w;
                    s.insert({ d[e.v], e.v });
                }
    }

    int y = n - 1;
    cout << d[y] << endl;
    return 0;
}