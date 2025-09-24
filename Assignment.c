#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


//Function Signatures
void intersection(int[], int[], int, int);
void mergeSort(int[], int, int);
void merge(int[], int, int, int);
bool deleteElement(int[], int, int);

int main()
{
    //Initialisation of arrays
    int A[] = {8, 1, 5, 0, 13, 2, 6};
    int B[] = {19, 2, 3, 7, 12, 9, 4};
    
    //Counter variable
    int i;

    //Sizes of arrays initilaised because parameters are passed by reference
    int sizeA = sizeof(A)/sizeof(A[0]);
    int sizeB = sizeof(B)/sizeof(B[0]);

    //Variables for deleting the ith element
    int index;
    bool indexA, indexB;

    //Displays unsorted Array A
    printf("Array A(Unsorted):\n");

    for (i = 0; i < sizeA; i++)
    {
        printf("%d ",A[i]);
    }//end for
    
    //Function call to sort Array A
    mergeSort(A,0,sizeA - 1);

    //Displays sorted Array A
    printf("\nArray A(Sorted):\n");

    for (i = 0; i < sizeA; i++)
    {
        printf("%d ",A[i]);
    }//end for

    //Displays unsorted Array B
    printf("\n\nArray B(Unsorted):\n");

    for (i = 0; i < sizeB; i++)
    {
        printf("%d ",B[i]);
    }//end for
    
    //Function call to sort Array B
    mergeSort(B,0,sizeB - 1);

    printf("\nArray B(Sorted):\n");

    for (i = 0; i < sizeB; i++)
    {
        printf("%d ",B[i]);
    }//end for

    printf("\n\nSelect an element to delete (0 to %d)?\n",sizeA - 1);
    scanf("%d",&index);

    indexA = deleteElement(A,sizeA,index);
    indexB = deleteElement(B,sizeB,index);

    //To delete the element
    if (indexA == true && indexB == true)
    {
        sizeA--;
        sizeB--;
    }
    
    //Displays Array A with ith element deleted
    printf("\n\nNew array of A\n");

    for (i = 0; i < sizeA; i++)
    {
        printf("%d ",A[i]);
    }//end for

    //Displays Array B with ith element deleted
    printf("\n\nNew array of B\n");

    for (i = 0; i < sizeB; i++)
    {
        printf("%d ",B[i]);
    }

    printf("\n\nIntersection of Arrays:\n");

    //Function Intersection is called
    intersection(A,B,sizeA,sizeB);
    printf("\n");

    return 0;
}//end main


void mergeSort(int A[],int left,int right)
{
    int mid;

    if (left < right)
    {
        mid = left + (right - left) / 2;
        
        //Sorts the left and right side of the array
        mergeSort(A, left, mid);
        mergeSort(A, mid+1, right);
        
        //Merge function call after splitting the array
        merge(A, left, mid, right);
    }//end if
    
}//end mergeSort


//Merge function allows the 2 subarrays to merge into a sorted array
void merge(int A[],int left,int mid,int right)
{
    //Index Variables
    int i,j,k;

    //Variables for sizes of 2 temporary arrays
    int n1,n2;

    //n1 is the size of the subarray which includes the numbers from the left to middle element of the Array
    n1 = mid - left + 1;

    //n2 is the size of the subarray which includes the numbers from the middle to the right element of the Array
    n2 = right - mid;

    int leftSide[n1], rightSide[n2];

    //Copying data to the temporary arrays
    for (i = 0; i < n1; i++)
    {
        leftSide[i] = A[left + i];
    }//end for

    for (j = 0; j < n2; j++)
    {
        rightSide[j] = A[mid + 1 + j];
    }//end for

    i = 0;
    j = 0;

    //Used to keep track of current position of array
    k = left;

    while (i < n1 && j < n2)
    {
        
        //If the element in leftSide[i] is less than or equal to element in rightSide[j]
        if (leftSide[i] <= rightSide[j])
        {
            //The element is put in array A[k]
            A[k] = leftSide[i];
            i++;
        }//end if
        else
        {
            //Puts the element into array A[k] 
            A[k] = rightSide[j];
            j++;
        }//end else
        k++;
    }//end while
    

    //Copies remaining elements of left[] if any are left
    while (i < n1)
    {
        A[k] = leftSide[i];
        i++;
        k++;
    }//end while

    
    //Copies remaining elements of right[] if any are left
    while (j < n2)
    {
        A[k] = rightSide[j];
        j++;
        k++;
    }//end while

}//end merge


//Intersection function prints the intersection betweens the arrays
void intersection(int A[],int B[],int sizeA,int sizeB)
{
    //index variable
    int i;
    
    //Variables for Binary Search
    int low, mid, high;

    //Merge sort function called to organise arrays
    mergeSort(A,0,sizeA - 1);
    mergeSort(B,0,sizeB - 1);

    //Binary search to compare elements of A and B to see if they are the same 
   for (i = 0; i < sizeA; i++)
   {
        //Index of the low variable is set to the start of array A
        low = 0;

        //Index of the high variable is set to the end of the array B
        high = sizeB - 1;

        while (low <= high)
        {
            mid = (low + high) / 2;

            //If middle index is equal to the current element in the array
            if (B[mid] == A[i])
            {
                //Displays value and moves on to the next iteration
                printf("%d ",A[i]);
                break;
            }//end if
            //Else if the index is less than the current element
            else if (B[mid] < A[i])
            {
                //low will then update to search through the upper half of the remaining part of the array
                low = mid + 1;
            }//end else if
            else
            {
                //else high will update to search at the lower half of the remaining part of the array
                high = mid - 1;  
            }//end else
        }//end while     
   }//end for
}//end intersection


//deleteElement function deletes ith element
bool deleteElement(int A[],int size,int index)
{
    //Boolean variable initialised 
    bool deleted = false;
    int i;

    //To make sure number put in is more than 0 but smaller than array
    if (index < 0 || index >= size)
    {
        printf("\n\nError! Invalid Index\n");
        
        return deleted;
    }//end if
    
    //For loop that runs from the index to the penultimate element
    for (i = index; i < size - 1; i++)
    {
        A[i] = A[i + 1];
    }//end for

    deleted = true;
        
    printf("\n\nElement %d has been deleted.\n",index);

    return deleted;
}//end delElement 