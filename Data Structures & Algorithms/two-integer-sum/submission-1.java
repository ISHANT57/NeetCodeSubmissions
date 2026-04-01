public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> arr = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            arr.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (arr.containsKey(diff) && arr.get(diff) != i) {
                return new int[]{i, arr.get(diff)};
            }
        }

        return new int[0];
    }
}