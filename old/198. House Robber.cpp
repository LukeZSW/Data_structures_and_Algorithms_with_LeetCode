class Solution {
public:
    int rob(vector<int>& nums) {
        int len = nums.size();
        if(len == 0)
            return 0;
        if(len == 1)
            return nums[0];
        if(len == 2)
            return max(nums[0], nums[1]);
        vector<int> answer(len, 0);
        answer[0] = nums[0];
        answer[1] = max(nums[0], nums[1]);
        for(int i = 2; i < len; i++)
            answer[i] = max(answer[i-2] + nums[i], answer[i-1]);
        return answer[len-1];
    }
};