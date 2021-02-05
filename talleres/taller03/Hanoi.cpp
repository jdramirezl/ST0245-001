#include <bits/stdc++.h>
using namespace std;

#define vvi vector<vector<int>>
#define vsi vector<stack<int>>
#define D(x) cout << #x << " = " << x << endl;

// TODO
void towerOfHanoi(int n, char from_rod, char to_rod, char aux_rod) { 
    D(from_rod) 
    D(to_rod)  
    D(aux_rod)
    cout << endl;
    
    if (n == 1) { 
        cout << "Move disk 1 from rod " << from_rod << " to rod " << to_rod<<endl; 
        return; 
    } 
    towerOfHanoi(n - 1, from_rod, aux_rod, to_rod); 
    cout << "Move disk " << n << " from rod " << from_rod << " to rod " << to_rod << endl; 
    towerOfHanoi(n - 1, aux_rod, to_rod, from_rod); 
} 
int main(){
    int n_of_disks;
    cin >> n_of_disks;
    
    towerOfHanoi(n_of_disks, '1', '3', '2'); // A, B and C are names of rods 
    
    
}