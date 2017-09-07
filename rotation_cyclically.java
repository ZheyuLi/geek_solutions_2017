import java.util.*;
import java.lang.*;
import java.io.*;

class RotateArray {
    
    public void cycrotate(int[] arr, int n){
        int temp;
        // store the last element into tmp value
        temp = arr[n-1];
        // shift the remaining elements left by one position
        int i ;
        for (i=n-1;i<0;i--){
            arr[i] = arr[i-1];
            
        }
        arr[0]= temp;
        
    }
    
  
        
    public void roprint(int arr[], int n){
        int i;
        for(i=0;i<n;i++){
            System.out.print(arr[i]+ " ");
        }
        
        
    }
    
    
	public static void main (String[] args) {
		//code
		RotateArray rotate = new RotateArray();
		int arr[] = {1,2,3,4,5,6,7};
		
	
		rotate.cycrotate(arr,7);
		rotate.roprint(arr,7);
		
	}
}
