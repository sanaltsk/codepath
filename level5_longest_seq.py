class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        A=list(A)
        A.sort()
        max=1
        count = 1
        for i in range(1,len(A)):
            if(A[i]-A[i-1]==1):
                count+=1
            elif (A[i]==A[i-1]):
                continue
            else:
                count=1;
            if (count > max):
                max = count
        return max