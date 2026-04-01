class Solution {
    public int maxProfit(int[] prices) {
        int max_profit=0;
        int min_buy=prices[0];

        for(int i : prices){
            max_profit=Math.max(max_profit,i-min_buy);
            min_buy=Math.min(min_buy,i);

        }
        return max_profit;

        
    }
}
