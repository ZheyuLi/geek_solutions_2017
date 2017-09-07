import java.util.*;
import java.lang.*;
import java.io.*;

class RotateArray {
    
    public void leftrotate(int[] arr, int d, int n){
        reverse(arr,0,d-1);
        reverse(arr,d,n-1);
        reverse(arr,0,n-1);
        
        
    }
    
    public void reverse(int[] arr, int start, int end){
        int tmp;
        while (start < end){
            tmp = arr[start];
            arr[start] = arr[end];
            arr[end] = tmp;
            start++;
            end--;
            
        }
        
    }
    public void roprint(int arr[], int n){
        int i;
        for (i=0;i<n;i++){
            System.out.print(arr[i]+ " ");
        }
        
        
    }
    
    
	public static void main (String[] args) {
		//code
		RotateArray rotate = new RotateArray();
		int arr[] = {1,2,3,4,5,6,7};
		
	
		rotate.leftrotate(arr,2,7);
		rotate.roprint(arr,7);
		
	}
}
