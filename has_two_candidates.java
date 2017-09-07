import java.util.*;
import java.lang.*;
import java.io.*;

class QuickFindTwoCandidates {
    
    public int hasTwoCands(int[] arr,int size,int sum){
        quicksort(arr,0,size-1);
        int left =0 ;
        int right = size -1;
        while(left<right){
            if (arr[left] +arr[right] ==sum){
                return 1;
            }else if (arr[left]+arr[right]<sum){
                left++;
            }else{
                right--;
            }
        }
        return 0;
    }
    

    
    public static int partition(int[] arr, int low ,int high){
        //set last element of the array to be the pivot 
        int pivot = arr[high];
        // set the smaller index of the element to be -1 as the initial value
        int i = low -1;
        // loop through all the element before pivot
        for (int j = low; j< high-1;j++){
            // compare each element with pivot, if it is less than pivot then
            // swap it with the smaller one
            if (arr[j]< pivot ){
                i++;
                int temp ;
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            //if it is greter than pivot ,do nothing --> keep its position as it is
            // after loop through all the element before pivot, swap pivot with the elment 
            //next to the current smaller one 

        }
        // after the loop, do the swapping between pivot and 
        //the one next to the current smaller element
        int temp = arr[i+1];
        arr[i+1] = pivot;
        pivot = temp;
        // so now the pivot is no its right position which is i+1.
        return i+1;
    }
    
    public static void quicksort(int[] arr, int low ,int high){
        // because pi +1==> low and pi-1 ==> high are changing all the time
        // so some constrints needs to be set.
        if (low <high){
            
            int pi = partition(arr, low, high);
            
            quicksort(arr,low,pi -1);
            quicksort(arr,pi+1,high);
        }
    }
    
    
    
    
	public static void main (String[] args) {
		//code
		QuickFindTwoCandidates qfcands = new QuickFindTwoCandidates();
		
		int A[] = {1, 4, 45, 6, 10, -8};
        int n = 16;
        int arr_size = 6;
        if (qfcands.hasTwoCands(A,6,16) ==1){
            System.out.print("Array has two "+ 
                         "elements with sum 16");
        }else{
            System.out.print("Array doesn't have "+
                      "two elements with sum 16 ");
        }
		
	}
}
