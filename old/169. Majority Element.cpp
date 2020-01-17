//hash map
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        if(nums.size()==1)
            return nums[0];
        unordered_map<int, int> m;
        int answer = 0;
        for(int i = 0; i < nums.size(); i++)
        {
            if(m.find(nums[i])==m.end())
            {
                m[nums[i]] = 1;
            }
            else
            {
                m[nums[i]] += 1;
                if(m[nums[i]] > nums.size()/2)
                {
                    answer = nums[i];
                    break;
                }
            } 
        }
        return answer;
    }
};

//sort
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        return nums[nums.size()/2];
    }
};