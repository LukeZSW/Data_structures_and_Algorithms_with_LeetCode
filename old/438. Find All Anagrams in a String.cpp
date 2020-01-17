class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int lens = s.size();
        int lenp = p.size();
        vector<int> ans;
        if (lens < lenp)
            return ans;
        vector<int> pp(26,0);
        for(int i = 0; i < lenp; i++)
            pp[p[i]-'a']++;
        vector<int> ss(26,0);
        for(int i = 0; i < lenp; i++)
            ss[s[i]-'a']++;
        if(ss == pp)
            ans.push_back(0);
        for (int i = 1; i < lens - lenp + 1; i++)
        {
            ss[s[i-1]-'a']--;
            ss[s[i-1+lenp]-'a']++;
            if(ss == pp)
                ans.push_back(i);
        }
        return ans;    
    }
};