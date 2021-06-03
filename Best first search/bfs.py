#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pi;
vector<vector<pi> > graph;
// Function for adding edges to graph
void addedge(int x, int y, int cost)
{
graph[x].push_back(make_pair(cost, y));
graph[y].push_back(make_pair(cost, x));
}
// Function For Implementing Best First Search
// Gives output path having lowest cost
void best_first_search(int source, int target, int n)
{
vector<bool> visited(n, false);
// MIN HEAP priority queue
priority_queue<pi, vector<pi>, greater<pi> > pq;
// sorting in pq gets done by first value of pair

pq.push(make_pair(0, source));
visited[0] = true;
while (!pq.empty()) {
int x = pq.top().second;
// Displaying the path having lowest cost
cout << x <<"->"<< " ";
pq.pop();
if (x == target)
break;
for (int i = 0; i < graph[x].size(); i++) {
if (!visited[graph[x][i].second]) {
visited[graph[x][i].second] = true;
pq.push(graph[x][i]);
}
}
}
}
int main()
{
// No. of Nodes
int v = 13;
graph.resize(v);
// The nodes shown in above example(by alphabets) are
// implemented using integers addedge(x,y,cost);
addedge(0, 1, 7);
addedge(0, 2, 2);
addedge(0, 3, 3);
addedge(1, 2, 3);
addedge(1, 4, 4);
addedge(2, 4, 4);
addedge(2, 8, 1);
addedge(4, 6, 5);
addedge(8, 6, 3);
addedge(8, 7, 2);
addedge(7, 5, 2);
addedge(3, 12, 2);
addedge(12, 9, 4);
addedge(12, 10, 4);
addedge(9, 11, 4);
addedge(10, 11, 4);
addedge(11, 5, 5);
int source = 0;
int target = 5;
// Function call
best_first_search(source, target, v);
return 0;
}
