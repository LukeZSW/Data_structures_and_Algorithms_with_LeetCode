#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

class WordListOrder
{
public:
	static int canArrangeWords(int n, vector<string> arr)
	{
		vector<vector<int>> directedGraph(26, vector<int>(26, 0));
		vector<int> inDegree(26);
		vector<int> outDegree(26);
		vector<bool> hasletter(26);
		bool haseuler = true;
		for (int i = 0; i < n; i++)
		{
			string word = arr[i];
			char firstletter = word[0];
			char lastletter = word[word.size() - 1];
			outDegree[lastletter - 'a']++;
			inDegree[firstletter - 'a']++;
			directedGraph[firstletter - 'a'][lastletter - 'a'] = 1;
			hasletter[lastletter - 'a'] = true;
			hasletter[firstletter - 'a'] = true;
		}
		int startNum = 0;
		int endNum = 0;
		for (int vertex = 0; vertex < 26; vertex++)
		{
			if(outDegree[vertex] - inDegree[vertex] == 1)
				startNum++;
			if (inDegree[vertex] - outDegree[vertex] == 1)
				endNum++;
			if (abs(inDegree[vertex] - outDegree[vertex]) > 1)
			{
				haseuler = false;
				break;
			}
		}
		if (startNum != 1 || endNum != 1)
			haseuler = false;
		if (!haseuler)
			return -1;
		else
		{
			int vertexnum = 0;
			for (int i = 0; i < 26; i++)
			{
				if (hasletter[i])
					vertexnum++;
			}
			int firstWordFirstLetter = arr[0][0] - 'a';
			haseuler = isConnected(firstWordFirstLetter, vertexnum, directedGraph);
			if (haseuler)
				return 1;
			else
				return -1;
		}
	}

	static bool isConnected(int start, int vertexnum, vector<vector<int>> &directedGraph)
	{
		for (int i = 0; i < 26; i++)     // 把有向图转换成无向图
		{
			for (int j = 0; j < 26; j++)
			{
				if (directedGraph[i][j] == 1)
				{
					directedGraph[j][i] = 1;
				}
			}
		}
		queue<int> q;
		vector<bool> visited(26);
		int passedvertexnum = 0;
		q.push(start);
		while (!q.empty())
		{
			int cur = q.front();
			q.pop();
			visited[cur] = true;
			passedvertexnum++;
			for (int v = 0; v < 26; v++)
			{
				if (directedGraph[cur][v] == 1 && visited[v] == false)
					q.push(v);
			}
		}
		if (passedvertexnum == vertexnum)
			return true;
		else
			return false;
	}
};

int main()
{
	vector<string> arr;
	//arr.push_back("abc");
	//arr.push_back("cde");
	//arr.push_back("cfg");
	//arr.push_back("ghc");
	arr.push_back("abc");
	arr.push_back("cdefg");
	arr.push_back("ghijkl");
	int n = arr.size();
	int f = WordListOrder::canArrangeWords(n, arr);
	cout << f;
}