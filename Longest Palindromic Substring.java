/* Longest Palindromic Substring */
/* Solution by Arjun Mehta (inspired by Nick White) */

class Solution {
    public String longestPalindrome(String s) {
        
        /* Declare required variables. */
        int length1;
        int length2;
        int start = 0;
        int end = 0;
        
        /* Loop till the end of string. */
        for(int i=0; i<s.length(); i++){
            
            /* Check length for both types of palindrome (odd and even length) and set foundlength to the max of the two. */
            length1 = checkFromMiddle(s, i , i);
            length2 = checkFromMiddle(s, i, i+1);
            int foundlength = Math.max(length1, length2);
            
            /* If foundlength is greater than previous values, update start and end. */
            if(foundlength > end-start){
                start = i - (foundlength-1)/2;
                end = i + foundlength/2;
            }
        }
        
        /* Return the longest palindrome substring. */
        return s.substring(start,end+1);
    }
    
    /* Helper function to find longest palindrome starting from the middle. */
    public int checkFromMiddle(String s, int left, int right){
        
        /* If characters at indexes left and right are equal, update left and right to broaden the palindromic string. */
        while(left>=0 && right<s.length() && s.charAt(left)==s.charAt(right)){
            left --;
            right ++;
        }
        
        /* Return length of palindrome found. */
        return right-left-1;
    }
}
