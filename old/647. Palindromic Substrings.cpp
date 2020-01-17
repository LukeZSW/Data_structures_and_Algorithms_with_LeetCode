class Solution {
public:
    int countSubstrings(string s) {
        int len = s.size();
        int ans = 0;
        int j, k;
        for(int i = 0; i < len; i++) {
            j = i;
            k = i;
            while(j >= 0 && k < len) {
                if(s[j] != s[k])
                    break;
                ans++;
                j--;
                k++;
            }
            j = i;
            k = i+1;
            while(j >= 0 && k < len) {
                if(s[j] != s[k])
                    break;
                ans++;
                j--;
                k++;
            }
        }
        return ans;
    }
};