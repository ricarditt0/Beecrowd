
#include <iostream>
#include <vector>
#include <array>
#include <algorithm>

using namespace std;

using Posicao = pair<int, int>;
using Padrao = array<Posicao, 3>;

vector<Padrao> sets;

void gerar_padroes() {
    // 9 padrões de três cartas idênticas
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            sets.push_back({{{i, j}, {i, j}, {i, j}}});
        }
    }

    // 12 padrões restantes
    vector<Padrao> outros = {
        {{{0,0}, {0,1}, {0,2}}},
        {{{1,0}, {1,1}, {1,2}}},
        {{{2,0}, {2,1}, {2,2}}},

        {{{0,0}, {1,0}, {2,0}}},
        {{{0,1}, {1,1}, {2,1}}},
        {{{0,2}, {1,2}, {2,2}}},

        {{{0,0}, {1,1}, {2,2}}},
        {{{0,1}, {1,2}, {2,0}}},
        {{{0,2}, {1,0}, {2,1}}},

        {{{0,2}, {1,1}, {2,0}}},
        {{{0,1}, {1,0}, {2,2}}},
        {{{0,0}, {1,2}, {2,1}}}
    };

    for (const auto& p : outros) {
        sets.push_back(p);
    }
}

int backtracking(vector<vector<int>>& matriz, int index) {
    if (index == (int)sets.size()) {
        return 0;
    }

    Padrao p = sets[index];

    int r1 = p[0].first;
    int c1 = p[0].second;

    int r2 = p[1].first;
    int c2 = p[1].second;

    int r3 = p[2].first;
    int c3 = p[2].second;

    int k;

    // Caso as três cartas sejam do mesmo tipo
    if (p[0] == p[1] && p[1] == p[2]) {
        k = matriz[r1][c1] / 3;
    }
    else {
        k = min({
            matriz[r1][c1],
            matriz[r2][c2],
            matriz[r3][c3]
        });
    }

    int best = 0;

    for (int i = k; i >= 0; i--) {

        // Remover o padrão da matriz
        matriz[r1][c1] -= i;
        matriz[r2][c2] -= i;
        matriz[r3][c3] -= i;

        // Chamada recursiva
        int resultado = i + backtracking(matriz, index + 1);

        best = max(best, resultado);

        // Restaurar a matriz
        matriz[r1][c1] += i;
        matriz[r2][c2] += i;
        matriz[r3][c3] += i;
    }

    return best;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    gerar_padroes();

    int n;

    while (cin >> n && n != 0) {

        vector<vector<int>> matriz(3, vector<int>(3, 0));

        for (int i = 0; i < n; i++) {
            string quantidade, forma;
            cin >> quantidade >> forma;

            int linha = 0;
            int coluna = 0;

            if (forma == "circulo" || forma == "circulos")
                linha = 0;
            else if (forma == "quadrado" || forma == "quadrados")
                linha = 1;
            else if (forma == "triangulo" || forma == "triangulos")
                linha = 2;

            if (quantidade == "um")
                coluna = 0;
            else if (quantidade == "dois")
                coluna = 1;
            else if (quantidade == "tres")
                coluna = 2;

            matriz[linha][coluna]++;
        }

        cout << backtracking(matriz, 0) << '\n';
    }

    return 0;
}
