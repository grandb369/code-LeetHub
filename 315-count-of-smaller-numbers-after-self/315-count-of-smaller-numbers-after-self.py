class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        out=[0]
        #print([random.randint(-1000,1000)for i in range(35)])
        temp=[nums.pop()]
        while nums:
            cur=nums.pop()
            l=0
            r=len(temp)-1
            c=0
            while l<=r:
                mid=(l+r)//2
                if temp[mid]<cur:
                    if l==mid:
                        c+=1
                    if c>1:
                        break
                    l=mid+1
                else:
                    r=mid-1
            #print(cur,l,temp)
            if l<len(temp) and temp[l]<cur:
                l+=1
            temp.insert(l,cur)
            out.append(l)
        return out[::-1]