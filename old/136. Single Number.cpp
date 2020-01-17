class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int len = nums.size();
        int answer = 0;
        for(int i = 0; i < len; i++)
        {
            answer = answer ^ nums[i];
        }
        return answer;
    }
};

//hash table; time:O(n); space:O(n)
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_set<int> nn;
        int len = nums.size();
        for(int i = 0; i < len; i++)
        {
            if(nn.find(nums[i]) == nn.end())
            {
                nn.insert(nums[i]);
            }
            else
            {
                nn.erase(nums[i]);
            }
        }
        return *nn.begin();
    }
};