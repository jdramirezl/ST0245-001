#include "LinkedList.h"
#include <iostream>
#include <bits/stdc++.h>
#include <cassert>
#define D(x) cout << #x << " = " << x << endl;
using namespace std;

struct Node;


void LinkedList::push(int val){ //Dos nodos Pointer-to-pointer, deme la referencia de la referencia de Head
    Node *new_node = new Node();
    new_node -> data = val;
    new_node -> next = head;
    head = new_node;
}

void LinkedList::insert(int val, int pos){
    Node *prev = head;

    for(int i = 0; prev != nullptr && i<pos-1; ++i){
        prev = prev -> next;
    }

    if (prev == nullptr){
        cout << "Accessing unexistent position" << endl;
        return;
    }

    Node *new_node = new Node();
    new_node -> data = val;
    new_node -> next = prev -> next;
    prev -> next = new_node;
}

void LinkedList::append(int val){
    Node *new_node = new Node(), *temp;
    new_node -> data = val;
    new_node -> next = nullptr;

    temp = head;

    if(head == nullptr){
        head = new_node;
        return;
    }

    while (temp->next != nullptr) temp = temp -> next;

    temp -> next = new_node;
}



void LinkedList::printList(){
    Node *node = head;
    while (node != nullptr){
        cout << " " << node -> data << endl;
        node = node->next;
    }
}

void LinkedList::deleteNode(int key){
    Node *temp = head, *prev;

    if(temp == nullptr){
        return;
    }

    if(temp -> data == key){
        head = temp -> next;
        free(temp);
        return;
    }

    while(temp -> next != nullptr && temp -> data != key){
        prev = temp;
        temp = temp -> next;
    }

    if (temp -> next == nullptr){
        cout << "Value not in LinkedList" << endl;
        return;
    }

    prev -> next = temp -> next;

    free(temp);
}

void LinkedList::deleteNodeAt(int pos){
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
        cout << "Position exceeds LinkedList" << endl;
        return;
    }

    Node *conect = prev -> next -> next;

    free(prev -> next);

    prev -> next = conect;
}

void LinkedList::deleteList(){
    Node *next = head, *now;

    if(head == nullptr) return;

    while(now -> next != nullptr){
        next = now -> next;
        free(now);
        now = next;
    }

    head = nullptr;
}

int LinkedList::length(){
    Node *now = head;
    int count = 0;

    if(head == nullptr) return 0;

    while(now  != nullptr){
        count++;
        now = now -> next;
    }

    return count;
}

bool LinkedList::find(int key){
    Node *now = head;

    if(head == nullptr) return false;

    while(now != nullptr){
        if (now -> data == key) return true;
        now = now -> next;
    }

    return false;
}

int LinkedList::get(int pos){
    Node *prev = head;

    for(int i = 0; prev != nullptr && i<pos; ++i){
        prev = prev -> next;
    }

    if(prev == nullptr) {
        cout << "non existent position" << endl;
        assert(0);
    }

    return prev -> data;
}

Node* LinkedList::getNode(int pos){
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

void LinkedList::reverse(){
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

void LinkedList::set(int val, int pos){
    Node *prev = head;

    for(int i = 0; prev != nullptr && i<pos-1; ++i){
        prev = prev -> next;
    }

    if (prev == nullptr || prev -> next == nullptr){
        cout << "null node" << endl;
        return;
    }

    prev -> next -> data = val;
}
