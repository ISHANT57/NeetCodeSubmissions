class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        // Step 1: Frequency count
        HashMap<Integer, Integer> freq = new HashMap<>();

        for (int num : nums) {
            if (freq.containsKey(num)) {
                freq.put(num, freq.get(num) + 1);
            } else {
                freq.put(num, 1);
            }
        }

        int[] result = new int[k];

        // Step 2: Find top k frequent elements
        for (int i = 0; i < k; i++) {

            int maxFreq = -1;
            int maxKey = 0;

            // find element with maximum frequency
            for (int key : freq.keySet()) {
                if (freq.get(key) > maxFreq) {
                    maxFreq = freq.get(key);
                    maxKey = key;
                }
            }

            result[i] = maxKey;

            // remove selected element
            freq.remove(maxKey);
        }

        return result;
    }
}
