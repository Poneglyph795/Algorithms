#include<stdio.h>

int binarysearch(int a[], int target, int size);  //Function declaration

int main()
{
  int a[]= {1,2,3,4,5,6,7};
  int size = sizeof(a) / sizeof(a[0]);   // Size of one elemnt int = 4 byte  so sizeof(a)=28 divde by size ([0])=4  is 7 bytes 
  int target;
  printf("Enter the targer number");
  scanf("%d",&target);
  int result = bubbleshot(a,target,size);  // Variable function  ---  1.Pasing pointer of array  2.Do not declare data type 
  if (result!= -1)
    printf("Number exists at index %d ",result);
  else 
     printf("Number does not exist in the array ");
     
  return 0;
}



int binarysearch(int a[],int target, int size) //  function defination
{
  int left=0;
  int right=size-1;
  while(left <= right)
  {
    int mid= (left + right) /2;   // position of mid array 
     if (a[mid]==target)
        return mid;
        
    else if (a[mid]< target)
       left= mid +1;
    else 
     right= mid  -1;
  }
 return -1;
}
