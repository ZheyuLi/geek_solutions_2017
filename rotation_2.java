import java.util.*;
import java.lang.*;
import java.io.*;

class RotateArray{
    public void leftrotate(int arr[], int d,int n){
        int i ;
        // for each element which need to be rotated, shift it left by one
        for (i=0;i<d;i++){
            shiftleftbyone(arr,n);
            
        }
        
    }
    public void shiftleftbyone(int arr[],int n){
        int i,temp;
        // put the first element into temp
        temp = arr[0];
        // and then shift all remaining elements left by one position
        // so we use a loop to achieve it
        for (i=0;i<n-1;i++){
            arr[i] = arr[i+1];
            
        }
        // and then put the temp element back to array;
        arr[i] = temp;
        
    }
    
    // function for printing out the array after rotation;
    public static void roprint(int arr[],int n){
        int i ;
        for (i =0; i<n;i++){
            System.out.print(arr[i]+" ");
        }
        
    }
    
    
    
    
	public static void main (String[] args) {
		//code
		// new instanvce
		RotateArray rotate =new RotateArray();
		int arr[] = {1, 2, 3, 4, 5, 6, 7};
		rotate.leftrotate(arr,2,7);
		rotate.roprint(arr,7);
	}
}
