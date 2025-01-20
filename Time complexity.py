## Binary seach array simple programe  which having time complexity of O(log n)(base is always 2 of log)
## mean it will take 0(log n ) time to  comple the operation for expample if there is 1024 element in the array
## it will just take (log base 2 1024)= 10 step  top complet




def Binary_search(array_list,Target):
    Low=0
    High=len(array_list)-1

    while Low<=High:                    
        Average=(Low+High)//2
        if array_list[Average]==Target:  
            return True
        if(array_list[Average]<Target):
            Low=Average+1
        else:
            High=Average-1

    return False


def simple_search(array_list,Target):
    Low=0                           
    High=len(array_list)-1

    while Low<=High:

        if(array_list[Low]==Target):
            return True
        else:
            Low+=1  
            if(High<array_list[Low]):         
                break
      
    return False

array_list=[1,2,3,4,5,6,7,8,9]
Target=int(input("Enter the number you wnated to search in array"))
result=Binary_search(array_list,Target)
result=simple_search(array_list,Target)
if(result==True):
    print("Number exsist in the array")
else:
    print("Number is not exsist in the array ")
