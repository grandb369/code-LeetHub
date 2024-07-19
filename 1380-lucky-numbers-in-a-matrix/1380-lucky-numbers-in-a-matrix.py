class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        temp=[i for i in matrix[0]]
        out=[]
        for r in range(1,len(matrix)):
            for c in range(len(matrix[0])):
                temp[c]=max(matrix[r][c],temp[c])
        for r in range(len(matrix)):
            val=min(matrix[r])
            index=matrix[r].index(val)
            if matrix[r][index]==temp[index]:
                out.append(temp[index])
        return out