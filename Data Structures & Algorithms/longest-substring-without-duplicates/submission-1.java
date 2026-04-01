class Solution {
    public int lengthOfLongestSubstring(String s) {


        HashSet<Character> set=new HashSet<>();

        if(s==null || s.length()==0){
            return 0;
        }

        if(s.length()==1){
            return 1;
        }

        int left=0;
        int length=0;

        for(int i=0;i<s.length();i++){
            while (set.contains(s.charAt(i))){
                set.remove(s.charAt(left));
                left++;

            }

            set.add(s.charAt(i));
            length=Math.max(length,i-left+1);


        

        }

        return length;
    }
}