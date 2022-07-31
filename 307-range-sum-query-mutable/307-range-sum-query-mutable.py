class NumArray:

    def __init__(self, nums: List[int]):
        self.tree=[0 for i in range(4*len(nums))]
        self.n=len(nums)
        if self.n>0:
            self.build(nums,0,0,len(nums)-1)
            #print(self.tree)
        
        
    def build(self, nums, index, l, r):
        if l==r:
            self.tree[index]=nums[l]
            return nums[l]
        mid=(l+r)//2
        left=self.build(nums,2*index+1,l,mid)
        right=self.build(nums,2*index+2,mid+1,r)
        self.tree[index]=left+right
        return self.tree[index]

    def tree_update(self, index, l, r, target, val):
        if l==r:
            diff=val-self.tree[index]
            self.tree[index]=val
            return diff
        mid=(l+r)//2
        if target>mid:
            diff=self.tree_update(2*index+2,mid+1,r,target,val)
        else:
            diff=self.tree_update(2*index+1,l,mid,target,val)
        self.tree[index]+=diff
        return diff
    
    def update(self, i: int, val: int) -> None:
        if self.n>0:
            self.tree_update(0,0,self.n-1,i,val)
            #print(self.tree)

    def tree_sum(self, index, l, r, i, j):
        if l>j or r<i:
            return 0
        if i<=l and j>=r:
            return self.tree[index]
        mid=(l+r)//2
        if i>mid:
            return self.tree_sum(2*index+2,mid+1,r,i,j)
        elif j<=mid:
            return self.tree_sum(2*index+1,l,mid,i,j)
        return self.tree_sum(2*index+2,mid+1,r,mid+1,j)+self.tree_sum(2*index+1,l,mid,i,mid)
    
    def sumRange(self, i: int, j: int) -> int:
        if self.n>0:
            return self.tree_sum(0,0,self.n-1,i,j)
        return 0


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)