class Solution {

    public String encode(List<String> strs) {

        StringBuilder result = new StringBuilder();
        for(String s :strs){
            int t = s.length();
            result.append(t).append('#').append(s);
        }

        return result.toString();

    }

   public List<String> decode(String str) {

    List<String> result = new ArrayList<>();
    int i = 0;

    while (i < str.length()) {
        int hashIndex = str.indexOf('#', i);
        int len = Integer.parseInt(str.substring(i, hashIndex));
        i = hashIndex + 1;
        result.add(str.substring(i, i + len));

        i = i + len;
    }

    return result;
}

}
