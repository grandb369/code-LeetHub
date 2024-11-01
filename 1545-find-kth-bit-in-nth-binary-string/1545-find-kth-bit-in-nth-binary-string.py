class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        val='0'
        for i in range(2,n+1):
            inv=bin(int('1'*len(val),2)^int(val,2))
            if inv[0]=='-':
                inv=inv[3:]
            else:
                inv=inv[2:]
            val=val+'1'+inv[::-1]
        #print(val)
        #print('011100110110001')
        return val[k-1]