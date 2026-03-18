#include <cmath>
#include <fstream>
#include <iostream>
#include <random>
#include <stack>
#include <vector>

struct Pos
{
    double x, y;
};

struct Graph
{
    int n;
    std::vector<Pos> points;
    std::vector<std::vector<int>> adjacencyList;
};

// Returns the squared distance between two points.
// This avoids the overhead of computing a square root, and is sufficient for comparing to r^2.
double dist2(Pos p1, Pos p2)
{
    double dx = p1.x - p2.x, dy = p1.y - p2.y;
    return dx * dx + dy * dy;
}
std::uniform_real_distribution<double> realDistributor;
std::uniform_int_distribution<> intDistributor;
std::default_random_engine re;

// Constructs a random geometric graph with n vertices and radius r.
Graph ConstructRGG(int n, double r)
{
    Graph g = { n, std::vector<Pos>(n), std::vector<std::vector<int>>(n) };
    // std::vector<Pos> points(n);
    for (int i = 0; i < n; i++) g.points[i] = { realDistributor(re), realDistributor(re) };
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (dist2(g.points[i], g.points[j]) <= r * r) g.adjacencyList[i].push_back(j);
    return g;
}

// Returns true if the graph is connected, false otherwise.
bool IsConnected(const Graph& graph)
{
    std::vector<bool> visited(graph.n, false);
    std::stack<int> next;
    next.push(0);
    int seen = 0;
    while (!next.empty())
    {
        int top = next.top();
        next.pop();
        if (visited[top]) continue;
        visited[top] = true;
        seen++;
        for (int a : graph.adjacencyList[top]) next.push(a);
    }
    return seen == graph.n;
}

int main()
{
    std::vector<std::pair<double, double>> results;
    int numTests   = 1000;
    intDistributor = std::uniform_int_distribution(100, 500);
    for (double r = 0; r < 3.005; r += 0.01)
    {
        std::cout << "Now running test " << r << std::endl;
        int numConnected = 0;
        for (int i = 0; i < numTests; i++)
        {
            int n   = intDistributor(re);
            Graph g = ConstructRGG(n, r / std::sqrt(n));
            if (IsConnected(g)) { numConnected++; }
        }
        results.push_back({ r, numConnected / ((double)numTests) });
    }
    // Write the results to a file for plotting with python.
    std::ofstream file("out.txt");
    for (auto [r, v] : results) { file << r << ' ' << v << '\n'; }
    file.close();
}
