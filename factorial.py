class Solution:
    def kthFactor(self, n: int, k: int) -> int:
             array=[0]*n
             index=0

             for i in range(1,n+1):
                      if(n%i)==0:
                        array[index]=i
                        index+=1
             if(k>len(array)):
                return -1  
             else:
              result=array[k]-1
              return result
    
            

solution=Solution()
n=12
k=3
result=solution.kthFactor(n,k)
print(result)