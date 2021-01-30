#include <bits/stdc++.h>
using namespace std;

#define vvi vector<vector<int>>

for(int i=0; i< menor.length(); i++){
        for(int j=0; j<mayor.length(); j++){
            if(mayor[j] == menor[i]){
                matriz[i][j] = 1;
                break;
            }
        }
    }

int lcs(string a, string b, int row, int col, vvi & matriz, int length, int min_col){
    if(col >= matriz[0].length() && row >= matriz[0].length()) return length;
    if(a[col] == b[row]){ 
        matriz[row][col] = 1;
        if(col == matriz[0].length()-1) return length;
        lcs(string a, string b, int row+1, int col+1, vvi & matriz, length + 1){
    }
    lcs(string a, string b, int row+1, int col+1, vvi & matriz, length + 1){
}

int main(){
    string a, b, mayor = b, menor = a;
    if(a.length() > b.length()){
        mayor = a;
        menor = b;
    }

    vvi matriz (mayor.length(), vector<int> (menor.length(), 0)));
    
    cout << lcs(mayor, menor, 0, 0, matriz, 0) << endl;
}