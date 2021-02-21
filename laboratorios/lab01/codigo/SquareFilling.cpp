#include <bits/stdc++.h>
using namespace std;
#define vvi vector<vector<string>>

unordered_map<int, string> colors = {
    {1    = '\33[31m'},
    {2  = '\33[32m'},
    {3 = '\33[33m'},
    {4   = '\33[34m'},
    {5 = '\33[35m'}
};


void print(vvi &square)
{
    for (const auto &row : square)
    {
        for (const auto &col : row)
        {
            cout << setw(2) << col;
        }
        cout << "\n";
    }
    cout << "\n";
}

void color(vvi &matrix, int i, int j, string color)
{
    matrix[i][j] = color;
}

void clear(vvi &matrix, int i, int j)
{
    matrix[i][j] = " ";
}

string randomize(vvi &matrix, boolean vertical, int i, int j){
    int choice;

    if (vertical) {
        choice = rand(1,5);
        while (j != 0 && colors[choice] == colors[matrix[i][j-1]] || colors[choice] == colors[matrix[i][j-1]]){
            choice = rand(1,5);
        }
    }
    else{

    }

    return choice;
}


int fill(vvi &square, int i, bool vertical)
{
    // if (square[0][square.size()-1] FALTA && square[1][square.size()-1] FALTA) return 1;
    if (i == square.size() - 1)
    {
        print(square);
        return 1;
    }

    color(square, 0, i, VIOLET);
    color(square, 1, i, YELLOW);
    int vertical = fill(square, i + 1, true);
    clear(square, 0, i);
    clear(square, 1, i);

    int horizontal = 0;
    if (i + 1 < square.size()){
        color(square, 0, i, RED);
        color(square, 0, i + 1, RED);
        color(square, 1, i, VIOLET);
        color(square, 1, i + 1, YELLOW);
        horizontal = fill(square, i + 2, false);
        clear(square, 0, i);
        clear(square, 0, i + 1);
        clear(square, 1, i);
        clear(square, 1, i + 1);
    }

    return vertical + horizontal;
}

int main()
{
    int n;
    cin >> n;
    vvi square(2, vector<string>(n, " "));
    cout << "Numero de maneras: " << fill(square, 0, false) << endl;
}

// Implementen  un  algoritmo  recursivo
// para  encontrar  de  cuántas  formas  se
// puede llenar un rectángulo de 2xn cm2 con rectángulos de 1x2 cm².



