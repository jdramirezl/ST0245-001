#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val;
    Node *next;
    Node() : val(0), next(nullptr) {}
    Node(int x) : val(x), next(nullptr) {}
    Node(int x, Node *next) : val(x), next(next) {}
};

int maxElement(Node *head, int top){
    if(!head) return top;
    return maxElement(head -> next, max(top, head ->val));
}

int main(){

    Node last(5), four(4, &last), three(3, &four), two(2, &three), head(1, &two);
    cout << maxElement(&head, 0);
}