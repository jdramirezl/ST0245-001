#include <bits/stdc++.h>
using namespace std;

#define vvi vector<vector<int>>

int lcs( string X, string Y, int m, int n )  {  
    if (m == 0 || n == 0) return 0;  
    if (X[m-1] == Y[n-1]) return 1 + lcs(X, Y, m-1, n-1);  
    else return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));  
}  

int main(){
    string a, b;

    cin >> a >> b;
    string mayor = b, menor = a;
    if(a.length() > b.length()){
        mayor = a;
        menor = b;
    }
    
    cout << lcs(mayor, menor, mayor.length(), menor.length()) << endl;
}