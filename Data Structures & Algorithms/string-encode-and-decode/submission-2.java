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
        List<String> ans = new ArrayList<>();
        int i = 0;
        while (i < str.length()){
            int j = i;
            while(str.charAt(j) != '#'){
                j++;
            }
            int len = Integer.parseInt(str.substring(i,j));
            j ++;
            ans.add(str.substring(j, j + len));
            i = j + len;
        }
        return ans;
    }
}