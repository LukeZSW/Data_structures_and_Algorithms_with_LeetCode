class Solution {
public:
    vector<vector<int> > permute(vector<int> &num) {
	    vector<vector<int>> ans;
        backtrack(num, 0, ans);
	    return ans;
    }
    
    
	void backtrack(vector<int> &num, int first, vector<vector<int> > &ans)	{
		int n = num.size();
        if (first == n) {
		    ans.push_back(num);
		}
		for (int i = first; i < n; i++) {
		    swap(num[first], num[i]);
		    backtrack(num, first + 1, ans);
		    swap(num[first], num[i]);
		}
    }
};