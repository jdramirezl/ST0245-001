#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val;
    Node *next;
    Node() : val(0), next(nullptr) {}
    Node(int x) : val(x), next(nullptr) {}
    Node(int x, Node *next) : val(x), next(next) {}
};

bool compare(Node *first, Node *second){
    if(!first && !second) return true;
    if (!first && second || first && !second || first->val != second->val) return false;
    return compare(first -> next, second -> next);
}

int main(){

    Node last(5), four(4, &last), three(3, &four), two(2, &three), head(1, &two);
    Node last2(5), four2(4, &last2), three2(69, &four2), two2(2, &three2), head2(1, &two2);
    cout << compare(&head, &head2);
}