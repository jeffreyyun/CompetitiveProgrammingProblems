#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using std::string;
using std::vector;
using std::cin;

struct Query {
    string type, s;
    size_t ind;
};

class QueryProcessor {
    int bucket_count;
    vector<vector<string> > hash_row;
    size_t hash_func(const string& s) const {
        static const size_t multiplier = 263;
        static const size_t prime = 1000000007;
        unsigned long long hash = 0;
        for (int i = static_cast<int> (s.size()) - 1; i >= 0; --i)
            hash = (hash * multiplier + s[i]) % prime;
        return hash % bucket_count;
    }

public:
    explicit QueryProcessor(int bucket_count): bucket_count(bucket_count), hash_row(bucket_count) {}

    Query readQuery() const {
        Query query;
        cin >> query.type;
        if (query.type != "check")
            cin >> query.s;
        else
            cin >> query.ind;
        return query;
    }

    void writeSearchResult(bool was_found) const {
        std::cout << (was_found ? "yes\n" : "no\n");
    }

    void processQuery(const Query& query) {
        if (query.type == "check") {
            int key = query.ind;
            // "beginning" of chain is end of array
            for (int i = hash_row[key].size()-1; i >= 0; --i)
                std::cout << hash_row[key][i] << " ";
            std::cout << "\n";
        } else {
            int key = hash_func(query.s);
            vector<string>::iterator it = std::find(hash_row[key].begin(), hash_row[key].end(), query.s);
            if (query.type == "find")
                writeSearchResult(it != hash_row[key].end());
            else if (query.type == "add") {
                if (it == hash_row[key].end())
                    hash_row[key].push_back(query.s);
            } else if (query.type == "del") {
                if (it != hash_row[key].end())
                    hash_row[key].erase(it);
            }
        }
    }

    void processQueries() {
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i)
            processQuery(readQuery());
    }
};

int main() {
    //string fdir = "~/hackerrank-problems/coursera/Data Structures - Assignment 3 - Hashing/hash_chains/tests";
    //freopen((fdir + "/06").c_str(), "r", stdin);

    std::ios_base::sync_with_stdio(false);
    int bucket_count;
    cin >> bucket_count;
    QueryProcessor proc(bucket_count);
    proc.processQueries();
    return 0;
}
