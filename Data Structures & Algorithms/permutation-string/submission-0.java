class Solution {
    public boolean checkInclusion(String s1, String s2) {

        if (s1.length()>s2.length()){
            return false;
        }

        int [] freq_s1=new int [26];
        int [] freq_s2=new int [26];

        for(int i=0;i<s1.length();i++){
            freq_s1[s1.charAt(i)-'a']++;
            freq_s2[s2.charAt(i)-'a']++;

        }

        if (match(freq_s1,freq_s2)){
            return true;

        }

        for(int i=s1.length();i<s2.length();i++){
            freq_s2[s2.charAt(i)-'a']++;
            freq_s2[s2.charAt(i-s1.length())-'a']--;

            if (match(freq_s1,freq_s2)){
                return true;
            }
            
        }          
        return false;  
    }

    private boolean match(int nums1[], int nums2[]){
            for(int i=0;i<26;i++){
                if (nums1[i]!=nums2[i]){
                    return false;
                }
            }
            return true;
        }  
}




