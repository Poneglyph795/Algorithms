#include<stdio.h>
#include<stdbool.h>    //  Have to mention that for using bool in code


void findDuplicateds(int arr[], int n)
{
  bool visted[n];     //Create an array of  size of n 
  bool found=false;   // Remove the garbage value     
  for(i=0;i<n;i++)
  visted[i]=false;   // Removing the garbage value from  the array
  
  for (i=0;i<n;i++)
  {
    if(visted[arr[i]]== true)
    {
      printf("%d is duplicate\n",arr[i]);
    }
    else
    {
      visted [arr[i]]=true
    }
    
  }
}

// By using brute force method

void BruteFoce(int arr[], int n)
{

  
}


int main()
{
  int arr1[]= {0,3,1,2};
  int  size = sizeof(arr1)/sizeof(arr1[0]);
  printf("Duplicates in arr1");
  findDuplicateds(arr1,size);
  BruteFoce(arr1,size)
  printf("\n");
  
  int arr2[]= {1,2,3,4,3,2};
  int  size = sizeof(arr1)/sizeof(arr1[0]);
  printf("Duplicates in arr1");
  findDuplicateds(arr1,size);
  BruteFoce(arr2,size)
  
  return 0;
}


