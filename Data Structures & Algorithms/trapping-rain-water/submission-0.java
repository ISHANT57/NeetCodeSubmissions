class Solution {
    public int trap(int[] height) {
        int result=0;
        int left=0;
        int right=height.length-1;

        if (height==null || height.length==0){
            return 0;
        }

        int left_max=height[left];
        int right_max=height[right];

        while(right>left){
            if (right_max>left_max){
                left++;

                left_max=Math.max(left_max,height[left]);
                result+=left_max-height[left];
            }

            else{
                right--;
                right_max=Math.max(right_max,height[right]);
                result+=right_max-height[right];
            }
        }


        return result;



        
    }
}
