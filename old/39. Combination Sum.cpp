class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> oneans;
        sort(candidates.begin(), candidates.end());
        help(ans, oneans, candidates, target, 0);
        return ans;
    }
    void help(vector<vector<int>> &ans, vector<int> oneans, 
              vector<int> candidates, int target, int start) {
        if(target == 0) {
            ans.push_back(oneans);
            return;            
        }
        int len = candidates.size();
        for(int i = start; i < len && candidates[i] <= target; i++) {
            vector<int> temp = oneans;
            temp.push_back(candidates[i]);
            help(ans, temp, candidates, target - candidates[i], i);
        }
    }
};