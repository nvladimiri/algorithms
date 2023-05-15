#include <iostream>
#include <vector>
using namespace std;

vector <vector <int> > adj;
vector <bool> vis;
int n, m;

void dfs(int v) {
    if (vis[v])
        return;
    vis[v] = true;
    cout << "in  " << v + 1 << endl;
    for (auto u : adj[v]) {
        dfs(u);
    }
    cout << "out " << v + 1 << endl;
}

int main() {
    cin >> n >> m;
    adj = vector <vector <int> >(n);

    for (int j = 0; j < m; j++) {
        int u, v;
        cin >> u >> v;
        u -= 1;
        v -= 1;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vis = vector <bool>(n);
    dfs(0);

    return 0;
}