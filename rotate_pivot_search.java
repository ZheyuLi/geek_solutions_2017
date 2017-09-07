import java.util.*;
import java.lang.*;
import java.io.*;

class Pivotbisearch {
    public int  pivotedBSearch(int arr[],int n, int key){
        int pivot = findPivot(arr,0,n-1);
        if ( pivot ==-1){
            // we can not find pivot ,it means the array is not rotated.
            // just do binary search for the array
            return bisearch(arr,key,0,n-1);
        }
        if (arr[pivot]==key){
            return arr[pivot];
            
        }
        if(arr[0]<=key){
            return bisearch(arr,key,0,pivot-1);
        }
        return bisearch(arr,key,pivot+1,n-1);
    }
    // function return type int
    public int  bisearch(int arr[] , int key,int low ,int high){
        
        
        int mid = (low+high)/2;
        //base case
        if (high<low){
            return -1;
        }
        if (key == arr[mid]){
            return mid;
        }
        if (key< arr[mid]){
            return bisearch(arr,key,low,mid-1);
        }
        return bisearch(arr,key,mid+1,high);
        
    }
    
    // function return type int instead of void.
    public int findPivot(int arr[],int low ,int high){
        //[3,4,5,6,1,2]
        //base case
        if (high<low){
            return -1;
        }
        if (high == low ){
            return low;
        }
        
        int  mid = (low +high)/2;
        if (mid<high&&arr[mid]>arr[mid+1]){
            return mid;
        }
        if (mid >low && arr[mid] <arr[mid-1]){
            return mid -1;
        }
        // it means pivot in the first half 
        if (arr[low]>arr[mid]){
            return findPivot(arr,low,mid-1);
        }
        // it means pivot in the second half
        return findPivot(arr,mid+1,high);
        
    }
 
    
    
	 public static void main(String args[])
    {
       // Let us search 3 in below array
       int arr1[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
       int n = arr1.length;
       int key = 3;
       Pivotbisearch pbsearch = new Pivotbisearch();
       int index = pbsearch.pivotedBSearch(arr1,n,key);
       System.out.print("Index of the element is: "+index);
       
    }
}
