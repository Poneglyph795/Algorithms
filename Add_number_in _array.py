#Simple program which add two number form the array which having complexity of o(n)  
##Question was Array1 = [2,7,11,15]  
##Array2 = [3,2,4]  
##Array3 = [3,3]  
##OUTPUT = 9,6,6


def Sum_Array(Array1):
    first = Array1[0]
    second = Array1[1]
    result=first+second
    return  result

def Sum_Array2(Array2):
    first = Array2[1]
    second = Array2[2]
    result1=first+second
    return result1

def Sum_Array3(Array3):
    first = Array3[0]
    second = Array3[1]
    result2=first+second
    return result2


Array1=[2,7,11,15]
Array2=[3,2,4]
Array3=[3,3]

First_result=Sum_Array(Array1)
print(First_result)

Second_result=Sum_Array2(Array2)
print(Second_result)

Third_result=Sum_Array3(Array3)
print(Third_result)


