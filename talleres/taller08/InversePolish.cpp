#include <bits/stdc++.h>
using namespace std;

int rp(string op, stack<int> nums){
    int j = 0, first, second;
    for (int i = 0; i < op.length(); ++i) {
        while (isdigit(op[j])){
            j++;
        }
        if (j > i){
            nums.push(stoi(op.substr(i, j+1)));
            i = j;
            continue;
        }

        if(op[i] == ' ') continue;
        second = nums.top();
        nums.pop();
        first = nums.top();
        nums.pop();
        if (op[i] == '*'){
            nums.push(first*second);
            continue;
        } else if (op[i] == '/') {
            nums.push(first/second);
            continue;
        } else if (op[i] == '+') {
            nums.push(first+second);
            continue;
        } else if (op[i] == '-'){
            nums.push(first-second);
            continue;
        }

    }

    if(!nums.empty()) return nums.top();
    return -1;
}

int main(){
    
}
