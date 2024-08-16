# https://quera.org/problemset/6404


#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Reaction {
public:
    vector<int> pre_materials;
    vector<int> response_materials;

    Reaction(const vector<int>& pre, const vector<int>& response) {
        pre_materials = pre;
        response_materials = response;
    }
};

int main() {
    int n, m, k;
    cin >> n >> m >> k;

    unordered_set<int> owned_materials;
    for (int i = 0; i < m; ++i) {
        int material;
        cin >> material;
        owned_materials.insert(material);
    }

    vector<Reaction> reactions;
    reactions.reserve(k); // Preallocate space to avoid multiple reallocations

    for (int i = 0; i < k; ++i) {
        int pre_n, response_n;
        cin >> pre_n >> response_n;

        vector<int> pre_materials(pre_n);
        for (int j = 0; j < pre_n; ++j) {
            cin >> pre_materials[j];
        }

        vector<int> response_materials(response_n);
        for (int j = 0; j < response_n; ++j) {
            cin >> response_materials[j];
        }

        reactions.emplace_back(pre_materials, response_materials);
    }

    bool progress = true;
    while (progress) {
        progress = false;
        for (size_t i = 0; i < reactions.size(); ++i) {
            bool can_react = true;
            for (int pre_mat : reactions[i].pre_materials) {
                if (owned_materials.find(pre_mat) == owned_materials.end()) {
                    can_react = false;
                    break;
                }
            }

            if (can_react) {
                owned_materials.insert(reactions[i].response_materials.begin(), reactions[i].response_materials.end());
                reactions.erase(reactions.begin() + i);
                progress = true;
                break;
            }
        }
    }

    // Print results
    cout << owned_materials.size() << endl;
    vector<int> sorted_owned_materials(owned_materials.begin(), owned_materials.end());
    sort(sorted_owned_materials.begin(), sorted_owned_materials.end());

    for (int material : sorted_owned_materials) {
        cout << material << " ";
    }
    cout << endl;

    return 0;
}
