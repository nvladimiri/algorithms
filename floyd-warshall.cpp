#include <iostream>
#include <vector>
using namespace std;

int const infinity = 0x3F3F3F3F;

int main() {
    int n, m;
    cin >> n >> m;
    vector <vector <int> > a(n,
        vector <int>(n, infinity));
    for (int j = 0; j < m; j++) {
        int u, v, w;
        cin >> u >> v >> w;
        u -= 1;
        v -= 1;
        a[u][v] = w;
        a[v][u] = w;
    }

    vector <vector <int> > p(n, vector <int>(n));
    for (int i = 0; i < n; i++) {
        a[i][i] = 0;
        for (int j = 0; j < n; j++)
            p[i][j] = j;
    }

    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (a[i][j] > a[i][k] + a[k][j]) {
                    a[i][j] = a[i][k] + a[k][j];
                    p[i][j] = p[i][k];
                }

    int x = 0, y = n - 1;
    cout << a[x][y] << endl;
    while (x != y) {
        cout << x + 1 << " ";
        x = p[x][y];
    }
    cout << x + 1 << endl;
    return 0;
}