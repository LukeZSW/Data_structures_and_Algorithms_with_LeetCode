//set method ; using O(n) space
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        int ans;
        for(int i = 0; i < nums.size(); i++) {
            if(s.find(nums[i]) == s.end())
                s.insert(nums[i]);
            else {
                ans = nums[i];
                break;
            }
        }
        return ans;
    }
};

//cycle detction O(1) space
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int tortoise = nums[0];
        int hare = nums[0];
        do {
            tortoise = nums[tortoise];
            hare = nums[nums[hare]];
        } while(tortoise != hare);
        
        int ptr1 = nums[0];
        int ptr2 = tortoise;
        while(ptr1 != ptr2) {
            ptr1 = nums[ptr1];
            ptr2 = nums[ptr2];
        }
        return ptr1;
    }
};