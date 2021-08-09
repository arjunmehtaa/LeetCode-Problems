/* Two Sum */
/* Solution by Arjun Mehta */

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        /* Initialize ans vector. */
        vector<int> ans;
        
        /* For every element in nums vector, loop through nums vector using nested for loop. */
        for(int i=0;i<nums.size();i++){
            for(int j=0;j<nums.size();j++){
                
                /* If i-th and j-th element of vector add to target and i is not equal to j, push i and j in ans vector. */
                if(i!=j&&(nums[i]+nums[j]==target)){
                    ans.push_back(i);
                    ans.push_back(j);
                    
                    /* Return the ans vector. */
                    return ans;
                }
            }
        }
        
        /* Return the ans vector. */
        return ans;
    }
};
