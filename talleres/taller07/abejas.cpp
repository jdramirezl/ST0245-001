#include "LinkedList/BeeList.hpp"
using namespace std;

int main(){
    BeeList abejas;

    vector<Bee> bees{Bee(0,1), Bee(5,13),Bee(3,23),Bee(-2,40),Bee(7,8),Bee(12,4)};

    for (int i = 0; i < bees.size(); ++i) {
        abejas.push_back(bees[i]);
    }

    abejas.printList();
    abejas.insert(Bee(69,420), 3);
    abejas.printList();
}