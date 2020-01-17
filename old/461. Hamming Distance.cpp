class Solution {
public:
    int hammingDistance(int x, int y) {
        int num = 0;
        int c = x ^ y;
        cout<<c;
        while(c > 0)
        {
            num += c % 2;
            c = c / 2;
        }
        return num;
    }
    //fast vesion
    /*
    int hammingDistance(int x, int y) {
        return bitset<32>(x^y).count();
    }
    */
};