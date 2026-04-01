class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

        int n1 = nums1.length;
        int n2 = nums2.length;

        int[] res = new int[n1 + n2];

        int idx = 0;

        for (int x : nums1) {
            res[idx++] = x;
        }

        for (int x : nums2) {
            res[idx++] = x;
        }

        java.util.Arrays.sort(res);

        int n = res.length;

        if (n % 2 == 1) {
            return res[n / 2];
        }

        return (res[n / 2 - 1] + res[n / 2]) / 2.0;
    }
}