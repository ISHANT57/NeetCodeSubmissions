class Solution {
    public int[] productExceptSelf(int[] nums) {

        int n = nums.length;
        int[] result = new int[n];

        int zeroCount = 0;
        int product = 1;

        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                zeroCount++;
            } else {
                product *= nums[i];
            }
        }

        if (zeroCount > 1) {
            return result;
        }

        if (zeroCount == 1) {
            for (int i = 0; i < n; i++) {
                if (nums[i] == 0) {
                    result[i] = product;
                } else {
                    result[i] = 0;
                }
            }
            return result;
        }

        for (int i = 0; i < n; i++) {
            result[i] = product / nums[i];
        }

        return result;
    }
}
