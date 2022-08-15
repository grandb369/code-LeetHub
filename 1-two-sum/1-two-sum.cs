public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Hashtable temp = new Hashtable();
        int [] ans = {0,0};
        for(int i=0;i<nums.Length;i++)
        {
            if(temp.ContainsKey(nums[i]))
            {
                int x=(int)temp[nums[i]];
                int [] res={x,i};
                return res;
            }
            if(!temp.ContainsKey(target-nums[i]))
            {
                temp.Add(target-nums[i],i);
            }
            
        }
        return ans;
    }
}