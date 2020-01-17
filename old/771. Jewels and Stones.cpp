class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int num = 0;
        for(int i = 0; i < S.size(); i++)
        {
            if(J.find(S[i]) < J.size())
            {
                num++;
            }
        }
        return num;
    }
};