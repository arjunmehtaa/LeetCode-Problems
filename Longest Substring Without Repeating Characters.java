/* Longest Substring Without Repeating Characters */
/* Solution by Arjun Mehta */

class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        /* Declare required variables. */
        int begin = 0;
        int end = 0;
        int max = 0;
        HashSet<Character> hashset = new HashSet();
        
        /* Loop till end reaches the last character of string. */
        while(end<s.length()){
            
            /* If hashset contains the character at end, it means the character at begin is same as character at end. */
            /* In this case, remove the character at begin and increament begin. Update max. */
            if(hashset.contains(s.charAt(end))){
                hashset.remove(s.charAt(begin));
                begin++;
                max = Math.max(max,hashset.size());
                
            /* If hashset doesn't contain character at end, then add it to the hashset and increament end. Update max. */
            } else{
                hashset.add(s.charAt(end));
                end++;
                max = Math.max(max,hashset.size());
            }
        }
        
        /* Return max. */
        return max;
    }
}
