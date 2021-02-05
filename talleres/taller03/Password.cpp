#include <bits/stdc++.h>
using namespace std;

vector<string> answers;

void permutations(int (&characters)[26], int depth, string word){
    if (depth == 0) {
        answers.push_back(word);
        return;
    }
    for (int i = 0; i < 26; i++) {
        if (characters[i] == 1) {
            characters[i] = 0;
            permutations(characters, depth -1, word + char('a' + i));
            characters[i] = 1;
        }
    }
}

int main(){
    string s, real = "abcd";
    cin >> s;
    int characters[26];
    int l = s.length();


    memset(characters, 0, sizeof(characters));
    for(auto &a: s) {
        cout << a << endl;
        characters[a - 'a'] = 1;
    }

    permutations(characters, l, "");

    
    for(auto &a: answers){
        cout << a << " ";
        if(a == real) cout << "found";
        cout << endl;
    }
    
}