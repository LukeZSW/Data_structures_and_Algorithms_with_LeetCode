class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len = nums.size();
        int pro = 1;
        vector<int> nzero;
        for(int i = 0; i < len; i++) {
            if(nums[i] != 0)
                pro *= nums[i];
            else
                nzero.push_back(i);
        }
        if(nzero.size() == 0) {
            for(int i = 0; i < len; i++) {
                nums[i] = pro / nums[i];
            }
        } 
        else if(nzero.size() == 1) {
            for(int i = 0; i < len; i++) {
                if(i != nzero[0])
                    nums[i] = 0;
                else
                    nums[i] = pro;
            }        
        }
        else {
            for(int i = 0; i < len; i++) {
                nums[i] = 0;
            }                
        }
        return nums;
    }
};

//no extra space, two loop count left product and right product;
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len = nums.size();
        vector<int> ans(len, 1);
        for(int i = 1; i < len; i++) {
            ans[i] = ans[i-1] * nums[i-1];
        }
        int right = 1;
        for(int i = len - 1; i >= 0; i--) {
            ans[i] *= right;
            right *= nums[i];
        }
        return ans;
    }
};