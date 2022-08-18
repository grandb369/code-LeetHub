public class Solution {
    public int MinSetSize(int[] arr) {
        SortedDictionary<int,int>temp = new SortedDictionary<int,int>();
        foreach(int i in arr)
        {
            if(!temp.ContainsKey(i))
            {
                temp[i]=0;
            }
            temp[i]+=1;
        }
        int n=arr.Length;
        int ans=0;
        //Console.WriteLine((int)arr.Length/2);
        foreach(var item in temp.OrderByDescending (x=>x.Value))
        {
            n-=item.Value;
            ans+=1;
            //Console.WriteLine("{0},{1}",item.Key,item.Value);
            if(n<=(int)arr.Length/2)
            {
                return ans;
            }
        }
        return ans;
    }
}