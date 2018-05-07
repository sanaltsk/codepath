class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        a=[]
        maxn=2*A-1
        mid = A-1
        for i in range(0,maxn):
            for j in range(0,maxn):
                a.append([i,j])
    
        new_matrix=[]
        for j in a:
            n = max(abs(j[0]-mid),abs(j[1]-mid))+1
            new_matrix.append(n)
        return [new_matrix[i:i+maxn] for i in range(0,len(new_matrix),maxn)]
