class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        int len = nums.size();
        for(int i = 0; i < len; i++) {
            if(m.find(nums[i]) == m.end()) {
                m[nums[i]] = 1;
            }
            else{
                m[nums[i]] += 1;   
            }
        }
        vector<pair<int, int>> p;
        for(auto& a: m) {
            pair<int, int> temp(a.second, a.first);
            p.push_back(temp);
        }
        sort(p.begin(), p.end());
        vector<int> ans;
        for(int i= p.size() - 1; i >= 0; i--) {
            ans.push_back(p[i].second);
            k--;
            if(k==0)
                break;
        }
        return ans;
    }
};
