#include <bits/stdc++.h>

#define D(x) cout << #x << " = " << x << endl;
#define ios ios_base::sync_with_stdio(0), cin.tie(0);
#define forn(x, n) for (int i = x; i < (int)n; ++i)
#define all(v) v.begin(), v.end()
#define allgreater(v) v.begin(), v.end(), greater<int>()
#define formap(map) for (const auto &[key, value] : map)
#define ms(ar, val) memset(ar, val, sizeof ar)
#define vvi vector<vector<int>>
typedef long long ll;
typedef long double ld;

using namespace std;

int n;

bool isSafe(vvi &board, int x, int y){
    //arriba, lados
    for(int i = 0; i < n; ++i){
        if(board[x][i]) return false; //fila
        if(board[i][y]) return false; //columna
    }

    //Diagonales
    for(int i = x, j = y; i < n && j < n; ++i, ++j){
        if(board[i][j]) return false; 
    }

    for(int i = 0; i <= x && i <= y && x - i >= 0 && y - i >= 0; ++i){
        if(board[x - i][y - i]) return false; 
    }

    for(int i = 0, j = y; i < n && (y - (y - j)) >= 0 && (x + i) < n; ++i, --j){
        if(board[x + i][y - (y - j)]) return false; 
    }

    for(int i = x, j = 0; (x - (x -i)) >= 0 && j < n && (y + j) < n; --i, ++j){
        if(board[x - (x -i)][y + j]) return false; 
    }

    return true;
} 

bool place_queens(vvi &board, int x, int y){
    if(y >= n) return true;

    cout << "In col: "<< y << endl;
    for(int i = 0; i < n; ++i){
        cout << "Entering is safe with " << i << " " << y << endl;
        if(isSafe(board, i, y)){
            cout << "In row: "<< i << endl;
            board[i][y] = 1;
            if(place_queens(board, 0, y + 1)) return true;
            else board[i][y] = 0;
        }
    }

    return false;
}


int main(){
    cin >> n;
    vvi board(n, vector<int>(n, 0));
    place_queens(board, 0, 0);

    for(auto &rows: board){
        for(auto &cols: rows){
            cout << cols << " ";
        }
        cout << endl;
    }
}