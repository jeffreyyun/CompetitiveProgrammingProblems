#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using std::string;
using std::vector;
using std::cin;
using std::unordered_map;

struct Query {
    string type, name;
    int number;
};

vector<Query> read_queries() {
    int n;
    cin >> n;
    vector<Query> queries(n);
    for (int i = 0; i < n; ++i) {
        cin >> queries[i].type;
        if (queries[i].type == "add")
            cin >> queries[i].number >> queries[i].name;
        else
            cin >> queries[i].number;
    }
    return queries;
}

void write_responses(const vector<string>& result) {
    for (size_t i = 0; i < result.size(); ++i)
        std::cout << result[i] << "\n";
}

int hash(long long number, int p)
{
    int a = 5557;
    int b = 9193;
    long long v = (a*number % p + b) % p;
    return v;
}

vector<string> process_queries(const vector<Query>& queries) {
    vector<string> result;
    int p = 100037;
    // Keep list of all existing (i.e. not deleted yet) contacts.
    vector<string> contacts(p, "");  // number to name
    int key;

    for (size_t i = 0; i < queries.size(); ++i)
    {
        key = hash(queries[i].number, p);
        if (queries[i].type == "add") {
            bool was_founded = false;
            // if we already have contact with such number,
            // we should rewrite contact's name
            if (contacts[key] != "")
            {
                contacts[key] = queries[i].name;
                was_founded = true;
            }
            // otherwise, just add it
            if (!was_founded)
                contacts[key] = queries[i].name;
        } else if (queries[i].type == "del") {
            contacts[key] = "";
        }
        string response = "not found";
        if (contacts[key] != "")
            response = contacts[key];
        result.push_back(response);

        return result;
    }
}

int main() {
    write_responses(process_queries(read_queries()));
    return 0;
}
