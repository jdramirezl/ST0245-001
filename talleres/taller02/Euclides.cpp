#include <cmath>
#include <iostream>
using namespace std;

int Euclides(int x, int y){
    int mayor = max(x, y), menor = min(x, y);
    if (mayor == 0) return menor;
    if (menor == 0) return mayor;
    if(mayor%menor == 0) return menor;
    int residue = mayor % menor;
    return Euclides(menor, residue);
}

int main(){
    cout << Euclides(1728 , 842) << endl; 
}