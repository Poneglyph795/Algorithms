class Solution:
    def kthFactor(self, n: int, k: int) -> int:
             array=[0]*n                 ##  Making  array size of n                          
             index=0

             for i in range(1,n+1):
                      if(n%i)==0:         ## n divide i is equal to zero 
                        array[index]=i    ## array.append[i]=i is  could be used here also
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
