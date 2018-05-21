// Edmond-Karp algorithm using adjacency matric
// Adapted from 1.2 Min-cost max-flow of Stanford ICPC Notebook
// https://www.topcoder.com/community/data-science/data-science-tutorials/minimum-cost-flow-part-two-algorithms/

// We want to Minimum Cost needed to achieve a flow of D

#include <cmath>
#include <vector>
#include <iostream>
#include <cstdio>
#include <limits>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long L;
typedef vector<L> VL;
typedef vector<VL> VVL;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const L INF = numeric_limits<L>::max() / 4;

struct MinCostMaxFlow {
    int N;     // number of nodes
    VVL cap, flow, cost;     // vector of vectors --> matrices storing capacity, flow, and cost
    VI found;     // vector --> used in Dijkstra to record if a node has been found
    VL dist, pi, width;     // vector --> pi for eliminating negative edges (like in Johnson's algorithm)
    // dist for Dijkstra's
    VPII dad;     // vector of tuples representing parent

    // Initializer list
    MinCostMaxFlow(int N) : N(N), cap(N, VL(N)), flow(N, VL(N)), cost(N, VL(N)), found(N), dist(N), pi(N), width(N), dad(N) {
    }


    // Basically, we follow shortest-cost augmenting paths, building up to the maximum flow (which is D, our supply/out-edge capacity of our added s),

    // We use ReduceCost to make all residual graph cost edges nonnegative
    /* This is a similar algorithm from the TopCoder link

       Successive Shortest Path w/ Potentials
       Transform network G by adding source and sink
       Initial flow is 0
       Use Bellman-Ford's algorithm to establish potentials pi (similar as initial step of Johnson's for All-Points Shortest-Paths)
       ReduceCost()
       While (G_f contains path s->t):
        Find any shortest path P s->t
        ReduceCost()
        Augment current flow along P
        Update G_f

       ReduceCost
       For each (i, j) in E:
        cost[i][j] = cost[i][j] + pi[i] - pi[j]
        cost[j][i] = 0
     */

    void AddEdge(int from, int to, L cap, L cost) {
        this->cap[from][to] = cap;
        this->cost[from][to] = cost;
    }

    /* s: edge source, k: curr, cap/cost: of s->k edge, dir: to/from */
    void Relax(int s, int k, L cap, L cost, int dir) {
        // Saves cost, parent, curr-flow at node k
        L val = dist[s] + pi[s] - pi[k] + cost;
        if (cap && val < dist[k]) {
            dist[k] = val;
            dad[k] = make_pair(s, dir);
            width[k] = min(cap, width[s]);
        }
    }

    L Dijkstra(int s, int t) {
        // finds shortest path and amount of flow delivered
        fill(found.begin(), found.end(), false);
        fill(dist.begin(), dist.end(), INF);
        fill(width.begin(), width.end(), 0);
        dist[s] = 0;
        width[s] = INF;
        while (s != -1) {
            int best = -1;
            found[s] = true;
            for (int k = 0; k < N; k++) {
                if (found[k]) continue;
                Relax(s, k, cap[s][k] - flow[s][k], cost[s][k], 1);
                Relax(s, k, flow[k][s], -cost[k][s], -1);
                if (best == -1 || dist[k] < dist[best]) best = k;
            }
            s = best;
        }
        for (int k = 0; k < N; k++)
            pi[k] = min(pi[k] + dist[k], INF);
        return width[t];
    }

    pair<L, L> GetMaxFlow(int s, int t) {
        L totflow = 0, totcost = 0;
        while (L amt = Dijkstra(s, t)) {
            // After storing the shortest path info, we update the flow and total cost
            totflow += amt;
            for (int x = t; x != s; x = dad[x].first) {
                if (dad[x].second == 1) {
                    flow[dad[x].first][x] += amt;
                    totcost += amt * cost[dad[x].first][x];
                } else {
                    flow[x][dad[x].first] -= amt;
                    totcost -= amt * cost[x][dad[x].first];
                }
            }
        }
        return make_pair(totflow, totcost);
    }
};
// BEGIN CUT
// The following code solves UVA problem #10594: Data Flow
int main() {
    int N, M;
    while (scanf("%d%d", &N, &M) == 2) {
        VVL v(M, VL(3));
        for (int i = 0; i < M; i++)
            scanf("%Ld%Ld%Ld", &v[i][0], &v[i][1], &v[i][2]);
        L D, K;
        scanf("%Ld%Ld", &D, &K);
        MinCostMaxFlow mcmf(N+1);
        for (int i = 0; i < M; i++) {
            mcmf.AddEdge(int(v[i][0]), int(v[i][1]), K, v[i][2]);
            mcmf.AddEdge(int(v[i][1]), int(v[i][0]), K, v[i][2]);
        }
        mcmf.AddEdge(0, 1, D, 0);
        pair<L, L> res = mcmf.GetMaxFlow(0, N);
        if (res.first == D) {
            printf("%Ld\n", res.second);
        } else {
            printf("Impossible.\n");
        }
    }
    return 0;
}
// END CUT
