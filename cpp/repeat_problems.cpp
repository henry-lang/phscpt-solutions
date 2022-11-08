#include <unordered_map>
#include <iostream>
#include <cstddef>

using namespace std;

int main() {
    unordered_map<size_t, bool> probs;

    int n;
    cin >> n;
    for(size_t i = 0; i < n; i++) {
        size_t prob;
        cin >> prob;
        probs.insert(prob, true);
    }

    cout << probs.size() << endl;
}