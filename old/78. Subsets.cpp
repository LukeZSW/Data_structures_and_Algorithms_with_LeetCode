class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> beginset;
        help(nums, ans, beginset, 0);
        return ans;
    }
    void help(vector<int>& nums, vector<vector<int>> &ans, vector<int> subset, int pos) {
        //termination
        if(pos == nums.size()) {
            ans.push_back(subset);
            return;
        }
        help(nums, ans, subset, pos+1);
        subset.push_back(nums[pos]);
        help(nums, ans, subset, pos+1);
    }
};