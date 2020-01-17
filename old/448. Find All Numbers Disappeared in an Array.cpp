class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> answer;
        for(int i = 0; i < nums.size(); i++) 
        {
            int temp = abs(nums[i]) - 1;
            if(nums[temp] > 0)
            {
                nums[temp] *= -1;
            }
        }
        for(int i = 0; i < nums.size(); i++) 
        {
            if(nums[i] > 0) 
                answer.push_back(i+1);
        }
        return answer;
    }
};