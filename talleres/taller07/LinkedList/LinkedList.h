#ifndef CLIONTESTING_LINKEDLIST_H
#define CLIONTESTING_LINKEDLIST_H

struct Node{
    int  data;
    Node *next;
};

class LinkedList{
    Node *head = nullptr;
    Node *last = nullptr;

    public:
        void push(int val);
        void insert(int val, int pos);
        void append(int val);
        void printList();
        void deleteNode(int key);
        void deleteNodeAt(int pos);
        void deleteList();
        int length();
        bool find(int key);
        int get(int pos);
        Node *getNode(int pos);
        void set(int val, int pos);
        void reverse();
};

#include "LinkedList.cpp"

#endif
