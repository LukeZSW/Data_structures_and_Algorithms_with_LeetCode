class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int len = prices.size();
        int minprice = INT_MAX;
        int answer = 0;
        for(int i = 0; i < len; i++)
        {
            if(prices[i] < minprice)
                minprice = prices[i];
            else if(prices[i] - minprice > answer)
                answer = prices[i] - minprice;
        }
        return answer;
    }
};