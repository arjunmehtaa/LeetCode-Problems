/* Container With Most Water */
/* Solution by Arjun Mehta*/

class Solution {
    public int maxArea(int[] height) {
        
        /* Declare required variables. */
        int maxsize = 0;
        int l = 0;
        int r = height.length-1;
        
        /* Loop till l is less than r. */
        while(l<r){
            
            /* If size is greater than  maxsize, set maxsize. */
            maxsize = Math.max(maxsize, Math.min(height[l],height[r])*(r-l));
            
            /* Increment l / decrement r  based on value of height. */
            if(height[l]<height[r]) l++;
            else r--;
        }
        
        /* Return maxsize. */
        return maxsize;
    }
}
