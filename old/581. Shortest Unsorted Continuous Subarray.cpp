//O(nlgn) version, use sort
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int len = nums.size();
        if(len == 0 || len == 1)
        {
            return 0;
        }
        vector<int> sortnums = nums;
        sort(sortnums.begin(), sortnums.end());
        int i, j;
        for(i = 0; i < len; i++)
        {
            if(sortnums[i]!=nums[i])
                break;
        }
        if(i == len)
            return 0;
        for(j = len-1; j >= 0; j--)
        {
            if(sortnums[j]!=nums[j])
                break;
        }
        return j - i + 1;
    }
};

//O(n) version
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int nmin = INT_MAX;
        int nmax = INT_MIN;
        bool flag = false;
        int len = nums.size();
        for(int i = 1; i < len; i++)
        {
            if(nums[i] < nums[i-1])
                flag = true;
            if(flag)
                nmin = min(nmin, nums[i]);
        }
        flag = false;        
        for(int i = len-2; i >= 0; i--)
        {
            if(nums[i+1] < nums[i])
                flag = true;
            if(flag)
                nmax = max(nmax, nums[i]);
        }
        int l, r;
        for(l = 0;l < len; l++)
        {
            if(nmin < nums[l])
                break;
        }
        for(r = len-1; r >= 0; r--)
        {
            if(nmax > nums[r])
                break;
        }
        return r - l < 0 ? 0 : r - l + 1;
    }
};