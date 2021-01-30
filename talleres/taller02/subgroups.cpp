#include <bits/stdc++.h>
using namespace std;

struct comparator{
    bool operator()(vector<int> v1, vector<int> v2){
        if(v1.size() == v2.size()){
            int v1s = 0, v2s = 0;
            for (int i = 0; i < v1.size(); ++i){
                v1s += v1[i];
                v2s += v2[i];
            }
            return v1s > v2s;
        }
        return v1.size() > v2.size();
    }
};

priority_queue<vector<int>, vector<vector<int>>, comparator> pq;

void print(vector<int> &x){
    cout << "[ ";
    for (int i = 0; i < x.size(); ++i){
        cout << x[i] << " ";
    }
    cout << " ]" << endl;
}

void subsets(vector<int> &stack, vector<int> &set, int index){
    for (int i = index ; i < set.size(); ++i){
        stack.push_back(set[i]);
        pq.push(stack);
        subsets(stack, set, i + 1);
        stack.pop_back();
    }
}


int main(){
    vector<int> stack;
    vector<int> set {1,2,3,4,5};
    subsets(stack, set, 0);

    cout << pq.size() << endl;
    while (!pq.empty()) {
        vector<int> temp = pq.top();
        print(temp);
        pq.pop();
    }
    cout << '\n';
}