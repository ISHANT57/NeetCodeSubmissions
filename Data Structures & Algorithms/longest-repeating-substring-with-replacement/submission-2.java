public class Solution {

    public int characterReplacement(String s, int k) {

        int res = 0;

        for (int i = 0; i < s.length(); i++) {

            HashMap<Character, Integer> count = new HashMap<>();
            int maxFreq = 0;

            for (int j = i; j < s.length(); j++) {

                char ch = s.charAt(j);
                count.put(ch, count.getOrDefault(ch, 0) + 1);

                maxFreq = Math.max(maxFreq, count.get(ch));

                int windowLength = j - i + 1;
                int replacementsNeeded = windowLength - maxFreq;

                if (replacementsNeeded <= k) {
                    res = Math.max(res, windowLength);
                }
            }
        }

        return res;
    }
}
