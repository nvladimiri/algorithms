#include <iostream>
#include <queue>
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
    priority_queue <pair <int, int> > pq;
    int x = 0;
    d[x] = 0;
    pq.push({ -d[x], x });
    while (!pq.empty()) {
        auto u = pq.top().second;
        pq.pop();
        if (vis[u])
            continue;
        vis[u] = true;
        for (auto e : adj[u])
            if (!vis[e.v])
                if (d[e.v] > d[u] + e.w) {
                    d[e.v] = d[u] + e.w;
                    pq.push({ -d[e.v], e.v });
                }
    }

    int y = n - 1;
    cout << d[y] << endl;
    return 0;
}