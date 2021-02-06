#ifndef CLIONTESTING_BEELIST_H
#define CLIONTESTING_BEELIST_H
struct Bee{
    int x;
    int y;

    Bee(int x, int y){
        this -> x = x;
        this -> y = y;
    }

    void setX(int x){
        this -> x = x;
    }

    void setY(int y){
        this -> y = y;
    }
};

struct Node{
    Bee *bee;
    Node *next;
};


class BeeList{
    Node *head = nullptr;
    Node *last = nullptr;

    public:
        void push_front(Bee val);
        void insert(Bee val, int pos);
        void push_back(Bee val);
        void printList();
        void deleteNode(Bee key);
        void deleteNodeAt(int pos);
        void deleteList();
        int length();
        Bee *find(Bee key);
        Bee *get(int pos);
        Node *getNode(int pos);
        void set(Bee val, int pos);
        void reverse();
};

#include "BeeList.cpp"

#endif
