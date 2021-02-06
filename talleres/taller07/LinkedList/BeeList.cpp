#include "BeeList.hpp"
#include <iostream>
#include <bits/stdc++.h>
#include <cassert>
#define D(x) cout << #x << " = " << x << endl;
using namespace std;

struct Bee;
struct Node;


void BeeList::push_front(Bee given_bee){ //Dos nodos Pointer-to-pointer, deme la referencia de la referencia de Head
    Node *new_node = new Node();
    new_node -> bee = &given_bee;
    new_node -> next = head;
    head = new_node;
}

void BeeList::insert(Bee val, int pos){
    Node *prev = head;

    for(int i = 0; prev != nullptr && i<pos-1; ++i){
        prev = prev -> next;
    }

    if (prev == nullptr){
        cout << "Accessing unexistent position" << endl;
        return;
    }

    Node *new_node = new Node();
    new_node -> bee = &val;
    new_node -> next = prev -> next;
    prev -> next = new_node;
}

void BeeList::push_back(Bee val){
    Node *new_node = new Node(), *temp;
    new_node -> bee = &val;
    new_node -> next = nullptr;

    temp = head;

    if(head == nullptr){
        head = new_node;
        return;
    }

    while (temp->next != nullptr) temp = temp -> next;

    temp -> next = new_node;
}



void BeeList::printList(){
    Node *node = head;
    while (node != nullptr){
        cout << "Bee coordinates: (" << node -> bee -> x << ", " << node -> bee -> y << ")" << endl;
        node = node->next;
    }
}

void BeeList::deleteNode(Bee key){
    Node *temp = head, *prev;

    if(temp == nullptr){
        return;
    }

    if(temp -> bee == &key){
        head = temp -> next;
        free(temp);
        return;
    }

    while(temp -> next != nullptr && temp -> bee != &key){
        prev = temp;
        temp = temp -> next;
    }

    if (temp -> next == nullptr){
        cout << "Value not in BeeList" << endl;
        return;
    }

    prev -> next = temp -> next;

    free(temp);
}

void BeeList::deleteNodeAt(int pos){
    Node *temp = head, *prev;

    if(temp == nullptr){
        return;
    }

    if(pos == 0){
        head = temp -> next;
        free(temp);
        return;
    }

    prev = temp;

    for(int i = 0; prev != nullptr && i<pos-1; ++i){
        prev = prev -> next;
    }

    if (prev == nullptr || prev -> next == nullptr) {
        cout << "Position exceeds BeeList" << endl;
        return;
    }

    Node *conect = prev -> next -> next;

    free(prev -> next);

    prev -> next = conect;
}

void BeeList::deleteList(){
    Node *next = head, *now;

    if(head == nullptr) return;

    while(now -> next != nullptr){
        next = now -> next;
        free(now);
        now = next;
    }

    head = nullptr;
}

int BeeList::length(){
    Node *now = head;
    int count = 0;

    if(head == nullptr) return 0;

    while(now  != nullptr){
        count++;
        now = now -> next;
    }

    return count;
}

Bee *BeeList::find(Bee key){
    Node *now = head;

    if(head == nullptr) {
        cout << "Bee not found" << endl;
        return nullptr;
    }

    while(now != nullptr){
        if (now -> bee == &key) {
            return now -> bee;
        }
        now = now -> next;
    }

    cout << "Bee not found" << endl;
    return nullptr;
}

Bee* BeeList::get(int pos){
    Node *prev = head;

    for(int i = 0; prev != nullptr && i<pos; ++i){
        prev = prev -> next;
    }

    if(prev == nullptr) {
        cout << "non existent position" << endl;
        assert(0);
    }

    return prev -> bee;
}

Node* BeeList::getNode(int pos){
    Node *prev = head;

    for(int i = 0; prev != nullptr && i<pos-1; ++i){
        prev = prev -> next;
    }

    if(prev == nullptr) {
        cout << "non existent position" << endl;
        assert(0);
    }

    return prev;
}

void BeeList::reverse(){
    if (head == nullptr) return ;

    Node *node = head, *anterior = nullptr, *next;

    while(node != nullptr){
        next = node -> next;
        node -> next = anterior;
        anterior = node;
        node = next;
    }

    head = anterior;
}

void BeeList::set(Bee val, int pos){
    Node *prev = head;

    for(int i = 0; prev != nullptr && i<pos-1; ++i){
        prev = prev -> next;
    }

    if (prev == nullptr || prev -> next == nullptr){
        cout << "null node" << endl;
        return;
    }

    prev -> next -> bee = &val;
}
