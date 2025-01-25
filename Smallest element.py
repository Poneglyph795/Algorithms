## Find the smallest number in the array

def Smallest_element(array): 
     Smallest_number=array[0]      ## Puting zero index  number in Smallest_number variable   
     Smallest_index=0               ## Assing the zero  to Smallest_index

     for i in range(1 , len(array)):     ##  Because asign smallest_number at zero index so start form 1 , len(array)
      if(array[i]<Smallest_index):       ##  Condition if array [i] smallest than zero index array[0] 
               Smallest_number=array[i]
               Smallest_index=i
     return Smallest_index,Smallest_number



## Use fucntion to write selction sort:
def selectionSort(array):
     New_array=[]
     for i in range(len(array)):
          smallest=Smallest_element(array)
          New_array.append(array.pop(smallest))
     return New_array

     
            
            
array=[2,3,4,5,6,7]
Result=Smallest_element(array)
selectionSort(array)
print(Result)
