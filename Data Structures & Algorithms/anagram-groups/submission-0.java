

class Solution {

    boolean isAnagram(String a, String b) {
        if (a.length() != b.length()) return false;
        char[] x = a.toCharArray();
        char[] y = b.toCharArray();
        Arrays.sort(x);
        Arrays.sort(y);
        return Arrays.equals(x, y);
    }

    public List<List<String>> groupAnagrams(String[] strs) {

        List<List<String>> res = new ArrayList<>();
        boolean used []=new boolean [strs.length];

        for(int i=0;i<strs.length;i++){
            if(used[i]){
                continue;
            }

            List<String> result=new ArrayList<>();
            result.add(strs[i]);
            used[i]=true; 


        for(int j=i+1;j<strs.length;j++){
            if ((!used[j])&& isAnagram(strs[i],strs[j])){
                result.add(strs[j]);
                used[j]=true;

            }
        }

         res.add(result);
        }
        return res;
    }
}