class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        HashMap<String, List<String>> map = new HashMap<>();

        for (String s : strs) {

            // frequency array for current string
            int[] freq = new int[26];

            for (char ch : s.toCharArray()) {
                freq[ch - 'a']++;
            }

            // convert frequency array to string key
            String key = Arrays.toString(freq);

            // if key not present, create new list
            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }

            // add string to its anagram group
            map.get(key).add(s);
        }

        return new ArrayList<>(map.values());
    }
}
