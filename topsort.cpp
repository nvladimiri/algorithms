#include <iostream>
#include <vector>
using namespace std;

vector <vector <int> > adj;
vector <int> vis;
vector <int> order;
int n, m;

enum { fresh, busy, done };

bool dfs(int v) {
    if (vis[v] != fresh)
        return vis[v] == done;
    vis[v] = busy;
    for (auto u : adj[v])
        if (!dfs(u))
            return false;
    order.push_back(v);
    vis[v] = done;
    return true;
}

int main() {
    cin >> n >> m;
    adj = vector <vector <int> >(n);
    for (int j = 0; j < m; j++) {
        int u, v;
        cin >> u >> v;
        u -= 1;
        v -= 1;
        adj[v].push_back(u);
    }

    vis = vector <int>(n);
    bool ok = true;
    for (int v = 0; v < n; v++)
        ok &= dfs(v);

    if (ok) {
        cout << "YES" << endl;
        for (auto v : order)
            cout << v + 1 << " ";
        cout << endl;
    }
    else
        cout << "NO" << endl;

    return 0;
}