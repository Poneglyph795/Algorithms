

def Smallest_element(array):
     Smallest_number[index]=array[]
     Smallest_index=0

     for i in range(1 , len(array)):
      if(array[i]<Smallest_index):
               Smallest_number[index]=array[i]
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
