#include <bits/stdc++.h>
using namespace std;
#define vvi vector<vector<int>>



void print(vvi &square){
    for(const auto &row: square){
        for(const auto &col: row){
            cout << setw(5) << col;
        }
        cout << "\n";
    }
    cout << "\n";
}
int main(){
    vvi a = {{1,2},{3,4}};
    print(a);
}