/* Palindrome Number */
/* Solution by Arjun Mehta*/

class Solution {
    public boolean isPalindrome(int x) {
        
        /* Define StringBuilder s containing input x as a string. */
        StringBuilder s = new StringBuilder(Integer.toString(x));
        
        /* If s does not equal to its reverse, return false. */
        if(!s.toString().equals(s.reverse().toString())){
            return false;
        }
        
        /* Else, return true. */
        return true;
    }
}
