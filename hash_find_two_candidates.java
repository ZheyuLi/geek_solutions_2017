import java.util.*;
import java.lang.*;
import java.io.*;

class HashFindTwoCandidates {
    
    public boolean hashfind(int[] arr, int sum){
        // initial value
        boolean[] binmap = new boolean[100000];
        for (int i =0;i<arr.length; i++){
            int temp = sum - arr[i];
            if (temp>0&& binmap[temp]){
                return true;
            }
            binmap[arr[i]] =true;
        }
        return false;
    }
    
    
    
	public static void main (String[] args) {
		//code
		int A[] = {1, 4, 45, 6, 10, 8};
        int n = 16;
		HashFindTwoCandidates hfind = new HashFindTwoCandidates();
		if (hfind.hashfind(A,n)){
		    System.out.print("find");
		}else{
		    System.out.print("noooooooooooo");
		}
	}
}
