class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        x=[]
        for i in range(0,len(A)):
            for j in range(i+1,len(A)):
                if A[i]<A[j]:
                    x.append(A[j])
                    break
                elif j==len(A)-1:
                    x.append(-1)
        x.append(-1)
        return x