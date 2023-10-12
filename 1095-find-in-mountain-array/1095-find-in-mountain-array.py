# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        leng = mountain_arr.length()
        left, right = 0, leng-1
        # find peak
        while left < right: # there is definitely a peak, so we use '<' instead of '<='
            mid = (left+right) // 2
            if mountain_arr.get(mid) >= mountain_arr.get(mid+1):
                right = mid
            else:
                # 'left' and 'right' could be consecutive
                # 'mid' intends to be 'left', so we need 'left' to plus one to avoid endless loop
                left = mid + 1 
        peak = left
        if target == mountain_arr.get(peak):
            return peak

        # search behind the peak
        l, r = 0, peak-1
        while l <= r: # there may not be a target behind the peak, so using '<='
            print(l, r, end =' ')
            mid = (l + r) // 2
            print('1:', mid)
            cur = mountain_arr.get(mid)
            if cur == target:
                return mid
            elif cur > target:
                r = mid - 1
            else:
                l = mid + 1
                
        # search after the peak
        l, r = peak+1, leng-1
        while l <= r: # there may not be a target after the peak, so using '<='
            print('2:', mid)
            mid = (l + r) // 2
            cur = mountain_arr.get(mid)
            if cur == target:
                return mid
            elif cur > target:
                l = mid + 1
            else:
                r = mid - 1
        return -1