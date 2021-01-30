#include <bits/stdc++.h>
using namespace std;

bool inventory_sums_to_target(vector<int> &weights, vector<bool> &visited, int target_sum, int index, int sum){
    sum += weights[index];
    if(sum > target_sum) return false;
    if(sum == target_sum) return true;
    for (int i = 0; i < weights.size(); i++){
        if (!visited[i]) {
            visited[i] = true;
            if (inventory_sums_to_target(weights, visited, target_sum, i, sum)){
                return true;
            }
            visited[i] = false;
        }
    }

    return false;
}


int main(){
    vector<int> weights {1,2,3,4,5,6,7,8,9,10,11};
    vector<bool> visited(weights.size(), false);
    cout << inventory_sums_to_target(weights, visited, 69, 0, 0);
}