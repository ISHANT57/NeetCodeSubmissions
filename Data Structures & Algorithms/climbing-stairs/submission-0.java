class Solution {
    public int climbStairs(int n) {
        
        int prev1=1;
        int prev2=2;

        for(int i=2;i<n;i++){
            int cry=prev1+prev2;
            prev1=prev2;
            prev2=cry;

        }

        return prev2;
        
    }
}
