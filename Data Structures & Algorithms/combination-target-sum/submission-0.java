class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {

        List<List<Integer>> result = new ArrayList<>();
        List<Integer> sum = new ArrayList<>();

        backtrack(nums, target, sum, 0, result);

        return result;
    }

    public void backtrack(int[] nums, int target, List<Integer> sum, int i, List<List<Integer>> result) {

        if (target == 0) {
            result.add(new ArrayList<>(sum));
            return;
        }

        if (target < 0 || i == nums.length) {
            return;
        }

        sum.add(nums[i]);
        backtrack(nums, target - nums[i], sum, i, result);

        sum.remove(sum.size() - 1);

        backtrack(nums, target, sum, i + 1, result);
    }
}