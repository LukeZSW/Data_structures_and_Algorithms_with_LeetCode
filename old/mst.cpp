//MST Prim, lazy version
#include<queue>
#include<vector>
#include<unordered_map>
#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

class Connection {
public:
	string first;
	string second;
	int cost;
	Connection(string s1, string s2, int c) {
		first = s1;
		second = s2;
		cost = c;
	}
};

struct comp {
	bool operator()(const pair<int, pair<int, int>> &v1, const pair<int, pair<int, int>> &v2) {
		return v1.first < v2.first;
	}
};

vector<Connection> PrimBST(vector<Connection> connection) {
	unordered_map<string, int> m;
	unordered_map<int, string> m1;
	int count_string = 0;
	int n = connection.size();
	//unordered_map<pair<int, int>, int> edge;
	vector<vector<pair<int, pair<int, int>>>> adj;
	for (int i = 0; i < n; i++) {
		string sf = connection[i].first;
		string ss = connection[i].second;
		int nc = connection[i].cost;
		int nf, ns;
		if (m.find(sf) == m.end()) {
			m[sf] = count_string;
			m1[count_string] = sf;
			nf = count_string;
			count_string++;
			vector<pair<int, pair<int, int>>> v;
			adj.push_back(v);
		}
		else {
			nf = m[sf];
		}
		// if(ss == sf)
		//     continue;
		if (m.find(ss) == m.end()) {
			m[ss] = count_string;
			m1[count_string] = ss;
			ns = count_string;
			count_string++;
			vector<pair<int, pair<int, int>>> v;
			adj.push_back(v);
		}
		else {
			ns = m[ss];
		}
		if (nf > ns)
			swap(ns, nf);
		bool flag = true;
		for (auto j : adj[nf]) {
			if (j.second.first == nf && j.second.second == ns) {
				if (nc < j.first) {
					j.first = nc;
				}
				flag = false;
				break;
			}
		}
		if (flag)
			adj[nf].push_back(make_pair(nc, make_pair(nf, ns)));
	}
	vector<Connection> ans;
	vector<int> inT(count_string, 0);
	inT[0] = 1;
	priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, comp> pq;
	for (auto i : adj[0])
		pq.push(i);
	while (pq.size() > 0) {
		pair<int, pair<int, int>> p = pq.top();
		int nc = p.first;
		int nf = p.second.first;
		int ns = p.second.second;
		pq.pop();
		if (inT[ns] == 1)
			continue;
		else
			inT[ns] = 1;
		Connection c = Connection(m1[nf], m1[ns], nc);
		ans.push_back(c);
		for (auto i : adj[ns])
			pq.push(i);
	}
	if (find(inT.begin(), inT.end(), 0) != inT.end())
		ans.clear();
	return ans;
}

int main() {
	vector<Connection> connections;
	connections.push_back(Connection("A", "B", 6));
	connections.push_back(Connection("B", "C", 4));
	connections.push_back(Connection("C", "D", 5));
	connections.push_back(Connection("D", "E", 8));
	connections.push_back(Connection("E", "F", 2));
	connections.push_back(Connection("B", "F", 10));
	connections.push_back(Connection("E", "C", 9));
	connections.push_back(Connection("F", "C", 7));
	connections.push_back(Connection("B", "E", 3));
	connections.push_back(Connection("A", "F", 16));
	vector<Connection> ans = PrimBST(connections);
	for (Connection c : ans) {
		cout << c.first << " -> " << c.second << " " << c.cost << endl;
	}
	return 0;
}