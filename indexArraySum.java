import java.util.*;
import java.lang.*;
import java.io.*;
/*
1) Compute sum of all array elements. Let this sum be 'arrSum'.

2) Compute R0 by doing i*arr[i] for given array. 
   Let this value be currVal.

3) Initialize result: maxVal = currVal // maxVal is result.

// This loop computes Rj from  Rj-1 
4) Do following for j = 1 to n-1
......a) currVal = currVal + arrSum-n*arr[n-j];
......b) If (currVal > maxVal)
            maxVal = currVal   

5) Return maxVal

*/
class IndexArrSum {
    
    public static int getsum(int[] arr){
        // get the arrsum and i*arr[i]
        int arrSum=0 ;
        int indexValue=0;
        for (int i =0;i<arr.length;i++){
            arrSum = arrSum + arr[i];
            indexValue= indexValue + i*arr[i];
        }
        int maxValue = indexValue;
        for (int j = 1;j<arr.length;j++){
            indexValue = indexValue+ arrSum - arr.length*arr[arr.length-j];
            if (indexValue > maxValue){
                maxValue = indexValue;
            }
        }
        return maxValue;
    }
    
    
    
	public static void main (String[] args) {
		//code
		
		int[] arr = {10, 1, 2, 3, 4, 5, 6, 7, 8, 9};
		
		IndexArrSum inarrsum = new IndexArrSum();
		System.out.print("the max index multiply element is :"+inarrsum.getsum(arr));
		
	}
}
